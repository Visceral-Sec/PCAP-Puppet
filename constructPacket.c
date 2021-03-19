#include <stdio.h>
#include <string.h>

struct packet
{
    int sPort;
    int dPort;
    int sMac[];
    int dMac[];
    int target[];
    int source[];
    char data[];
};

int constructPacket(char name[], int sPort, int dPort, int sMac, int dMac, int target[], int source[], char data[])
{
    struct packet PingReq;

    return 0;
}

int main()
{
    return 0;
}