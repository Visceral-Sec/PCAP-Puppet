#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <arpa/inet.h> //for checksums stuff
#include <stdlib.h>
#include <time.h>

struct packetStruct
{
    char sMac[6];
    char dMac[6];
    char source[4];
    char target[4];
    char sPort[2];
    char dPort[2];
    char payload[100];
    char identification[2];
    char seqNum[2];
};
struct packetStruct g_currentFrame;

//for testing mainly
void read_pcap_out(char pcapOut[], uint16_t pcapLen)
{
    for (uint16_t x = 0; x < pcapLen; x++)
    {
        printf("%c", pcapOut[x]);
    }
    return;
}

// the below function is from http://www.microhowto.info/howto/calculate_an_internet_protocol_checksum_in_c.html (author: Dr Graham D Shaw; accessed: 18/05/2021 - this needs to be cited properly) to create a C function to calc an rfc 1071 checksum
// it has been reformatted and altered to keep with the style of the other code (and so that it works in our context)

uint16_t calc_checksum(void* vdata, uint16_t length) //uint16_t is a 16-bit unsigned uint16_t
{
    char* payload = (char*)vdata; //Cast the payload pointer to one that can be indexed.
    uint32_t acc = 0xffff; // Initialise the accumulator
    for (uint16_t i = 0; (i + 1) < length; i += 2) // Handle complete 16-bit blocks.
    {
        uint16_t word; // a word being 16-bits
        memcpy(&word, payload + i, 2);
        acc += ntohs(word);
        if (acc > 0xffff)
        {
            acc -= 0xffff;
        }
    }
    if (length&1) // Handle any partial block at the end of the payload.
    {
        uint16_t word = 0;
        memcpy(&word, payload + length - 1, 1);
        acc += ntohs(word);
        if (acc > 0xffff)
        {
            acc -= 0xffff;
        }
    }
    return htons(~acc); // Return the checksum in network byte order.
}

//takes array and inserts it into the desired position in a chosen array
void insert_var_into(char arrIn[], char arrOut[], uint16_t l_emptyPointer, uint16_t bytesToWrite)
{
    for (uint16_t x = 0; x < bytesToWrite; x++)
    {
        arrOut[l_emptyPointer++] = arrIn[x];
    }
    return;
}

//parse payload from python frontend
uint16_t * condense_char(char currentParam[], uint16_t paramSize)//Turns a two digit string into a number
{
    uint16_t l_emptyPointer = 0; //points to the last filled entry (ofc -1 isnt filled but it has to start somewhere)
    static uint16_t returnParam[/*paramSize - 3 - (paramSize - 7)/2*/10];
    for(uint16_t i = 0; i < paramSize; i += 3) //robert's magic to convert to suitable uint16_t arrays
    {
        uint16_t digit1 = currentParam[i] - 48;
        uint16_t digit2 = currentParam[i + 1] - 48;
        if(digit1 > 9)
        {
            digit1 -= 39;
        }
        if(digit2 > 9)
        {
            digit2 -= 39;
        }
        returnParam[l_emptyPointer++] = digit1*16 + digit2; //incriment endPointer after assignment
    }
    
    return returnParam;
}

//converts the incoming payload into the correct formats for writing
void data_parse(char sMac[17], char dMac[17], char target[11], char source[11], char sPort[5], char dPort[5], char payload[], char identification[], char seqNum[])
{   
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in g_currentFrame.sMac
    for(uint16_t i = 0; i < 6; i++)
    {
    	g_currentFrame.sMac[i] = condense_char(sMac, 17)[i];
    }
    for(uint16_t i = 0; i < 6; i++)
    {
    	g_currentFrame.dMac[i] = condense_char(dMac, 17)[i];
    }
    for(uint16_t i = 0; i < 4; i++)
    {
    	g_currentFrame.target[i] = condense_char(target, 11)[i];
    }
    for(uint16_t i = 0; i < 4; i++)
    {
    	g_currentFrame.source[i] = condense_char(source, 11)[i];
    }
    for(uint16_t i = 0; i < 2; i++)
    {
    	g_currentFrame.sPort[i] = condense_char(sPort, 5)[i];
    }
    for(uint16_t i = 0; i < 2; i++)
    {
    	g_currentFrame.dPort[i] = condense_char(dPort, 5)[i];
    }
    for(uint16_t i = 0; i < 2; i++)
    {
    	g_currentFrame.identification[i] = condense_char(identification, 5)[i];
    }
    for(uint16_t i = 0; i < 2; i++)
    {
    	g_currentFrame.seqNum[i] = condense_char(seqNum, 5)[i];
    }
    
    strcpy(g_currentFrame.payload, payload);
    return;
}

