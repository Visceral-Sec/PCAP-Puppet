#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <arpa/inet.h>
#include <stdlib.h>

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

//REMOVE THIS IF FOUND IN BACKEND
void read_pcap_out(char pcapOut[], int pcapLen)
{
    for (int x = 0; x < pcapLen; x++)
    {
        printf("%c", pcapOut[x]);
    }
    return;
}

// the below function is from http://www.microhowto.info/howto/calculate_an_internet_protocol_checksum_in_c.html (18/05/2021 - we need to cite this) to create a C function to calc an rfc 1071 checksum
// it has been reformatted and altered to keep with the style of the other code (and so that it works in our context)

uint16_t calcChecksum(void* vdata, size_t length) //uint16_t is a 16-bit unsigned int
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
void insertVarInto(char arrIn[], char arrOut[], int l_emptyPointer, int bytesToWrite)
{
    for (int x = 0; x < bytesToWrite; x++)
    {
        arrOut[l_emptyPointer++] = arrIn[x];
    }
    return;
}

//parse data from python frontend
int * condenseChar(char currentParam[], int paramSize)//Turns a two digit string into a number
{
    int paramPointer = 0; //points to the last filled entry (ofc -1 isnt filled but it has to start somewhere)
    static int returnParam[/*paramSize - 3 - (paramSize - 7)/2*/10];
    for(int i = 0; i < paramSize; i += 3) //robert's magic to convert to suitable int arrays
    {
        int digit1 = currentParam[i] - 48;
        int digit2 = currentParam[i + 1] - 48;
        if(digit1 > 9)
        {
            digit1 -= 39;
        }
        if(digit2 > 9)
        {
            digit2 -= 39;
        }
        returnParam[paramPointer] = digit1*16 + digit2; //incriment endPointer before assignment
        paramPointer++;
    }
    
    return returnParam;
}

//converts the incoming data into the correct formats for writing
void dataParse(char sMac[17], char dMac[17], char target[11], char source[11], char sPort[5], char dPort[5], char data[])
{   
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in PingReq.sMac
    for(int i = 0; i < 6; i++)
    {
    	PingReq.sMac[i] = condenseChar(sMac, 17)[i];
    }
    for(int i = 0; i < 6; i++)
    {
    	PingReq.dMac[i] = condenseChar(dMac, 17)[i];
    }
    for(int i = 0; i < 4; i++)
    {
    	PingReq.target[i] = condenseChar(target, 11)[i];
    }
    for(int i = 0; i < 4; i++)
    {
    	PingReq.source[i] = condenseChar(source, 11)[i];
    }
    for(int i = 0; i < 2; i++)
    {
    	PingReq.sPort[i] = condenseChar(sPort, 5)[i];
    }
    for(int i = 0; i < 2; i++)
    {
    	PingReq.dPort[i] = condenseChar(dPort, 5)[i];
    }
    
    
    strcpy(PingReq.payload, data);
    return;
}

//jujhaar needs to do this one properly, this is a placeholder function to get proto 1 going
void headerConstruct(char bigArr[])
{
    char placeholderHeader[] = {0xD4, 0xC3, 0xB2, 0xA1, 0x02, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x5D, 0x31, 0x25, 0x60, 0xE7, 0xC8, 0x07, 0x00, 0x4A, 0x00, 0x00, 0x00, 0x4A, 0x00, 0x00, 0x00};
    insertVarInto(placeholderHeader, bigArr, 0, 40);
    return;
}

//slaps icmp segment into the frame
void icmpConstruct(char icmpSegment[])
{
    int l_emptyPointer = 0;
    icmpSegment[l_emptyPointer++] = 0x08;//icmp ping request
    icmpSegment[l_emptyPointer++] = 0x00;//code is 0
    icmpSegment[l_emptyPointer++] = 0x00; icmpSegment[l_emptyPointer++] = 0x00;/*placeholder value*///icmp check sum, I'm currently figuring it out
    icmpSegment[l_emptyPointer++] = 0x00; icmpSegment[l_emptyPointer++] = 0x01;//identifier?
    icmpSegment[l_emptyPointer++] = 0x00; icmpSegment[l_emptyPointer++] = 0x00;//sequence number 
    insertVarInto(PingReq.payload, icmpSegment, l_emptyPointer, strlen(PingReq.payload));
    return;
}
/*
//creates a transport layer tcp header
void tcpConstruct(char tcpSegment[])
{
    int l_emptyPointer = 0;
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
}
*/

