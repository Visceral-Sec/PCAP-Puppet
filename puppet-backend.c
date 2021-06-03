#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <arpa/inet.h> //for checksums stuff
#include <stdlib.h>
#include <time.h>

struct packet
{
    char sMac[6];
    char dMac[6];
    char source[4];
    char target[4];
    char sPort[2];
    char dPort[2];
    char payload[100];
    char lastSeq[2];
    char transactionID[2];
};
struct packet g_currentFrame;

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

uint16_t calcChecksum(void* vdata, size_t length) //uint16_t is a 16-bit unsigned uint16_t
{
    char* data = (char*)vdata; //Cast the data pointer to one that can be indexed.
    uint32_t acc = 0xffff; // Initialise the accumulator
    for (size_t i = 0; (i + 1) < length; i += 2) // Handle complete 16-bit blocks.
    {
        uint16_t word; // a word being 16-bits
        memcpy(&word, data + i, 2);
        acc += ntohs(word);
        if (acc > 0xffff)
        {
            acc -= 0xffff;
        }
    }
    if (length&1) // Handle any partial block at the end of the data.
    {
        uint16_t word = 0;
        memcpy(&word, data + length - 1, 1);
        acc += ntohs(word);
        if (acc > 0xffff)
        {
            acc -= 0xffff;
        }
    }
    return htons(~acc); // Return the checksum in network byte order.
}

//takes array and inserts it into the desired position in a chosen array
void insertVarInto(char arrIn[], char arrOut[], uint16_t l_emptyPointer, uint16_t bytesToWrite)
{
    for (uint16_t x = 0; x < bytesToWrite; x++)
    {
        arrOut[l_emptyPointer++] = arrIn[x];
    }
    return;
}

//parse data from python frontend
uint16_t * condenseChar(char currentParam[], uint16_t paramSize)//Turns a two digit string into a number
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
        returnParam[l_emptyPointer++] = digit1*16 + digit2; //incriment endPointer before assignment
    }
    
    return returnParam;
}

//converts the incoming data into the correct formats for writing
void dataParse(char sMac[17], char dMac[17], char target[11], char source[11], char sPort[5], char dPort[5], char data[])
{   
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in g_currentFrame.sMac
    for(uint16_t i = 0; i < 6; i++)
    {
    	g_currentFrame.sMac[i] = condenseChar(sMac, 17)[i];
    }
    for(uint16_t i = 0; i < 6; i++)
    {
    	g_currentFrame.dMac[i] = condenseChar(dMac, 17)[i];
    }
    for(uint16_t i = 0; i < 4; i++)
    {
    	g_currentFrame.target[i] = condenseChar(target, 11)[i];
    }
    for(uint16_t i = 0; i < 4; i++)
    {
    	g_currentFrame.source[i] = condenseChar(source, 11)[i];
    }
    for(uint16_t i = 0; i < 2; i++)
    {
    	g_currentFrame.sPort[i] = condenseChar(sPort, 5)[i];
    }
    for(uint16_t i = 0; i < 2; i++)
    {
    	g_currentFrame.dPort[i] = condenseChar(dPort, 5)[i];
    }
    
    strcpy(g_currentFrame.payload, data);
    return;
}

//is run once at the start of the program so that it is only at the top of the file
void pcapHeaderConstruct(FILE *fp)
{
	int pcapHeaderLen = 24;
    	char pcapHeader[24] = {0xD4, 0xC3, 0xB2, 0xA1, 0x02, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00};
	
    	fwrite(pcapHeader, 1, pcapHeaderLen, fp);
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
    char hex[4];
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
    
    insertVarInto(hex, pcap, l_emptyPointer, 4);
    
    return;
}

