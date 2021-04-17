#include <stdio.h>
#include <string.h>
struct packet
{
    char sMac[6];
    char dMac[6];
    char source[4];
    char target[4];
    char sPort;
    char dPort;
    char payload[100];
};
struct packet PingReq;
char packetOut[200]; //placeholder length - will fix
int emptyPointer = 0;

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
int dataParse(/*int sPort, int dPort, */char sMac[], char dMac[], char target[], char source[], char data[])
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
    
    /*
    PingReq.sMac = condenseChar(sMac, 11);
    PingReq.dMac = condenseChar(dMac, 11);
    PingReq.target = condenseChar(target, 7);
    PingReq.source = condenseChar(source, 7);
    */
    strcpy(PingReq.payload, data);
    
    return 0;
}

//constructs an ethernet header {dMac,sMac,IPv4} -> array of 14 bytes
int etherConstruct()
{
    strncat(packetOut, PingReq.dMac, 6); emptyPointer += 6;
    strncat(packetOut, PingReq.sMac, 6); emptyPointer += 6;
    packetOut[emptyPointer] = 0x08;
    emptyPointer++;
    packetOut[emptyPointer] = 0x03; //etherversion?  (IPv4) can't seem to condense it into one line
    emptyPointer++;
    return 0;
}

//slaps an IP header into the array
int ipConstruct()
{
    packetOut[emptyPointer] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    emptyPointer++;
    packetOut[emptyPointer] = 0x03; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    emptyPointer++;
    packetOut[emptyPointer] = 0x03;
    emptyPointer++;
    packetOut[emptyPointer] = strlen(PingReq.payload) + 28; //Identification? will check
    emptyPointer++;
    packetOut[emptyPointer] = 0x03; 
    emptyPointer++;
    packetOut[emptyPointer] = 0x03; //flags and fragment offset
    emptyPointer++;
    packetOut[emptyPointer] = 0x80; //ttl of 128
    emptyPointer++;
    packetOut[emptyPointer] = 0x01; //icmp is 01
    emptyPointer++;
    packetOut[emptyPointer] = 0x03; 
    emptyPointer++;
    packetOut[emptyPointer] = 0x03; //header checksum, 0000 means no validation
    emptyPointer++;
    strncat(packetOut, PingReq.source, 4); emptyPointer += 4;
    strncat(packetOut, PingReq.target, 4); emptyPointer += 4;
    return 0;
}

//slaps icmp ¿packet? into the frame
int icmpConstruct()
{
    packetOut[emptyPointer] = 0x08;//icmp ping request
    emptyPointer++;
    packetOut[emptyPointer] = 0x03;//code is 0
    emptyPointer++;
    packetOut[emptyPointer] = 0x03;
    emptyPointer++;
    packetOut[emptyPointer] = 0x03;/*placeholder value*///icmp check sum, I'll figure it out later
    emptyPointer++;
    packetOut[emptyPointer] = 0x03;
    emptyPointer++;
    packetOut[emptyPointer] = 0x01;//identifier
    emptyPointer++;
    packetOut[emptyPointer] = 0x03;
    emptyPointer++;
    packetOut[emptyPointer] = 0x04;//sequence number 
    emptyPointer++;
    strncat(packetOut, PingReq.payload, strlen(PingReq.payload)); emptyPointer += strlen(PingReq.payload); 
    return 0;
}


//construct all of the arrays into one frame array
int constructPacket()
{
    etherConstruct();
    ipConstruct();
    icmpConstruct();
    return 0;
}


//write the frame's array to the pcap file
int writeToFile()
{
    FILE *fp;
    fp = fopen("pingReq.pcapng","wb");
    fwrite(packetOut, 1, 114, fp);
    fclose(fp);
    return 0;
}

int main()
{
    char sMac[17] = "11:11:11:11:11:11"; char dMac[17] = "22:22:22:22:22:22"; char target[11] = "6f.6f.6f.6f"; char source[11] = "de.de.de.de"; char data[200] = "Yes, I do love C.";//placeholder line to get it to compile
    dataParse(sMac, dMac, target, source, data);
    constructPacket();
    writeToFile();
}