void udpConstruct(char udpSegment[])
{
    int l_emptyPointer = 0;
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
}
/*
void arpConstruct(char arpSegment[])
{
    int l_emptyPointer = 0;
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Hardware type
    arpSegment[l_emptyPointer++] = 0x08; arpSegment[l_emptyPointer++] = 0x00;//IPv4
    arpSegment[l_emptyPointer++] = 0x06;//Hardware size
    arpSegment[l_emptyPointer++] = 0x04;//Protocal size
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Request
    insertVarInto(PingReq.sMac, arpSegment, l_emptyPointer, 6);
    insertVarInto(PingReq.source, arpSegment, l_emptyPointer, 4);
    insertVarInto(0x000000000000, arpSegment, l_emptyPointer, 6);
    insertVarInto(PingReq.target, arpSegment, l_emptyPointer, 4);
    return;
}

void dnsConstruct(char dnsSegment[])
{
    int l_emptyPointer = 0;
    insertVarInto(TransactionID, dnsSegment, l_emptyPointer, 2);//remains static throughout interaction
    insertVarInto(flags, dnsSegment, l_emptyPointer, 2);//0100 for standard query, 8580 for standard query response
    insertVarInto(0x0001, dnsSegment, l_emptyPointer, 2);//questions
    insertVarInto(0x0000, dnsSegment, l_emptyPointer, 2);//answers, would be 0x0001 for a response
    insertVarInto(0x00000000, dnsSegment, l_emptyPointer, 2);//RRses and stuff
    insertVarInto(query, dnsSegment, l_emptyPointer, strlen(query));//the query response repeats the query's data in its own data section
    return;
}*/