//is functional and dynamic for a single packet but needs some work for multiple
void headerConstruct(char pcap[], char etherFrame[], uint16_t etherFrameLen)
{
    //is only written at the start of a pcap
    uint16_t l_emptyPointer = 0;
	
    //is after every packet 
    epoch(pcap, l_emptyPointer); l_emptyPointer += 4;
    pcap[l_emptyPointer++] = 0x81; pcap[l_emptyPointer++] = 0x08; pcap[l_emptyPointer++] = 0x03; pcap[l_emptyPointer++] = 0x00;//milliseconds since last second, is currently just static because it doesn't really matter
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//length of packet excluding header
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//the same thing again for some reason it wants it twice
    insertVarInto(etherFrame, pcap, 16, etherFrameLen);
    return;
}

//slaps icmp segment into the frame
void icmpReqConstruct(char icmpReqSegment[], uint16_t segmentLen)
{
    uint16_t l_emptyPointer = 0;
    uint32_t seqNum = rand();
    icmpReqSegment[l_emptyPointer++] = 0x08;//icmp ping request
    icmpReqSegment[l_emptyPointer++] = 0x00;//code is 0
    icmpReqSegment[l_emptyPointer++] = 0x00; icmpReqSegment[l_emptyPointer++] = 0x00;//checksum, this is a placeholder for later in the function
    icmpReqSegment[l_emptyPointer++] = 0x00; icmpReqSegment[l_emptyPointer++] = 0x01;//identifier?
    icmpReqSegment[l_emptyPointer++] = seqNum >> 24;
    icmpReqSegment[l_emptyPointer++] = seqNum & 0x000000FF;
    insertVarInto(g_currentFrame.payload, icmpReqSegment, l_emptyPointer, strlen(g_currentFrame.payload));
    uint16_t checksum = calcChecksum(icmpReqSegment, segmentLen);
    icmpReqSegment[2] = checksum & 0x00FF;
    icmpReqSegment[3] = checksum >> 8;
    return;
}

/* we need to do handshakes
//creates a transport layer tcp header
void tcpConstruct(char tcpSegment[])
{
    uint16_t l_emptyPointer = 0;
    insertVarInto(g_currentFrame.sPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insertVarInto(g_currentFrame.dPort, tcpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insertVarInto(seqNum, tcpSegment, l_emptyPointer, 4); l_emptyPointer += 4; //seq num
    insertVarInto(AckNum, tcpSegment, l_emptyPointer, 4); l_emptyPointer += 4; //ack num
    tcpSegment[l_emptyPointer++] = flags; //tcp flags - probably easier to impliment once parsing is done
    insertVarInto(windowSize, tcpSegment, l_emptyPointer, 2);
    insertVarInto(checkSum, tcpSegment, l_emptyPointer, 2);
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//Urgent pointer?
    //then a bunch of options that are scary
    return;
}*/

