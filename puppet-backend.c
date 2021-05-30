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
};
struct packet PingReq;

//for testing mainly
void read_pcap_out(char pcapOut[], short pcapLen)
{
    for (short x = 0; x < pcapLen; x++)
    {
        printf("%c", pcapOut[x]);
    }
    return;
}

// the below function is from http://www.microhowto.info/howto/calculate_an_internet_protocol_checksum_in_c.html (18/05/2021 - we need to cite this) to create a C function to calc an rfc 1071 checksum
// it has been reformatted and altered to keep with the style of the other code (and so that it works in our context)

uint16_t calcChecksum(void* vdata, size_t length) //uint16_t is a 16-bit unsigned short
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
void insertVarInto(char arrIn[], char arrOut[], short l_emptyPointer, short bytesToWrite)
{
    for (short x = 0; x < bytesToWrite; x++)
    {
        arrOut[l_emptyPointer++] = arrIn[x];
    }
    return;
}

//parse data from python frontend
short * condenseChar(char currentParam[], short paramSize)//Turns a two digit string into a number
{
    short l_emptyPointer = 0; //points to the last filled entry (ofc -1 isnt filled but it has to start somewhere)
    static short returnParam[/*paramSize - 3 - (paramSize - 7)/2*/10];
    for(short i = 0; i < paramSize; i += 3) //robert's magic to convert to suitable short arrays
    {
        short digit1 = currentParam[i] - 48;
        short digit2 = currentParam[i + 1] - 48;
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
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in PingReq.sMac
    for(short i = 0; i < 6; i++)
    {
    	PingReq.sMac[i] = condenseChar(sMac, 17)[i];
    }
    for(short i = 0; i < 6; i++)
    {
    	PingReq.dMac[i] = condenseChar(dMac, 17)[i];
    }
    for(short i = 0; i < 4; i++)
    {
    	PingReq.target[i] = condenseChar(target, 11)[i];
    }
    for(short i = 0; i < 4; i++)
    {
    	PingReq.source[i] = condenseChar(source, 11)[i];
    }
    for(short i = 0; i < 2; i++)
    {
    	PingReq.sPort[i] = condenseChar(sPort, 5)[i];
    }
    for(short i = 0; i < 2; i++)
    {
    	PingReq.dPort[i] = condenseChar(dPort, 5)[i];
    }
    
    strcpy(PingReq.payload, data);
    return;
}


//returns num^pow as a long short
long power(short num, short pow)
{
	long result = 1;
	for(short i = 0; i < pow; i++)
	{
		result *= num;
	}
	
	return(result);
}


//adds on to pcap epoch in hex and little endian
void epoch(char pcap[], short l_emptyPointer)
{
    long seconds;
    seconds = time(NULL);
    
    long divisor = power(16, 9);
    char hex[4];
    short temp;
    
    for(short i = 9; i >= 0; i--)
    {
    	short result = seconds/divisor;
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
void headerConstruct(char pcap[], char etherFrame[], short etherFrameLen)
{
    //is only written at the start of a pcap
    short l_emptyPointer = 0;
    char headerStart[] = {0xD4, 0xC3, 0xB2, 0xA1, 0x02, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00};

    insertVarInto(headerStart, pcap, 0, 24); l_emptyPointer += 24;
	
    //is after every packet 
    epoch(pcap, l_emptyPointer); l_emptyPointer += 4;
    pcap[l_emptyPointer++] = 0x81; pcap[l_emptyPointer++] = 0x08; pcap[l_emptyPointer++] = 0x03; pcap[l_emptyPointer++] = 0x00;//milliseconds since last second, is currently just static because it doesn't really matter
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//length of packet excluding header
    pcap[l_emptyPointer++] = etherFrameLen; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00; pcap[l_emptyPointer++] = 0x00;//the same thing again for some reason it wants it twice
    insertVarInto(etherFrame, pcap, 40, etherFrameLen);
    return;
}

//slaps icmp segment into the frame
void icmpReqConstruct(char icmpReqSegment[], short seqNum, short segmentLen)
{
    short l_emptyPointer = 0;
    icmpReqSegment[l_emptyPointer++] = 0x08;//icmp ping request
    icmpReqSegment[l_emptyPointer++] = 0x00;//code is 0
    icmpReqSegment[l_emptyPointer++] = 0x00; icmpReqSegment[l_emptyPointer++] = 0x00;//icmp checksum, this is a placeholder for later in the function
    icmpReqSegment[l_emptyPointer++] = 0x00; icmpReqSegment[l_emptyPointer++] = 0x01;//identifier?
    char seqNumArr[2] = {seqNum >> 8, seqNum & 0x00FF};
    insertVarInto(seqNumArr, icmpReqSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insertVarInto(PingReq.payload, icmpReqSegment, l_emptyPointer, strlen(PingReq.payload));
    short checksum = calcChecksum(icmpReqSegment, segmentLen);
    char checksumArr[2] = {checksum & 0x00FF, checksum >> 8}; //was little endian, lower 8 bits read in first then upper to make it big endian (don't want to change checksum funct)
    insertVarInto(checksumArr, icmpReqSegment, 2, 2);
    return;
}

/*
//creates a transport layer tcp header
void tcpConstruct(char tcpSegment[])
{
    short l_emptyPointer = 0;
    insertVarInto(PingReq.sPort, tcpSegment, l_emptyPointer, 2);
    insertVarInto(PingReq.dPort, tcpSegment, l_emptyPointer, 2);
    insertVarInto(seqNum, tcpSegment, l_emptyPointer, 4); //seq num
    insertVarInto(AckNum, tcpSegment, l_emptyPointer, 4); //ack num
    tcpSegment[l_emptyPointer++] = flags; //tcp flags - probably easier to impliment once parsing is done
    insertVarInto(windowSize, tcpSegment, l_emptyPointer, 2);
    insertVarInto(checkSum, tcpSegment, l_emptyPointer, 2);
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//Urgent pointer?
    //then a bunch of options that are scary
    return;
}*/

/*
void udpConstruct(char udpSegment[])
{
    short l_emptyPointer = 0;
    insertVarInto(PingReq.sPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    insertVarInto(PingReq.dPort, udpSegment, l_emptyPointer, 2); l_emptyPointer += 2;
    
    if(8 + strlen(PingReq.payload) < 256)
    {
    	udpSegment[l_emptyPointer++] = 0x00;
    	udpSegment[l_emptyPointer++] = 8 + strlen(PingReq.payload);
    }
    else
    {
    	udpSegment[l_emptyPointer++] = 8 + strlen(PingReq.payload); l_emptyPointer++;
    }
    
    //insertVarInto(checkSum, udpSegment, l_emptyPointer, 2);
    insertVarInto(PingReq.payload, udpSegment, l_emptyPointer, strlen(PingReq.payload));
    return;
}*/

/*
void arpConstruct(char arpSegment[])
{
    short l_emptyPointer = 0;
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Hardware type
    arpSegment[l_emptyPointer++] = 0x08; arpSegment[l_emptyPointer++] = 0x00;//IPv4
    arpSegment[l_emptyPointer++] = 0x06;//Hardware size
    arpSegment[l_emptyPointer++] = 0x04;//protocol size
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Request
    insertVarInto(PingReq.sMac, arpSegment, l_emptyPointer, 6);
    insertVarInto(PingReq.source, arpSegment, l_emptyPointer, 4);
    insertVarInto(0x000000000000, arpSegment, l_emptyPointer, 6);
    insertVarInto(PingReq.target, arpSegment, l_emptyPointer, 4);
    return;
}*/

/*
void dnsConstruct(char dnsSegment[])
{
    short l_emptyPointer = 0;
    insertVarInto(TransactionID, dnsSegment, l_emptyPointer, 2);//remains static throughout interaction
    insertVarInto(flags, dnsSegment, l_emptyPointer, 2);//0100 for standard query, 8580 for standard query response
    insertVarInto(0x0001, dnsSegment, l_emptyPointer, 2);//questions
    insertVarInto(0x0000, dnsSegment, l_emptyPointer, 2);//answers, would be 0x0001 for a response
    insertVarInto(0x00000000, dnsSegment, l_emptyPointer, 2);//RRses and stuff
    insertVarInto(query, dnsSegment, l_emptyPointer, strlen(query));//the query response repeats the query's data in its own data section
    return;
}*/

//slaps an IP header into the array
void ipConstruct(char ipPacket[], char transportSegment[], short transportSegLen, short ipPacketLen)
{
    short l_emptyPointer = 0;
    ipPacket[l_emptyPointer++] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    ipPacket[l_emptyPointer++] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    char ipPacketLenArr[2] = {ipPacketLen >> 8, ipPacketLen & 0x00FF};
    insertVarInto(ipPacketLenArr, ipPacket, l_emptyPointer, 2); l_emptyPointer += 2; //length of packet  (excl. ether)
    ipPacket[l_emptyPointer++] = 0x1b; ipPacket[l_emptyPointer++] = 0xd1; //idenfitication???????????
    ipPacket[l_emptyPointer++] = 0x00; ipPacket[l_emptyPointer++] = 0x00; //flags and fragment offset
    ipPacket[l_emptyPointer++] = 0x80; //ttl of 128
    ipPacket[l_emptyPointer++] = 0x01; //icmp is 01
    ipPacket[l_emptyPointer++] = 0x00; ipPacket[l_emptyPointer++] = 0x00; //header checksum, 0000 means no validation
    insertVarInto(PingReq.source, ipPacket, l_emptyPointer, 4); l_emptyPointer += 4; //not being incrimented by insertVarInto :(
    insertVarInto(PingReq.target, ipPacket, l_emptyPointer, 4); l_emptyPointer += 4;
    insertVarInto(transportSegment, ipPacket, l_emptyPointer, transportSegLen);
    return;
}

//constructs an ethernet header {dMac,sMac,IPv4} -> array of 14 bytes
void etherConstruct(char etherFrame[], char networkPacket[], short netPacketLen)
{
    short l_emptyPointer = 0;
    insertVarInto(PingReq.dMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    insertVarInto(PingReq.sMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    etherFrame[l_emptyPointer++] = 0x08; etherFrame[l_emptyPointer++] = 0x00; //etherversion? ¿IPv4? can't seem to condense it into one line
    insertVarInto(networkPacket, etherFrame, l_emptyPointer, netPacketLen);
    return;
}


//construct all of the arrays into one frame array - needs more work
short constructPacket(char bigArr[512], char protocol)
{

    short segmentLen;
    char *segment;
    
    switch(protocol)
    {
	case 'i':
	
    	segmentLen = 8 + strlen(PingReq.payload);
    	segment = (char *)malloc(sizeof(char) * segmentLen); //reserves (8 + length of payload) bytes on the heap
    	icmpReqConstruct(segment, 0, segmentLen);
    	
    	break;
    /*	
	case 'u':
	
    	segmentLen = 6 + strlen(PingReq.payload);
    	segment = (char *)malloc(sizeof(char) * segmentLen); //reserves (8 + length of payload) bytes on the heap
    	udpConstruct(segment);
    	
    	break;
    	
    	
	case 't':
	
    	segmentLen = 6 + strlen(PingReq.payload);
    	segment = (char *)malloc(sizeof(char) * segmentLen); //reserves (8 + length of payload) bytes on the heap
    	tcpConstruct(segment);
    	
    	break;
    	
	case 'a':
	
    	segmentLen = 6 + strlen(PingReq.payload);
    	segment = (char *)malloc(sizeof(char) * segmentLen); //reserves (8 + length of payload) bytes on the heap
    	arpConstruct(segment);
    	
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
    
    char *ipPacket;

    short ipPacketLen = 20 + segmentLen;
    ipPacket = (char *)malloc(sizeof(char) * (ipPacketLen)); //reserves 20 + segmentLen bytes onthe heap
    ipConstruct(ipPacket, segment, segmentLen, ipPacketLen); //builds on top of the icmpseg
    //read_pcap_out(ipPacket, ipPacketLen); //use this for testing
    
    char *etherFrame;
    short etherFrameLen = 14 + ipPacketLen;
    etherFrame = (char *)malloc(sizeof(char) * (etherFrameLen)); //reserves 14 bytes on the heap
    etherConstruct(etherFrame, ipPacket, ipPacketLen); //builds on top of the ipPacket
    
    char *pcap; //header + frame in an array
    short pcapLen = 40 + etherFrameLen;
    pcap = (char *)malloc(sizeof(char) * (pcapLen)); //reserves 40 + etherFrameLen bytes on the heap
    headerConstruct(pcap, etherFrame, etherFrameLen); //builds on top of the ipPacket
    
    insertVarInto(pcap, bigArr, 0, pcapLen); //insert each of the parts of the frame into the bigArr

    free(segment); //free up the reserved space on the heap
    free(ipPacket);
    free(etherFrame);
    free(pcap);

    return pcapLen;
}


void assemblePacket(char protocol, FILE *fp)
{
    char bigArr[1024];
    short pcapLen = constructPacket(bigArr, protocol);

    char *pcapOut;
    pcapOut = (char *)malloc(sizeof(char) * pcapLen);
    insertVarInto(bigArr, pcapOut, 0, pcapLen);

    //read_pcap_out(pcapOut, bigArrLen);
    fwrite(pcapOut, 1, pcapLen, fp);
    
    free(pcapOut);
}


int main()
{
    FILE *fp;
    fp = fopen("pingReq.pcapng","wb");

    char sMac[17] = "a8:a1:59:33:f4:00"; char dMac[17] = "40:0d:10:53:0d:e0"; char target[11] = "ac.d9.a9.4e"; char source[11] = "c0.a8.00.3a"; char sPort[5] = "1b.43"; char dPort[5] = "00.50"; char data[33] = "abcdefghijklmnopqrstuvwabcdefgh"; char protocol = 'i';//placeholder line to get it to compile
    dataParse(sMac, dMac, target, source, sPort, dPort, data);

    assemblePacket(protocol, fp);
    
    fclose(fp);

    return 0;
}
