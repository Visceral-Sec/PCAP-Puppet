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
char g_packetOut[200]; //placeholder length - will fix
int g_emptyPointer = 0;

//takes an array in and inserts it into the correct place, keeping emptyPointer safe
int insertVariable(char arrIn[], int bytesToWrite)
{
    for (int x = 0; x < bytesToWrite; x++)
    {
        g_packetOut[g_emptyPointer++] = arrIn[x];
    }
    return 0;
}

//parse data from python frontend
int* condenseChar(int currentParam[], int paramSize)//Turns a two digit string into a number
{
    int paramPointer = 0; //points to the last filled entry (ofc -1 isnt filled but it has to start somewhere)
    int returnParam[paramSize - 3 - (paramSize - 7)/2];

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
int dataParse(/*int sPort, int dPort, */int sMac[], int dMac[], int target[], int source[], char data[])
{   
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in PingReq.sMac
    
    for(int i = 0; i < 6; i++)
    {
    	PingReq.sMac[i] = condenseChar(sMac, 11)[i];
    }
    
    for(int i = 0; i < 6; i++)
    {
    	PingReq.dMac[i] = condenseChar(dMac, 11)[i];
    }
    
    for(int i = 0; i < 4; i++)
    {
    	PingReq.target[i] = condenseChar(target, 7)[i];
    }
    
    for(int i = 0; i < 4; i++)
    {
    	PingReq.source[i] = condenseChar(source, 7)[i];
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
    insertVariable(PingReq.dMac, 6);
    insertVariable(PingReq.sMac, 6);
    g_packetOut[g_emptyPointer++] = 0x08; g_packetOut[g_emptyPointer++] = 0x00; //etherversion?  (IPv4) can't seem to condense it into one line
    return 0;
}

//slaps an IP header into the array
int ipConstruct()
{
    g_packetOut[g_emptyPointer++] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    g_packetOut[g_emptyPointer++] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    g_packetOut[g_emptyPointer++] = 0x00; g_packetOut[g_emptyPointer++] = strlen(PingReq.payload) + 28; //Identification? will check
    g_packetOut[g_emptyPointer++] = 0x00; g_packetOut[g_emptyPointer++] = 0x00; //flags and fragment offset
    g_packetOut[g_emptyPointer++] = 0x80; //ttl of 128
    g_packetOut[g_emptyPointer++] = 0x01; //icmp is 01
    g_packetOut[g_emptyPointer++] = 0x00; g_packetOut[g_emptyPointer++] = 0x00; //header checksum, 0000 means no validation
    insertVariable(PingReq.source, 4);
    insertVariable(PingReq.target, 4);
    return 0;
}

//slaps icmp ¿packet? into the frame
int icmpConstruct()
{
    g_packetOut[g_emptyPointer++] = 0x08;//icmp ping request
    g_packetOut[g_emptyPointer++] = 0x00;//code is 0
    g_packetOut[g_emptyPointer++] = 0x00; g_packetOut[g_emptyPointer++] = 0x00;/*placeholder value*///icmp check sum, I'll figure it out later
    g_packetOut[g_emptyPointer++] = 0x00; g_packetOut[g_emptyPointer++] = 0x01;//identifier
    g_packetOut[g_emptyPointer++] = 0x00; g_packetOut[g_emptyPointer++] = 0x04;//sequence number 
    insertVariable(PingReq.payload, strlen(PingReq.payload));
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
int writeToFile(char g_packetOut[114])
{
    FILE *fp;
    fp = fopen("pingReq.pcapng","wb");
    fwrite(g_packetOut, 114, 1, fp);
    return 0;
}

int main()
{
    int sMac[6]; int dMac[6]; int target[4]; int source[4]; char data[200];//placeholder line to get it to compile
    dataParse(sMac, dMac, target, source, data);
    constructPacket();
}