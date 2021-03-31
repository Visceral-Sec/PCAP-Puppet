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

//parse data from python frontend
int* condenseChar(int currentParam[])//Turns a two digit string into a number
{
    int emptyPointer = 0; //points to the empty space after the last filled entry
    int returnParam[strlen(currentParam)];

    for(int i = 0; i < strlen(currentParam); i += 3) //robert's magic to convert to suitable int arrays
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
        
        returnParam[emptyPointer++] = digit1*16 + digit2); //incriment emptyPointer after assignment
    }
    
    return returnParam;
}

//converts the incoming data into the correct formats for writing
int dataParse(/*int sPort, int dPort, */int sMac[], int dMac[], int target[], int source[], char data[])
{   
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in PingReq.sMac
    PingReq.sMac = condenseChar(sMac);
    PingReq.dMac = condenseChar(dMac);
    PingReq.target = condenseChar(target);
    PingReq.source = condenseChar(source);
    strcpy(PingReq.data, data);
    
    return 0;
}

//constructs an ethernet header {dMac,sMac,IPv4} -> array of 14 bytes
int etherConstruct()
{
    strncat(packetOut, PingReq.dMac, 6);
    strncat(packetOut, PingReq.sMac, 6);
    strncat(packetOut, 0x0800, 2);
    return 0;
}

//slaps an IP header into the array
int ipConstruct()
{
    strncat(packetOut, 0x45, 1); //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    strncat(packetOut, 0x00, 1); //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    strncat(packetOut, strlen(PingReq.payload) + 28, 2); //Identification? will check
    strncat(packetOut, 0x0000, 2); //flags and fragment offset
    strncat(packetOut, 0x80, 1); //ttl of 128
    strncat(packetOut, 0x01, 1); //icmp is 01
    strncat(packetOut, 0x0000, 2); //header checksum, 0000 means no validation
    strncat(packetOut, PingReq.source, 4);
    strncat(packetOut, PingReq.target, 4);
    return 0;
}

//slaps icmp ¿packet? into the frame
int icmpConstruct()
{
    strncat(packetOut, 0x08, 1);//icmp ping request
    strncat(packetOut, 0x00, 1);//code is 0
    strncat(packetOut, 0x0000/*placeholder value*/, 2);//icmp check sum, I'll figure it out later
    strncat(packetOut, 0x0001, 2);//identifier
    strncat(packetOut, 0x0004, 2);//sequence number 
    strncat(packetOut, PingReq.payload, strlen(PingReq.payload));
    
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
int writeToFile(char packetOut[114])
{
    FILE *fp;
    fp = fopen("pingReq.pcapng","wb");
    fwrite(packetOut, 114, 1, fp);
    return 0;
}

int main(int sMac[], int dMac[], int target[], int source[], char data[])
{
    dataParse(sMac, dMac, target, source, data);
    constructPacket();
}