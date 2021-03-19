#include <stdio.h>

int sMac[];
int dMac[];
int sTarget[];
int dTarget[];
int sPort;
int dPort;
char[] payload;




int dataParse()
{
    return 0;
}

int constructPacket(char name[], int sPort, int dPort, int sMac, int dMac, int target[], int source[], char data[])
{
    struct packet PingReq;

    return 0;
}

int writeToFile(struct packet pingReq)
{
    FILE *fp;
    fp = fopen("./pingReq.pcapng","wb");
    fprintf(fp, "";
    return 0;
}

int main()
{
    puts("Hello World");
    return 0;
}