//is run once at the start of the program so that it is only at the top of the file
void pcap_header_construct(FILE *fpWrite)
{
	int pcapHeaderLen = 24;
    	char pcapHeader[24] = {0xD4, 0xC3, 0xB2, 0xA1, 0x02, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00};
	
    	fwrite(pcapHeader, 1, pcapHeaderLen, fpWrite);
    	return;
}

//returns num^pow as a long uint16_t
long power(uint16_t num, uint16_t pow)
{
	long result = 1;
	for(uint16_t i = 0; i < pow; i++)
	{
		result *= num;
	}
	
	return(result);
}

//adds on to pcap epoch in hex and little endian
void epoch(char pcap[], uint16_t l_emptyPointer)
{
    long seconds;
    seconds = time(NULL);
    
    long divisor = power(16, 9);
    char hex[5];
    uint16_t temp;
    
    for(int i = 9; i >= 0; i--)// i needs to be an int for some reason
    {
    	uint16_t result = seconds/divisor;
    	if(i % 2 == 1)
    	{
    		temp = result;
    	}
    	else
    	{
    		hex[i/2] = (temp * 16) + result;
	}
    	seconds -= result * divisor;
    	divisor /= 16;
    }
    
    insert_var_into(hex, pcap, l_emptyPointer, 4);
    
    return;
}

//is functional and dynamic for a single packet but needs some work for multiple
void header_construct(char pcap[], char etherFrame[], uint16_t etherFrameLen)
{
    //is only written at the start of a pcap
    uint16_t l_emptyPointer = 0;
	
    //is after every packet 
    epoch(pcap, l_emptyPointer); l_emptyPointer += 4;
    pcap[l_emptyPointer++] = 0x81; pcap[l_emptyPointer++] = 0x08; pcap[l_emptyPointer++] = 0x03; pcap[l_emptyPointer++] = 0x00;//milliseconds since last second, is currently just static because it doesn't really matter
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//length of packet excluding header
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//the same thing again for some reason it wants it twice
    insert_var_into(etherFrame, pcap, 16, etherFrameLen);
    return;
}

void dns_req_construct(char dnsSegment[], int type)
{
    uint16_t l_emptyPointer = 0;
    //uint16_t flags = rand() % 16;
    insert_var_into(g_currentFrame.identification, dnsSegment, l_emptyPointer, 2); l_emptyPointer += 2;//remains static throughout interaction
    //dnsSegment[l_emptyPointer++] = flags >> 8;
    //dnsSegment[l_emptyPointer++] = flags & 0x0FF; //0100 for standard query, 8580 for standard query response//is randomized for compilation's sake
    dnsSegment[l_emptyPointer++] = 0x01; dnsSegment[l_emptyPointer++] = 0x00;//flags for request
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //how many questions
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = type; //how many answers, would be 0x0001 for a response
    //number of name server resource records in authority records and number of name server resource records in authority records? is currently blank for compliation's sake
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; 
    dnsSegment[l_emptyPointer++] = 0x03; insert_var_into(g_currentFrame.payload, dnsSegment, l_emptyPointer, strlen(g_currentFrame.payload)); l_emptyPointer += strlen(g_currentFrame.payload); dnsSegment[l_emptyPointer++] = 0x00;//adding the query section to the pcap?
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //host
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //class
    
    if(type == 1)
    {
    	dnsSegment[2] = 0x85;
    	dnsSegment[3] = 0x80;
    	
    	dnsSegment[l_emptyPointer++] = 0xc0; dnsSegment[l_emptyPointer++] = 0x0c; //Name?
	dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //host
	dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //class
	dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; 
	insert_var_into(g_currentFrame.target, dnsSegment, l_emptyPointer, 4);
    }
}

//slaps icmp segment into the frame
void icmp_construct(char icmpReqSeg[], uint16_t segLen, char type)
{
    uint16_t l_emptyPointer = 0;
    icmpReqSeg[l_emptyPointer++] = type;//icmp ping request
    icmpReqSeg[l_emptyPointer++] = 0x00;//code is 0
    icmpReqSeg[l_emptyPointer++] = 0x00; icmpReqSeg[l_emptyPointer++] = 0x00;//checksum, this is a placeholder for later in the function
    insert_var_into(g_currentFrame.identification, icmpReqSeg, l_emptyPointer, 2); l_emptyPointer +=2; //identifier?
    insert_var_into(g_currentFrame.seqNum, icmpReqSeg, l_emptyPointer, 2); l_emptyPointer +=2; //sequence number
    insert_var_into(g_currentFrame.payload, icmpReqSeg, l_emptyPointer, strlen(g_currentFrame.payload));
    uint16_t checksum = calc_checksum(icmpReqSeg, segLen);
    icmpReqSeg[2] = checksum & 0x00FF;
    icmpReqSeg[3] = checksum >> 8;
    return;
}

