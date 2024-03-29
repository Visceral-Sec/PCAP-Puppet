#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <arpa/inet.h> //for checksums stuff
#include <stdlib.h>
#include <time.h>

//g_currentFrame holds the data for each packet. Every time a packet is read the data of g_currentFrame is replaced
//Not all of the properties in packetStruct are used in each file
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

//For testing mainly
void read_pcap_out(char pcapOut[], uint16_t pcapLen)
{
    for (uint16_t x = 0; x < pcapLen; x++)
    {
        printf("%c", pcapOut[x]);
    }
    return;
}

// The below function is from http://www.microhowto.info/howto/calculate_an_internet_protocol_checksum_in_c.html (author: Dr Graham D Shaw; accessed: 18/05/2021 - this needs to be cited properly) to create a C function to calc an rfc 1071 checksum
// It has been reformatted and altered to keep with the style of the other code (and so that it works in our context)

uint16_t calc_checksum(void* vdata, uint16_t length) //uint16_t is a 16-bit unsigned uint16_t
{
    char* payload = (char*)vdata; //Cast the payload pointer to one that can be indexed
    uint32_t acc = 0xffff; // Initialise the accumulator
    for (uint16_t i = 0; (i + 1) < length; i += 2) // Handle complete 16-bit blocks
    {
        uint16_t word; // A word being 16-bits
        memcpy(&word, payload + i, 2);
        acc += ntohs(word);
        if (acc > 0xffff)
        {
            acc -= 0xffff;
        }
    }
    if (length&1) // Handle any partial block at the end of the payload
    {
        uint16_t word = 0;
        memcpy(&word, payload + length - 1, 1);
        acc += ntohs(word);
        if (acc > 0xffff)
        {
            acc -= 0xffff;
        }
    }
    return htons(~acc); // Return the checksum in network byte order
}

//Takes array and inserts it into the desired position in a chosen array
void insert_var_into(char arrIn[], char arrOut[], uint16_t l_emptyPointer, uint16_t bytesToWrite)
{
    for (uint16_t x = 0; x < bytesToWrite; x++)
    {
        arrOut[l_emptyPointer++] = arrIn[x];
    }
    return;
}

