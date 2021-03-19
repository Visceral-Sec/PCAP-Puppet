#include <stdio.h>

int sMac[];
int dMac[];
int sTarget[];
int dTarget[];
int sPort;
int dPort;
char[] payload;




int dataParse(int sPort, int dPort, int sMac, int dMac, int target[], int source[], char data[])
{   
    struct packet PingReq;
    PingReq.sPort
    return 0;
}

int constructPacket(struct packet Packet)
{
    return 0;
}

int writeToFile(char packetOut[114])
{
    FILE *fp;
    fp = fopen("pingReq.pcapng","wb");
    fwrite(packetOut, 114, 1, fp);
    return 0;
}

int main()
{
    puts("Hello World");
    return 0;
}
