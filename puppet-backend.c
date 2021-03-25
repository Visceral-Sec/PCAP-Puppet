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
    packetOut[12] = 0x08; //ipv4?
    packetOut[13] = 0x00;
    return 0;
}

int ipConstruct()
{
    packetOut[14] = 0x45;
    packetOut[15] = PingReq.data.length(); //i dont know if this works - someone else test is please. - fin
    return 0;
}

//construct all of the arrays into one frame array
int constructPacket(struct packet Packet)
{
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
    etherConstruct():
    ipConstruct();
}
