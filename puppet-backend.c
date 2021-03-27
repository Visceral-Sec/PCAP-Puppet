#include <stdio.h>
#include <string.h>

char sMac[6];
char dMac[6];
char sTarget[4];
char dTarget[4];
char sPort;
char dPort;
char payload[100];

//parse data from python frontend
int dataParse(int sPort, int dPort, int sMac, int dMac, int target[], int source[], char data[])
{   
    struct packet PingReq;
    PingReq.sPort
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

int ipConstruct()
{
    strncat(packetOut, 0x45, 1); //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    strncat(packetOut, 0x00, 1); //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    strncat(packetOut, PingReq.length() + 20, 2); //Identification? will check
    strncat(packetOut, 0x0000, 2); //flags and fragment offset
    strncat(packetOut, 0x80, 1); //ttl of 128
    strncat(packetOut, 0x01, 1); //icmp is 01
    strncat(packetOut, 0x0000, 2); //header checksum, 0000 means no validation
    strncat(packetOut, PingReq.source, 4);
    strncat(packetOut, PingReq.target, 4);
    return 0;
}

//construct all of the arrays into one frame array
int constructPacket(struct packet PingReq)
{
    etherConstruct();
    ipConstruct();
    return 0;
}

int icmpConstruct())
{
    
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

int main()
{
    dataParse();
    constructPacket();
}