void udpConstruct(char udpSegment[], uint16_t udpSegmentLen)
{
    uint16_t l_emptyPointer = 0;
    insertVarInto(g_currentFrame.sPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insertVarInto(g_currentFrame.dPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    udpSegment[l_emptyPointer++] = (strlen(g_currentFrame.payload) + 8) >> 24;
    udpSegment[l_emptyPointer++] = (strlen(g_currentFrame.payload) + 8) & 0x000000FF;
    udpSegment[l_emptyPointer++] = 0x00; udpSegment[l_emptyPointer++] = 0x00;//checksum, this is a placeholder for later in the function
    insertVarInto(g_currentFrame.payload, udpSegment, l_emptyPointer, strlen(g_currentFrame.payload));
    uint16_t checksum = calcChecksum(udpSegment, udpSegmentLen);
    udpSegment[6] = checksum & 0x00FF;
    udpSegment[7] = checksum >> 8;
    return;
}


void arpConstruct(char arpSegment[])
{
    uint16_t l_emptyPointer = 0;
    char placeholderArr[6] = {0,0,0,0,0,0};
    
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Hardware type
    arpSegment[l_emptyPointer++] = 0x08; arpSegment[l_emptyPointer++] = 0x00;//IPv4
    arpSegment[l_emptyPointer++] = 0x06;//Hardware size
    arpSegment[l_emptyPointer++] = 0x04;//protocol size
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Request
    insertVarInto(g_currentFrame.sMac, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6;
    insertVarInto(g_currentFrame.source, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
    insertVarInto(placeholderArr, arpSegment, l_emptyPointer, 6); l_emptyPointer += 6; //For a request the destination mac address isn't know so it's zeros instead
    insertVarInto(g_currentFrame.target, arpSegment, l_emptyPointer, 4); l_emptyPointer += 4;
    return;
}

/*
void dnsReqConstruct(char dnsSegment[])
{
    uint16_t l_emptyPointer = 0;
    uint16_t flags = rand() % 16;
    insertVarInto(g_currentFrame.transactionID, dnsSegment, l_emptyPointer, 2);//remains static throughout interaction
    dnsSegment[l_emptyPointer++] = flags >> 8;
    dnsSegment[l_emptyPointer++] = flags & 0x0FF; //0100 for standard query, 8580 for standard query response//is randomized for compilation's sake
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x01; //how many questions
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; //how many answers, would be 0x0001 for a response
    //number of name server resource records in authority records and number of name server resource records in authority records? is currently blank for compliation's sake
    dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00; dnsSegment[l_emptyPointer++] = 0x00;
    insertVarInto(query, dnsSegment, l_emptyPointer, strlen(query)); //adding the query section to the pcap?
}*/

//slaps an IP header into the array
void ipConstruct(char ipPacket[], char transportSegment[], uint16_t transportSegLen, uint16_t ipPacketLen, int protocol)
{
    char ipHeader[20];
    uint16_t l_emptyPointer = 0;
    ipPacket[l_emptyPointer++] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    ipPacket[l_emptyPointer++] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    ipPacket[l_emptyPointer++] = ipPacketLen >> 8; //takes upper 8 bits
    ipPacket[l_emptyPointer++] = ipPacketLen & 0x00FF; //takes lower 8 bits
    ipPacket[l_emptyPointer++] = 0x1b; ipPacket[l_emptyPointer++] = 0xd1; //idenfitication???????????
    ipPacket[l_emptyPointer++] = 0x00; ipPacket[l_emptyPointer++] = 0x00; //flags and fragment offset
    ipPacket[l_emptyPointer++] = 0x80; //ttl of 128
    ipPacket[l_emptyPointer++] = protocol;
    ipPacket[l_emptyPointer++] = 0x00; ipPacket[l_emptyPointer++] = 0x00; //checksum
    insertVarInto(g_currentFrame.source, ipPacket, l_emptyPointer, 4); l_emptyPointer += 4; //not being incrimented by insertVarInto :(
    insertVarInto(g_currentFrame.target, ipPacket, l_emptyPointer, 4); l_emptyPointer += 4;
    insertVarInto(ipPacket, ipHeader, 0, 20); //make header by itself for checksum
    insertVarInto(transportSegment, ipPacket, l_emptyPointer, transportSegLen);
    uint16_t checkSum = calcChecksum(ipHeader, 20); //calc checksum
    ipPacket[10] = checkSum & 0x00FF; //checksum is little endian so insert this way to make big endian
    ipPacket[11] = checkSum >> 8;
    return;
}

//constructs an ethernet header {dMac,sMac,IPv4} -> array of 14 bytes
void etherConstruct(char etherFrame[], char networkPacket[], uint16_t netPacketLen, uint16_t networkID)
{
    uint16_t l_emptyPointer = 0;
    insertVarInto(g_currentFrame.dMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    insertVarInto(g_currentFrame.sMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    etherFrame[l_emptyPointer++] = 0x08; etherFrame[l_emptyPointer++] = networkID; //etherversion? ¿IPv4? can't seem to condense it into one line
    insertVarInto(networkPacket, etherFrame, l_emptyPointer, netPacketLen);
    return;
}

//construct all of the arrays into one frame array - needs more work
uint16_t constructPacket(char bigArr[512], char protocol)
{
    uint16_t protocolSegmentLen;
    char *protocolSegment;
    
    uint16_t ipPacketLen;
    char *ipPacket;
    
    uint16_t segmentLen;
    char *segment;
    
    uint16_t networkID = 0;
    
    switch(protocol)
    {
	case 'i':
	
	networkID = 0;
	
    	protocolSegmentLen = 8 + strlen(g_currentFrame.payload);
    	protocolSegment = (char *)malloc(sizeof(char) * protocolSegmentLen); //reserves (8 + length of payload) bytes on the heap
    	icmpReqConstruct(protocolSegment, protocolSegmentLen);
    	
    	ipPacketLen = 20 + protocolSegmentLen;
        ipPacket = (char *)malloc(sizeof(char) * (ipPacketLen)); //reserves 20 + protocolSegmentLen bytes onthe heap
        ipConstruct(ipPacket, protocolSegment, protocolSegmentLen, ipPacketLen, 1); //builds on top of the icmpseg
        
        segmentLen = ipPacketLen;
        segment = (char *)malloc(sizeof(char) * (segmentLen)); 
        insertVarInto(ipPacket, segment, 0, segmentLen);
    	
    	break;
    
	case 'u':
	
	networkID = 0;
	
    	protocolSegmentLen = 8 + strlen(g_currentFrame.payload);
    	protocolSegment = (char *)malloc(sizeof(char) * protocolSegmentLen); //reserves (8 + length of payload) bytes on the heap
    	udpConstruct(protocolSegment, protocolSegmentLen);
    	
    	ipPacketLen = 20 + protocolSegmentLen;
        ipPacket = (char *)malloc(sizeof(char) * (ipPacketLen)); //reserves 20 + protocolSegmentLen bytes onthe heap
        ipConstruct(ipPacket, protocolSegment, protocolSegmentLen, ipPacketLen, 17); //builds on top of the icmpseg
        
        segmentLen = ipPacketLen;
        segment = (char *)malloc(sizeof(char) * (segmentLen)); 
        insertVarInto(ipPacket, segment, 0, segmentLen);
    	
    	break;
    	
	case 'a':
	
	networkID = 6;
	
        ipPacket = (char *)malloc(sizeof(char) * (1));
    	protocolSegment = (char *)malloc(sizeof(char) * 1);
	
    	segmentLen = 28;
    	segment = (char *)malloc(sizeof(char) * segmentLen); //reserves (8 + length of payload) bytes on the heap
    	arpConstruct(segment);
    	
    	break;
    	
    	/*	
    	
	case 't':
	
    	segmentLen = 6 + strlen(PingReq.payload);
    	segment = (char *)malloc(sizeof(char) * segmentLen); //reserves (8 + length of payload) bytes on the heap
    	tcpConstruct(segment);
    	
    	break;
    	
	case 'd':
	
    	segmentLen = 6 + strlen(PingReq.payload);
    	segment = (char *)malloc(sizeof(char) * segmentLen); //reserves (8 + length of payload) bytes on the heap
    	dnsConstruct(segment);
    	
    	break;
    	
    */
    default :
        puts("a valid protocol hasn't been passed");
    }
    
    
    char *etherFrame;
    uint16_t etherFrameLen = 14 + segmentLen;
    etherFrame = (char *)malloc(sizeof(char) * (etherFrameLen)); //reserves 14 bytes on the heap
    etherConstruct(etherFrame, segment, segmentLen, networkID); //builds on top of the ipPacket
    
    char *pcap; //header + frame in an array
    uint16_t pcapLen = 16 + etherFrameLen;
    pcap = (char *)malloc(sizeof(char) * (pcapLen)); //reserves 40 + etherFrameLen bytes on the heap
    headerConstruct(pcap, etherFrame, etherFrameLen); //builds on top of the ipPacket
    
    insertVarInto(pcap, bigArr, 0, pcapLen); //insert each of the parts of the frame into the bigArr

    free(protocolSegment); //free up the reserved space on the heap
    free(segment);
    free(ipPacket);
    free(etherFrame);
    free(pcap);

    return pcapLen;
}

void assemblePacket(char protocol, FILE *fp)
{
    char bigArr[1024];
    uint16_t pcapLen = constructPacket(bigArr, protocol);

    char *pcapOut;
    pcapOut = (char *)malloc(sizeof(char) * pcapLen);
    insertVarInto(bigArr, pcapOut, 0, pcapLen);

    //read_pcap_out(pcapOut, bigArrLen);
    fwrite(pcapOut, 1, pcapLen, fp);
    
    free(pcapOut);
}

void icmp8Found()
{

    return;
}

int readData(char sMac[17], char dMac[17], char target[11], char source[11], char sPort[5], char dPort[5], char data[65507], int loopCounter, char protocol[1])
{
	int len;
	int line = 0;
	char currentLine[1000]; //variable holds current line in textfile
	int fileEnd = 0;
	
	FILE *fptr; //Declaring a pointer
    	fptr = fopen("data.txt", "r"); //read
	if (fptr == NULL) { //check to see if file exists
		printf("Unable to open file");
		exit(1);
	}
	
	fscanf(fptr, "%s", currentLine);
	line = 0;
	
	while (fgets(currentLine, sizeof(currentLine), fptr) != NULL && line < 9 + 9 * loopCounter) { //reads the 7 lines under icmp8 
		
		if (line == 1 + 9 * loopCounter){
			switch(currentLine[1])
			{
				case 'i': protocol[0] = 'i'; break;
				
				case 'u': protocol[0] = 'u'; break;
				
				case 'a': protocol[0] = 'a'; break;
				
				default: printf("Invalid file format.");
			}
		}
		if (line == 2 + 9 * loopCounter){
			strcpy(sMac, currentLine);
		}
		if (line == 3 + 9 * loopCounter) {
			strcpy(dMac, currentLine);
		}
		if (line == 4 + 9 * loopCounter) {
			strcpy(target, currentLine);
		}
		if (line == 5 + 9 * loopCounter) {
			strcpy(source, currentLine);
		}
		if (line == 6 + 9 * loopCounter) {
			strcpy(sPort, currentLine);
		}
		if (line == 7 + 9 * loopCounter) {
			strcpy(dPort, currentLine);
		}
		if (line == 8 + 9 * loopCounter) {
			strcpy(data, currentLine);
		}
		line += 1;
	}
	
	if(fgets(currentLine, sizeof(currentLine), fptr) == NULL)
	{
		fileEnd = 1;
	}
	
	fclose(fptr);
	
	return(fileEnd);
}


void assembleAllPackets(FILE *fp)
{
	char sMac[17] = "00:00:00:00:00:00"; char dMac[17] = "00:00:00:00:00:00"; char target[11] = "00.00.00.00"; char source[11] = "00.00.00.00"; char sPort[5] = "00.00"; char dPort[5] = "00.00"; char data[65507] = "default"; char protocol[1] = "i";
	
	int fileEnd = 0;
	for(int i = 0; fileEnd == 0; i++)
	{
		fileEnd = readData(sMac, dMac, target, source, sPort, dPort, data, i, protocol);
		
	    	dataParse(sMac, dMac, target, source, sPort, dPort, data);

	    	assemblePacket(protocol[0], fp);
    	}
}


int main()
{
    time_t t;
    srand((unsigned) time(&t));
    FILE *fp;
    fp = fopen("generated-packets.pcapng","wb");
    pcapHeaderConstruct(fp);

    assembleAllPackets(fp);
    
    fclose(fp);

    return 0;
}