void insert_udp_header(char udpSegment[], uint16_t udpSegmentLen, uint16_t dns)
{
    uint16_t dnsLen = 0;
    uint16_t l_emptyPointer = 0;
    insert_var_into(g_currentFrame.sPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(g_currentFrame.dPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    udpSegment[l_emptyPointer++] = 0x00; udpSegment[l_emptyPointer++] = 0x00;//length, this is a placeholder for later in the function
    udpSegment[l_emptyPointer++] = 0x00; udpSegment[l_emptyPointer++] = 0x00;//checksum, this is a placeholder for later in the function
    insert_var_into(g_currentFrame.payload, udpSegment, l_emptyPointer, strlen(g_currentFrame.payload));
    
    if(dns != 0)
    {
	char *dnsSegment;
	    
	dnsLen = 4 + 28/dns;
	uint16_t dnsSegmentLen;
	dnsSegmentLen = 4 + 28/dns + strlen(g_currentFrame.payload);
	dnsSegment = (char *)malloc(sizeof(char) * dnsSegmentLen); //reserves (8 + length of payload) bytes on the heap
	dns_req_construct(dnsSegment, dns);
	    
	insert_var_into(dnsSegment, udpSegment, l_emptyPointer, dnsSegmentLen);
	free(dnsSegment);
    }
    
    udpSegment[4] = (strlen(g_currentFrame.payload) + dnsLen + 8) >> 24;
    udpSegment[5] = (strlen(g_currentFrame.payload) + dnsLen + 8) & 0x000000FF;
    uint16_t checksum = calc_checksum(udpSegment, udpSegmentLen);
    udpSegment[6] = checksum & 0x00FF;
    udpSegment[7] = checksum >> 8;
    return;
}

//slaps an IP header into the array
void insert_ip_header(char packet[], char transportSegment[], uint16_t transportSegLen, uint16_t packetLen, int packetType)
{
    char ipHeader[20];
    uint16_t l_emptyPointer = 0;
    packet[l_emptyPointer++] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    packet[l_emptyPointer++] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    packet[l_emptyPointer++] = packetLen >> 8; //takes upper 8 bits
    packet[l_emptyPointer++] = packetLen & 0x00FF; //takes lower 8 bits
    packet[l_emptyPointer++] = 0x1b; packet[l_emptyPointer++] = 0xd1; //idenfitication???????????
    packet[l_emptyPointer++] = 0x00; packet[l_emptyPointer++] = 0x00; //flags and fragment offset
    packet[l_emptyPointer++] = 0x80; //ttl of 128
    packet[l_emptyPointer++] = packetType; //what type of networking proto?
    packet[l_emptyPointer++] = 0x00; packet[l_emptyPointer++] = 0x00; //checksum
    insert_var_into(g_currentFrame.source, packet, l_emptyPointer, 4); l_emptyPointer += 4; //not being incrimented by insert_var_into :(
    insert_var_into(g_currentFrame.target, packet, l_emptyPointer, 4); l_emptyPointer += 4;
    insert_var_into(packet, ipHeader, 0, 20); //make header by itself for checksum
    insert_var_into(transportSegment, packet, l_emptyPointer, transportSegLen);
    uint16_t checkSum = calc_checksum(ipHeader, 20); //calc checksum
    packet[10] = checkSum & 0x00FF; //checksum is little endian so insert this way to make big endian
    packet[11] = checkSum >> 8;
    return;
}

//constructs an ethernet header {dMac,sMac,IPv4} -> array of 14 bytes
void insert_ether_header(char etherFrame[], char networkPacket[], uint16_t netPacketLen, uint16_t networkID)
{
    uint16_t l_emptyPointer = 0;
    insert_var_into(g_currentFrame.dMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    insert_var_into(g_currentFrame.sMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    etherFrame[l_emptyPointer++] = 0x08; etherFrame[l_emptyPointer++] = networkID; //etherversion? ¿IPv4? can't seem to condense it into one line
    insert_var_into(networkPacket, etherFrame, l_emptyPointer, netPacketLen);
    return;
}

void arp_req_construct(char arpSegment[])
{
    uint16_t l_emptyPointer = 0;
    char placeholderArr[6] = {0,0,0,0,0,0};
    
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Hardware type
    arpSegment[l_emptyPointer++] = 0x08; arpSegment[l_emptyPointer++] = 0x00;//IPv4
    arpSegment[l_emptyPointer++] = 0x06;//Hardware size
    arpSegment[l_emptyPointer++] = 0x04;//packetType size
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Request
    insert_var_into(g_currentFrame.sMac, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6;
    insert_var_into(g_currentFrame.source, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
    insert_var_into(placeholderArr, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6; //For a request the destination mac address isn't know so it's zeros instead
    insert_var_into(g_currentFrame.target, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
    return;
}

void arp_res_construct(char arpSegment[])
{
    uint16_t l_emptyPointer = 0;
    
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Hardware type
    arpSegment[l_emptyPointer++] = 0x08; arpSegment[l_emptyPointer++] = 0x00;//IPv4
    arpSegment[l_emptyPointer++] = 0x06;//Hardware size
    arpSegment[l_emptyPointer++] = 0x04;//protocol size
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x02;//Reply
    insert_var_into(g_currentFrame.dMac, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6;
    insert_var_into(g_currentFrame.target, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
    insert_var_into(g_currentFrame.sMac, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6; //For a request the destination mac address isn't know so it's zeros instead
    insert_var_into(g_currentFrame.source, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
    return;
}

//construct all of the arrays into one frame array - needs more work
uint16_t construct_packet(char bigArr[2048], char packetType[2])
{
    uint16_t segLen;
    char *segment;
    
    uint16_t packetLen;
    char *packet;
    
    uint16_t networkID = 0;
    
    switch(packetType[0])
    {
	case 'i':
	    networkID = 0;
    	segLen = 8 + strlen(g_currentFrame.payload);
    	segment = (char *)calloc(segLen, 1); //reserves (8 + length of payload) bytes on the heap
        switch (packetType[1])
        {
            case 'r':
                icmp_construct(segment, segLen, 0);
            break;
            case 'a':
                g_currentFrame.seqNum[1]++;
                icmp_construct(segment, segLen, 8);
            break;
            default:
                puts("malformed input for icmp_construct");
                exit(1);
            break;
        }
    	packetLen = 20 + segLen;
        packet = (char *)calloc(packetLen, 1); //reserves 20 + segLen bytes onthe heap
        insert_ip_header(packet, segment, segLen, packetLen, 1); //builds on top of the icmpseg
    	
    break;
	case 'u':
	networkID = 0;
	
    	segLen = 8 + strlen(g_currentFrame.payload);
    	segment = (char *)calloc(segLen, 1); //reserves (8 + length of payload) bytes on the heap
    	insert_udp_header(segment, segLen, 0);
    	
    	packetLen = 20 + segLen;
        packet = (char *)calloc(packetLen, 1); //reserves 20 + segLen bytes onthe heap
        insert_ip_header(packet, segment, segLen, packetLen, 17); //builds on top of the icmpseg
    	
    break;
	case 'a':
	networkID = 6;
	
    	segment = (char *)calloc(1, 1);
	
    	packetLen = 28;
    	packet = (char *)calloc(segLen, 1); //reserves (8 + length of payload) bytes on the heap
    	arp_req_construct(segment);
    	
    break;
	networkID = 0;
	
    	segLen = 40 + strlen(g_currentFrame.payload);
    	segment = (char *)calloc(segLen, 1); //reserves (8 + length of payload) bytes on the heap
    	insert_udp_header(segment, segLen, 1);
    	
    	packetLen = 20 + segLen;
        packet = (char *)calloc(packetLen, 1); //reserves 20 + segLen bytes onthe heap
        insert_ip_header(packet, segment, segLen, packetLen, 17); //builds on top of the icmpseg
    	
    break;
    default :
        printf("Malformed passed data, proto param incorrect: %c%c\n", packetType[0], packetType[1]); //if not recognised then error out badly
        exit(1);
    }
    
    char *etherFrame;
    uint16_t etherFrameLen = 14 + packetLen;
    etherFrame = (char *)calloc(etherFrameLen, 1); //reserves 14 bytes on the heap
    insert_ether_header(etherFrame, packet, packetLen, networkID); //builds on top of the packet
    
    char *pcap; //header + frame in an array
    uint16_t pcapLen = 16 + etherFrameLen;
    pcap = (char *)calloc(pcapLen, 1); //reserves 40 + etherFrameLen bytes on the heap
    header_construct(pcap, etherFrame, etherFrameLen); //builds on top of the packet
    
    insert_var_into(pcap, bigArr, 0, pcapLen); //insert each of the parts of the frame into the bigArr

    free(segment); //free up the reserved space on the heap
    free(packet);
    free(etherFrame);
    free(pcap);

    return pcapLen;
}

void assemble_packet(char packetType[2], FILE *fpWrite)
{
    char bigArr[2048];
    uint16_t pcapLen = construct_packet(bigArr, packetType);

    char *pcapOut;
    pcapOut = (char *)calloc(pcapLen, 1);
    insert_var_into(bigArr, pcapOut, 0, pcapLen);

    //read_pcap_out(pcapOut, bigArrLen);
    fwrite(pcapOut, 1, pcapLen, fpWrite);
    
    free(pcapOut);
}

void copy_data_into(char dataStream[], char arrOut[], uint16_t* linePointer)
{
    uint16_t x = 0;
    while (dataStream[(*linePointer)] != 0x0d)
    {
        arrOut[x++] = dataStream[(*linePointer)++];
    }
    (*linePointer) += 2;
    return; //return to one after the CRLF (Data.txt appears to be CRLF)
}

int read_data(char sMac[], char dMac[], char target[], char source[], char sPort[], char dPort[], char payload[], char packetType[], char identification[], char seqNum[], char dataStream[], uint16_t* linePointer)
{
    char proto[2];
    if (dataStream[(*linePointer)] == '\0')
    {
        return 1;
    }
    copy_data_into(dataStream, proto, linePointer);
    switch (proto[0]) //checking which proto to use
    {
        case 'i':
            packetType[0] = 'i';
            switch (proto[1]) //checking whether to do request or answer
            {
                case 'r':
                    packetType[1] = 'r';//request
                break;
                case 'a':
                    packetType[1] = 'a';//answer
                break;
                default://print error if neither and close file and exit badly
                    printf("Malformed passed data, proto param incorrect: %c%c\n", proto[0], proto[1]);
                    exit(1);
            }
            break;
        case 'u':
            packetType[0] = 'u';
            break;
        case 'a':
            packetType[0] = 'a';
            break;
        case '\0':
            return 1;
        default:
            printf("Malformed passed data, proto param incorrect: %c%c\n", proto[0], proto[1]);
            exit(1);
    }
    copy_data_into(dataStream, sMac, linePointer);
    copy_data_into(dataStream, dMac, linePointer);
    copy_data_into(dataStream, target, linePointer);
    copy_data_into(dataStream, source, linePointer);
    copy_data_into(dataStream, sPort, linePointer);
    copy_data_into(dataStream, dPort, linePointer);
    copy_data_into(dataStream, payload, linePointer);
    copy_data_into(dataStream, identification, linePointer);
    copy_data_into(dataStream, seqNum, linePointer);
	return 0;
}


void assemble_all_packets(FILE *fpWrite)
{
	char sMac[17] = "00:00:00:00:00:00";
    char dMac[17] = "00:00:00:00:00:00";
    char target[11] = "00.00.00.00";
    char source[11] = "00.00.00.00";
    char sPort[5] = "00.00";
    char dPort[5] = "00.00";
    char payload[1024] = "default";
    char packetType[2] = {'0','0'};
    char identification[5] = {"00.00"};
    char seqNum[5] = {"00.00"};
    uint16_t linePointer = 0;
	

    char *dataStream;
    FILE *fpRead;
    fpRead = fopen("Data.txt", "rb");
    if (fpRead == NULL)
    {
        puts("Data.txt doesnt exist");
        exit(1);
    }
    fseek(fpRead, 0L, SEEK_END);
    uint16_t fileLen = ftell(fpRead) + 1; //include 0x0a eof
    rewind(fpRead); //set file read linePointer to 0
    dataStream = (char *)calloc(fileLen, 1);

    fread(dataStream, sizeof(char), fileLen, fpRead);
    fclose(fpRead);
    //call (read_data, data_parse, assemble_packet) repeatedly for each packet found
	while (read_data(sMac, dMac, target, source, sPort, dPort, payload, packetType, identification, seqNum, dataStream, &linePointer) == 0) //if read_data returns 1, loop ends
	{
        data_parse(sMac, dMac, target, source, sPort, dPort, payload, identification, seqNum);

        assemble_packet(packetType, fpWrite);
    }
    free(dataStream);
    return;
}


int main()
{
    time_t t;
    srand((unsigned) time(&t));
    FILE *fpWrite;
    fpWrite = fopen("generated-packets.pcapng","wb");
    pcap_header_construct(fpWrite);

    assemble_all_packets(fpWrite);
    
    fclose(fpWrite);

    return 0;
}