//condense_char takes an array, takes two characters to produce a hexadecimal number, skips the third character then loops
//It stores each number in a array that it returns
uint16_t * condense_char(char currentParam[], uint16_t paramSize)//Turns a two digit string into a number
{
    uint16_t l_emptyPointer = 0;
    static uint16_t returnParam[10];
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

//data_parse takes the data retrived by read_data from Data.txt, which is in a format legible to humans, and writes it to g_currentFrame
//In g_currentFrame an address is stored in a string such that the ascii of each character represents a point of the address
//For example the IP address 97.98.99.100 would be stored in g_currentFrame.source as {97, 98, 99, 100} or as the string "abcd"
void data_parse(char sMac[17], char dMac[17], char target[11], char source[11], char sPort[5], char dPort[5], char payload[], char identification[], char seqNum[])
{   
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

//pcap_header_construct is run once at the start of the program so that it is only at the top of the file
//The data in pcapHeader is constant and consistent at the beginning of each pcap file
void pcap_header_construct(FILE *fpWrite)
{
	int pcapHeaderLen = 24;
    	char pcapHeader[24] = {0xD4, 0xC3, 0xB2, 0xA1, 0x02, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00};
	
    	fwrite(pcapHeader, 1, pcapHeaderLen, fpWrite);
    	return;
}

//It was easier to write a power function than find a library
long power(uint16_t num, uint16_t pow)
{
	long result = 1;
	for(uint16_t i = 0; i < pow; i++)
	{
		result *= num;
	}
	
	return(result);
}

//Adds epoch on to pcap array in hex and little endian
void epoch(char pcap[], uint16_t l_emptyPointer)
{
    long seconds;
    seconds = time(NULL);
    
    long divisor = power(16, 9);
    char hex[5];
    uint16_t temp;
    
    for(int i = 9; i >= 0; i--)//i needs to be an int for some reason
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

//Writes some metadata before the start of each packet 
void header_construct(char pcap[], char etherFrame[], uint16_t etherFrameLen)
{
    uint16_t l_emptyPointer = 0;
	
    epoch(pcap, l_emptyPointer); l_emptyPointer += 4;
    pcap[l_emptyPointer++] = 0x81; pcap[l_emptyPointer++] = 0x08; pcap[l_emptyPointer++] = 0x03; pcap[l_emptyPointer++] = 0x00;//Milliseconds since last second, is currently just static because it doesn't really matter
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//Length of packet excluding this header
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//The same thing again for some reason it wants it twice
    insert_var_into(etherFrame, pcap, 16, etherFrameLen);
    return;
}

//Writes a dns segment that can be a standard request or response
//If type is one, it writes a standard request. If type is two a standard response
void dns_req_construct(char dnsSegment[], int type)
{
    uint16_t l_emptyPointer = 0;
    insert_var_into(g_currentFrame.identification, dnsSegment, l_emptyPointer, 2); l_emptyPointer += 2;//Identification remains static throughout interaction
    dnsSegment[l_emptyPointer++] = 0x01; dnsSegment[l_emptyPointer++] = 0x00;//Flags for standard request
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //How many questions
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; //How many answers
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; 
    dnsSegment[l_emptyPointer++] = strlen(g_currentFrame.payload);//How long the query is
    insert_var_into(g_currentFrame.payload, dnsSegment, l_emptyPointer, strlen(g_currentFrame.payload)); l_emptyPointer += strlen(g_currentFrame.payload); dnsSegment[l_emptyPointer++] = 0x00;//The query
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //Host
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //Class
    
    if(type == 2)
    {
    	dnsSegment[2] = 0x85; dnsSegment[3] = 0x80;//Overwriting the flags for a standard response
    	dnsSegment[7] = 0x01;//Overwriting the number of answers
    	
    	dnsSegment[l_emptyPointer++] = 0xc0; dnsSegment[l_emptyPointer++] = 0x0c; //Name?
	dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //Host
	dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //Class
	dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; 
	dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x04; //IP length
	insert_var_into(g_currentFrame.target, dnsSegment, l_emptyPointer, 4);//Queried machine's IP address
    }
}

//Writes a icmp segment that can be a request or response
//If type is zero, it writes a standard request. If type is eight, it writes a standard response.
void icmp_construct(char icmpReqSeg[], uint16_t segLen, char type)
{
    uint16_t l_emptyPointer = 0;
    icmpReqSeg[l_emptyPointer++] = type;//icmp ping request or response
    icmpReqSeg[l_emptyPointer++] = 0x00;//Code is 0
    icmpReqSeg[l_emptyPointer++] = 0x00; icmpReqSeg[l_emptyPointer++] = 0x00;//Checksum, this is a placeholder for later in the function
    insert_var_into(g_currentFrame.identification, icmpReqSeg, l_emptyPointer, 2); l_emptyPointer +=2; //Identifier
    insert_var_into(g_currentFrame.seqNum, icmpReqSeg, l_emptyPointer, 2); l_emptyPointer +=2; //Sequence number
    insert_var_into(g_currentFrame.payload, icmpReqSeg, l_emptyPointer, strlen(g_currentFrame.payload));
	
    uint16_t checksum = calc_checksum(icmpReqSeg, segLen);//Once all the data is written, the checksum can be calculated
    icmpReqSeg[2] = checksum & 0x00FF;//Writes the checksum in little endian
    icmpReqSeg[3] = checksum >> 8;
    return;
}

//Produces a udp header for standard udp or dns traffic
//If dns is zero, it writes standard udp traffic. If dns is one, it writes a standard dns request. If dns is two a standard dns response
void insert_udp_header(char udpSegment[], uint16_t udpSegmentLen, uint16_t dns)
{
    uint16_t dnsLen = 0;
    uint16_t l_emptyPointer = 0;
    insert_var_into(g_currentFrame.sPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(g_currentFrame.dPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;//Source and destination ports
    udpSegment[l_emptyPointer++] = 0x00; udpSegment[l_emptyPointer++] = 0x00;//Length, this is a placeholder for later in the function
    udpSegment[l_emptyPointer++] = 0x00; udpSegment[l_emptyPointer++] = 0x00;//Checksum, this is a placeholder for later in the function
    insert_var_into(g_currentFrame.payload, udpSegment, l_emptyPointer, strlen(g_currentFrame.payload));//Standard udp traffic
	
    if(dns != 0)
    {
	char *dnsSegment;
	uint16_t dnsSegmentLen;
	    
	dnsLen = 2 + 16 * dns;//dns length changes between request and response
	dnsSegmentLen = dnsLen + strlen(g_currentFrame.payload);
	dnsSegment = (char *)malloc(sizeof(char) * dnsSegmentLen);
	dns_req_construct(dnsSegment, dns);//Creates a dns segment 
	    
	insert_var_into(dnsSegment, udpSegment, l_emptyPointer, dnsSegmentLen);//Adds the dns segment to the udp segment overwriting the udp payload written line 263
	free(dnsSegment);
    }
    
    udpSegment[4] = (strlen(g_currentFrame.payload) + dnsLen + 8) >> 24;
    udpSegment[5] = (strlen(g_currentFrame.payload) + dnsLen + 8) & 0x000000FF;//Writes the length of the udp segment in little endian
    uint16_t checksum = calc_checksum(udpSegment, udpSegmentLen);//Once all the data is written, the checksum can be calculated
    udpSegment[6] = checksum & 0x00FF;//Writes the checksum in little endian
    udpSegment[7] = checksum >> 8;
    return;
}

//The following code until line 400 successfully enables the production of a tcp handshake, however, is not supported by the rest of the program due to lack of time
void initialiseSeqAck(char seqNum[4], char ackNum[4])
{
    uint32_t randSeqNum1 = rand();
    uint32_t randSeqNum2 = rand();
    uint32_t randAckNum1 = rand();
    uint32_t randAckNum2 = rand();
    
    seqNum[0] = randSeqNum1 >> 24;
    seqNum[1] = randSeqNum1 & 0x000000FF;
    seqNum[2] = randSeqNum2 >> 24;
    seqNum[3] = randSeqNum2 & 0x000000FF;
    
    ackNum[0] = randAckNum1 >> 24;
    ackNum[1] = randAckNum1 & 0x000000FF;
    ackNum[2] = randAckNum2 >> 24;
    ackNum[3] = randAckNum2 & 0x000000FF;
}

void tcp_syn_construct(char tcpSegment[], char seqNum[4], char ackNum[4])
{
    uint16_t l_emptyPointer = 0;
    initialiseSeqAck(seqNum, ackNum);
    
    insert_var_into(g_currentFrame.sPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(g_currentFrame.dPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(seqNum, tcpSegment, l_emptyPointer, 4); l_emptyPointer += 4; //seq num
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;
    tcpSegment[l_emptyPointer++] = 0xa0;
    tcpSegment[l_emptyPointer++] = 0x02; //tcp flags
    tcpSegment[l_emptyPointer++] = 0xfa; tcpSegment[l_emptyPointer++] = 0xf0;//window size?
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//checksum
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//Urgent pointer?
    
    tcpSegment[l_emptyPointer++] = 0x02; tcpSegment[l_emptyPointer++] = 0x04;//options
    tcpSegment[l_emptyPointer++] = 0x05; tcpSegment[l_emptyPointer++] = 0xb4;
    tcpSegment[l_emptyPointer++] = 0x04; tcpSegment[l_emptyPointer++] = 0x02;
    tcpSegment[l_emptyPointer++] = 0x08; tcpSegment[l_emptyPointer++] = 0x0a;
    tcpSegment[l_emptyPointer++] = 0xfa; tcpSegment[l_emptyPointer++] = 0xe0;
    tcpSegment[l_emptyPointer++] = 0x62; tcpSegment[l_emptyPointer++] = 0x49;
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;
    tcpSegment[l_emptyPointer++] = 0x01; tcpSegment[l_emptyPointer++] = 0x03;
    tcpSegment[l_emptyPointer++] = 0x03; tcpSegment[l_emptyPointer++] = 0x04;
    return;
}

void tcp_synack_construct(char tcpSegment[], char seqNum[4], char ackNum[4])
{
    uint16_t l_emptyPointer = 0;
    seqNum[3]++;
    
    insert_var_into(g_currentFrame.dPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(g_currentFrame.sPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(ackNum, tcpSegment, l_emptyPointer, 4); l_emptyPointer += 4; //ack num
    insert_var_into(seqNum, tcpSegment, l_emptyPointer, 4); l_emptyPointer += 4; //seq num
    tcpSegment[l_emptyPointer++] = 0xa0;
    tcpSegment[l_emptyPointer++] = 0x12; //tcp flags
    tcpSegment[l_emptyPointer++] = 0xfa; tcpSegment[l_emptyPointer++] = 0xf0;//window size?
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//checksum
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//Urgent pointer?
    
    tcpSegment[l_emptyPointer++] = 0x02; tcpSegment[l_emptyPointer++] = 0x04;//options
    tcpSegment[l_emptyPointer++] = 0x05; tcpSegment[l_emptyPointer++] = 0xb4;
    tcpSegment[l_emptyPointer++] = 0x04; tcpSegment[l_emptyPointer++] = 0x02;
    tcpSegment[l_emptyPointer++] = 0x08; tcpSegment[l_emptyPointer++] = 0x0a;
    tcpSegment[l_emptyPointer++] = 0xfa; tcpSegment[l_emptyPointer++] = 0xe0;
    tcpSegment[l_emptyPointer++] = 0x62; tcpSegment[l_emptyPointer++] = 0x49;
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;
    tcpSegment[l_emptyPointer++] = 0x01; tcpSegment[l_emptyPointer++] = 0x03;
    tcpSegment[l_emptyPointer++] = 0x03; tcpSegment[l_emptyPointer++] = 0x04;
    return;
}

void tcp_ack_construct(char tcpSegment[], char seqNum[4], char ackNum[4])
{
    uint16_t l_emptyPointer = 0;
    ackNum[3]++;
    
    insert_var_into(g_currentFrame.sPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(g_currentFrame.dPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insert_var_into(seqNum, tcpSegment, l_emptyPointer, 4); l_emptyPointer += 4; //seq num
    insert_var_into(ackNum, tcpSegment, l_emptyPointer, 4); l_emptyPointer += 4; //ack num
    tcpSegment[l_emptyPointer++] = 0x80;
    tcpSegment[l_emptyPointer++] = 0x10; //tcp flags
    tcpSegment[l_emptyPointer++] = 0xfa; tcpSegment[l_emptyPointer++] = 0xf0;//window size?
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//checksum
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//Urgent pointer?
    
    tcpSegment[l_emptyPointer++] = 0x01; tcpSegment[l_emptyPointer++] = 0x01;//options
    tcpSegment[l_emptyPointer++] = 0x08; tcpSegment[l_emptyPointer++] = 0x0a;
    tcpSegment[l_emptyPointer++] = 0xfa; tcpSegment[l_emptyPointer++] = 0xe0;
    tcpSegment[l_emptyPointer++] = 0x62; tcpSegment[l_emptyPointer++] = 0x49;
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;
}

void tcp_construct(char tcpSegment[], uint16_t type)
{
    static char seqNum[4];
    static char ackNum[4];
    
    switch(type)
    {
    case 1: tcp_syn_construct(tcpSegment, seqNum, ackNum); break;
    
    case 2: tcp_synack_construct(tcpSegment, seqNum, ackNum); break;
    
    case 3: tcp_ack_construct(tcpSegment, seqNum, ackNum); break;
    }
}

//Constructs an arp segment for an arp request or response
//If type is 1 it produces a request, if type is 2 a response
void arp_construct(char arpSegment[], char type)
{
    uint16_t l_emptyPointer = 0;
    char placeholderArr[6] = {0,0,0,0,0,0};
    
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Hardware type
    arpSegment[l_emptyPointer++] = 0x08; arpSegment[l_emptyPointer++] = 0x00;//IPv4
    arpSegment[l_emptyPointer++] = 0x06;//Hardware size
    arpSegment[l_emptyPointer++] = 0x04;//PacketType size
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = type;//Request or response
    insert_var_into(g_currentFrame.sMac, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6;
    insert_var_into(g_currentFrame.source, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
	
	/*This code was written after testing and would have replaced the line under it. A response doesn't have a placeholder instead of a dMac aaddress 
    if(type == 1)
    {
    	insert_var_into(placeholderArr, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6;
    }
    else
    {
    	insert_var_into(g_currentFrame.dMac, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6;
    }
	*/
	
    insert_var_into(placeholderArr, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6; //For a request the destination mac address isn't know so it's zeros instead
    insert_var_into(g_currentFrame.target, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
    return;
}


//Produces an IP header for a transport segment(udp and icmp)
void insert_ip_header(char packet[], char transportSegment[], uint16_t transportSegLen, uint16_t packetLen, int packetType)
{
    char ipHeader[20];
    uint16_t l_emptyPointer = 0;
    packet[l_emptyPointer++] = 0x45; //0b0100 version 4 IP + 0101 IP header length
    packet[l_emptyPointer++] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    packet[l_emptyPointer++] = packetLen >> 8; 
    packet[l_emptyPointer++] = packetLen & 0x00FF; //Writes the packet length in little endian
    packet[l_emptyPointer++] = 0x1b; packet[l_emptyPointer++] = 0xd1; //Idenfitication
    packet[l_emptyPointer++] = 0x00; packet[l_emptyPointer++] = 0x00; //Flags and fragment offset
    packet[l_emptyPointer++] = 0x80; //Time to live of 128
    packet[l_emptyPointer++] = packetType; //The type of transport segment
    packet[l_emptyPointer++] = 0x00; packet[l_emptyPointer++] = 0x00; //Checksum placeholder
    insert_var_into(g_currentFrame.source, packet, l_emptyPointer, 4); l_emptyPointer += 4; 
    insert_var_into(g_currentFrame.target, packet, l_emptyPointer, 4); l_emptyPointer += 4;//IP addresses
    insert_var_into(packet, ipHeader, 0, 20); //Make header by itself for checksum
    insert_var_into(transportSegment, packet, l_emptyPointer, transportSegLen);//Adds the IP header to the transport segment
    uint16_t checkSum = calc_checksum(ipHeader, 20); //Calculates the checksum
    packet[10] = checkSum & 0x00FF; //Checksum is little endian so insert this way to make it big endian
    packet[11] = checkSum >> 8;
    return;
}

//Constructs an ethernet header {dMac,sMac,IPv4} -> array of 14 bytes
void insert_ether_header(char etherFrame[], char networkPacket[], uint16_t netPacketLen, uint16_t networkID)
{
    uint16_t l_emptyPointer = 0;
    insert_var_into(g_currentFrame.dMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    insert_var_into(g_currentFrame.sMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;//MAC addresses
    etherFrame[l_emptyPointer++] = 0x08; etherFrame[l_emptyPointer++] = networkID; //etherversion and network type
    insert_var_into(networkPacket, etherFrame, l_emptyPointer, netPacketLen);//Adds the ethernet header to the network packet
    return;
}


//Takes all of the arrays from different layers and constructs one frame array for the pcap
uint16_t construct_packet(char bigArr[2048], char packetType[2])
{
    uint16_t segLen;
    char *segment;//For the transport layer
	
    uint16_t packetLen;//For the network layer
    char *packet;
    
    uint16_t networkID = 0;//Used for the ethernet frame construction
    
    switch(packetType[0])//Determines which protocol function to run and with what parameters
    {
	case 'i'://For icmp
	networkID = 0;
    	segLen = 8 + strlen(g_currentFrame.payload);
    	segment = (char *)calloc(segLen, 1); //Reserves (8 + length of payload) bytes on the heap
        switch (packetType[1])//Decides if it's a request or a response
        {
            case 'r':
                icmp_construct(segment, segLen, 0);//Request
            break;
            case 'a':
                g_currentFrame.seqNum[1]++;
                icmp_construct(segment, segLen, 8);//Response
            break;
            default:
                puts("malformed input for icmp_construct");
                exit(1);
            break;
        }//Creates a icmp segment
		    
    	packetLen = 20 + segLen;
        packet = (char *)calloc(packetLen, 1); //Reserves 20 + packetLen bytes on the heap
        insert_ip_header(packet, segment, segLen, packetLen, 1); //Takes the icmp segment and uses it to make an IP packet
    	
    break;
	case 'u'://For udp
	networkID = 0;
    	
    	segLen = 8 + strlen(g_currentFrame.payload);
    	segment = (char *)calloc(segLen, 1); 
    	insert_udp_header(segment, segLen, 0);//Makes a udp segment without doing anything with dns
    	
    	packetLen = 20 + segLen;
        packet = (char *)calloc(packetLen, 1); 
        insert_ip_header(packet, segment, segLen, packetLen, 17); //Takes the udp segment and uses it to make an IP packet
		    
    break;
	case 'a'://For arp
	networkID = 6;
	//arp is a network layer protocol and so doesn't use segment, however, it still needs a value for when it's freed later
	segment = calloc(1,1);
		    
    	packetLen = 28;
    	packet = (char *)calloc(packetLen, 1);
        switch (packetType[1])//Decides if it's a request or a response
        {
            case 'r':
                arp_construct(packet, 1);
                break;
            case 'a':
                g_currentFrame.seqNum[1]++;
                arp_construct(packet, 2);
                break;
            default:
                printf("malformed input for arp_construct: %c,%c", packetType[0], packetType[1]);
                exit(1);
            break;
    	}//Creates an arp packet
		    
    break;
    	case 'd'://For dns
	networkID = 0;
        
        switch (packetType[1])//Decides if it's a request or a response
        {
            case 'r':
	    	segLen = 26 + strlen(g_currentFrame.payload);
	    	segment = (char *)calloc(segLen, 1); //The segment is defined here since the length varies between request and response
    		insert_udp_header(segment, segLen, 1);
                break;
            case 'a':
	    	segLen = 42 + strlen(g_currentFrame.payload);
	    	segment = (char *)calloc(segLen, 1); 
    		insert_udp_header(segment, segLen, 2);
                break;
            default:
	    	segment = (char *)calloc(1, 1); 
                printf("malformed input for arp_construct: %c,%c", packetType[0], packetType[1]);
                exit(1);
            break;
    	}//Creates a dns segment with a udp header
    	
    	packetLen = 20 + segLen;
        packet = (char *)calloc(packetLen, 1); 
        insert_ip_header(packet, segment, segLen, packetLen, 17); 
    	
    break;
    default :
        printf("Malformed passed data, proto param incorrect: %c%c\n", packetType[0], packetType[1]); //if not recognised then error out badly
        exit(1);
    }
    
    char *etherFrame;
    uint16_t etherFrameLen = 14 + packetLen;
    etherFrame = (char *)calloc(etherFrameLen, 1);
    insert_ether_header(etherFrame, packet, packetLen, networkID);//Takes the network packet and uses it to make an ethernet frame
    
    char *pcap; //header + frame in an array
    uint16_t pcapLen = 16 + etherFrameLen;
    pcap = (char *)calloc(pcapLen, 1); 
    header_construct(pcap, etherFrame, etherFrameLen); //Takes the ethernet frame and uses it to make the pcap packet
    
    insert_var_into(pcap, bigArr, 0, pcapLen); //insert each of the parts of the frame into the bigArr

    free(segment);
    free(packet);//free up the reserved space on the heap
    free(etherFrame);
    free(pcap);

    return pcapLen;
}

//Creates a pcap packet and writes it to the pcap file
void assemble_packet(char packetType[2], FILE *fpWrite)
{
    char bigArr[2048];
    uint16_t pcapLen = construct_packet(bigArr, packetType);

    char *pcapOut;
    pcapOut = (char *)calloc(pcapLen, 1);
    insert_var_into(bigArr, pcapOut, 0, pcapLen);
	
    fwrite(pcapOut, 1, pcapLen, fpWrite);
    
    free(pcapOut);
}

//Used to read lines of data from the Data.txt file
void copy_data_into(char dataStream[], char arrOut[], uint16_t* linePointer) //File array in, the array its printing out to and the pointer to the linePointer variable
{
    uint16_t x = 0;
    while (dataStream[(*linePointer)] != '\n')//(*linePointer) accesses the value of linePointer and allows it to be changed outside of scope
    {
        arrOut[x++] = dataStream[(*linePointer)++];
    }
    (*linePointer) += 1;
    return; //Return to one after the line feed at the end of the packet
}

//Takes data from the Data.txt and puts it in arrays
int read_data(char sMac[], char dMac[], char target[], char source[], char sPort[], char dPort[], char payload[], char packetType[], char identification[], char seqNum[], char dataStream[], uint16_t* linePointer)
{
    char proto[2];
	
    if (dataStream[(*linePointer)] == '\0')//Reached the end of datastream
    {
        return 1;
    }
    copy_data_into(dataStream, proto, linePointer);
    switch (proto[0]) //Checking which protocol to the current packet is
    {
        case 'i'://For icmp
            packetType[0] = 'i';
            switch (proto[1]) //Checking whether to do request or answer
            {
                case 'r':
                    packetType[1] = 'r';//Request
                break;
                case 'a':
                    packetType[1] = 'a';//Answer
                break;
                default://Print an error if neither and close file and exit poorly
                    printf("Malformed passed data, proto param incorrect: %c%c\n", proto[0], proto[1]);
                    exit(1);
            }
            break;
        case 'u':
            packetType[0] = 'u';//For udp
            break;
        case 'a'://For arp
            packetType[0] = 'a';
            switch (proto[1])
            {
                case 'r':
                    packetType[1] = 'r';
                break;
                case 'a':
                    packetType[1] = 'a';
                break;
                default:
                    printf("Malformed passed data, proto param incorrect: %c%c\n", proto[0], proto[1]);
                    exit(1);
            }
            break;
        case 'd'://For dns
            packetType[0] = 'd';
            switch (proto[1])
            {
                case 'r':
                    packetType[1] = 'r';
                break;
                case 'a':
                    packetType[1] = 'a';
                break;
                default:
                    printf("Malformed passed data, proto param incorrect: %c%c\n", proto[0], proto[1]);
                    exit(1);
            }
            break;
        case '\0'://End of dataStream
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

//assemble_all_packets creates and writes each packet sent from the frontend in Data.txt 
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
    if (fpRead == NULL)//If Data.txt can't be found
    {
        puts("Data.txt doesnt exist");
        exit(1);
    }
    fseek(fpRead, 0L, SEEK_END);
    uint16_t fileLen = ftell(fpRead) + 1; //Include 0x0a eof
    rewind(fpRead); //Set file read linePointer to 0
    dataStream = (char *)calloc(fileLen, 1);
    fread(dataStream, sizeof(char), fileLen, fpRead);//Stores the data from Data.txt in dataStream
    fclose(fpRead);
	
    //Until the end of dataStream, each packet is decoded, created and written
    while (read_data(sMac, dMac, target, source, sPort, dPort, payload, packetType, identification, seqNum, dataStream, &linePointer) == 0) //If read_data returns 1, loop ends
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
    fpWrite = fopen("generated-packets.pcapng","wb");//Creates the pcap file

    //Creates and writes the file header and then all packets for the file
    pcap_header_construct(fpWrite);

    assemble_all_packets(fpWrite);
    
    fclose(fpWrite);

    return 0;
}