//slaps an IP header into the array
void ipConstruct(char ipPacket[], char transportSegment[], int transportSegLen, int ipPacketLen)
{
    int l_emptyPointer = 0;
    ipPacket[l_emptyPointer++] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    ipPacket[l_emptyPointer++] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    ipPacket[l_emptyPointer++] = 0x00; ipPacket[l_emptyPointer++] = ipPacketLen; //frame length - also it doesnt work if > 255 length lmao
    ipPacket[l_emptyPointer++] = 0x1d; ipPacket[l_emptyPointer++] = 0x1d; //idenfitication???????????
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
void etherConstruct(char etherFrame[], char networkPacket[], int netPacketLen)
{
    int l_emptyPointer = 0;
    insertVarInto(PingReq.dMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    insertVarInto(PingReq.sMac, etherFrame, l_emptyPointer, 6); l_emptyPointer += 6;
    etherFrame[l_emptyPointer++] = 0x08; etherFrame[l_emptyPointer++] = 0x00; //etherversion?  (IPv4) can't seem to condense it into one line
    insertVarInto(networkPacket, etherFrame, l_emptyPointer, netPacketLen);
    return;
}


//construct all of the arrays into one frame array - needs more work
int constructPacket(char bigArr[512], char protocal)
{
    int protocalSegLen;
    char *protocalSegment;
    
    //finds the given protocal segment
    switch(protocal)
    {
	case 'i':
	
    	protocalSegLen = 8 + strlen(PingReq.payload);
    	protocalSegment = (char *)malloc(sizeof(char) * protocalSegLen); //reserves (8 + length of payload) bytes on the heap
    	icmpConstruct(protocalSegment);
    	
    	break;
    	
	case 'u':
	
    	protocalSegLen = 6 + strlen(PingReq.payload);
    	protocalSegment = (char *)malloc(sizeof(char) * protocalSegLen); //reserves (8 + length of payload) bytes on the heap
    	udpConstruct(protocalSegment);
    	
    	break;
    	/*
    	
	case 't':
	
    	protocalSegLen = 6 + strlen(PingReq.payload);
    	protocalSegment = (char *)malloc(sizeof(char) * protocalSegLen); //reserves (8 + length of payload) bytes on the heap
    	tcpConstruct(protocalSegment);
    	
    	break;
    	
	case 'a':
	
    	protocalSegLen = 6 + strlen(PingReq.payload);
    	protocalSegment = (char *)malloc(sizeof(char) * protocalSegLen); //reserves (8 + length of payload) bytes on the heap
    	arpConstruct(protocalSegment);
    	
    	break;
    	
	case 'd':
	
    	protocalSegLen = 6 + strlen(PingReq.payload);
    	protocalSegment = (char *)malloc(sizeof(char) * protocalSegLen); //reserves (8 + length of payload) bytes on the heap
    	dnsConstruct(protocalSegment);
    	
    	break;
    	*/
    }
    
    char *ipPacket;
    int ipPacketLen = 20 + protocalSegLen;
    ipPacket = (char *)malloc(sizeof(char) * (ipPacketLen)); //reserves 20 bytes onthe heap
    ipConstruct(ipPacket, protocalSegment, protocalSegLen, ipPacketLen); //builds on top of the icmpseg
    //read_pcap_out(ipPacket, ipPacketLen);
    
    char *etherFrame;
    int etherFrameLen = 14 + ipPacketLen;
    etherFrame = (char *)malloc(sizeof(char) * (etherFrameLen)); //reserves 14 bytes on the heap
    etherConstruct(etherFrame, ipPacket, ipPacketLen); //builds on top of the ipPacket
    
    insertVarInto(etherFrame, bigArr, 0, etherFrameLen); //insert each of the parts of the frame into the bigArr

    free(protocalSegment); //free up the reserved space on the heap
    free(ipPacket);
    free(etherFrame);

    return etherFrameLen;
}


void assemblePacket(char protocal, FILE *fp)
{
    char packetOut[512];
    int packetLen = 0; 
    packetLen = constructPacket(packetOut, protocal);

    char bigArr[512];
    int bigArrLen = packetLen + 40;
    headerConstruct(bigArr);
    insertVarInto(packetOut, bigArr, 40, packetLen);

    char *pcapOut;
    pcapOut = (char *)malloc(sizeof(char) * bigArrLen);
    insertVarInto(bigArr, pcapOut, 0, bigArrLen);

    //read_pcap_out(pcapOut, bigArrLen);
    fwrite(pcapOut, 1, bigArrLen, fp);
    
    free(pcapOut);
}


int main()
{
    FILE *fp;
    fp = fopen("pingReq.txt","wb");

    char sMac[17] = "11:11:11:11:11:11"; char dMac[17] = "22:22:22:22:22:22"; char target[11] = "6f.6f.6f.6f"; char source[11] = "de.de.de.de"; char sPort[5] = "1b.43"; char dPort[5] = "00.50"; char data[18] = "Yes, I do love C."; int icmpSize = 0; int tcpSize = 0; int udpSize = 1; int arpSize = 0; int dnsSize = 0;//placeholder line to get it to compile
    dataParse(sMac, dMac, target, source, sPort, dPort, data);

    //for each protocal it will loop for however many its size is
    for(int i = 0; i < icmpSize; i++)
    {
    	assemblePacket('i', fp);
    }
    for(int i = 0; i < tcpSize; i++)
    {
    	assemblePacket('t', fp);
    }
    for(int i = 0; i < udpSize; i++)
    {
    	assemblePacket('u', fp);
    }
    for(int i = 0; i < arpSize; i++)
    {
    	assemblePacket('a', fp);
    }
    for(int i = 0; i < dnsSize; i++)
    {
    	assemblePacket('d', fp);
    }
    
    fclose(fp);

    return 0;
}





