/*TESTING*/
#include <stdio.h>
#include <string.h>

char packetOut[200]; //placeholder length - will fix

int emptyPointer = 0;//points to the first empty space in the array

/*END OF TESTING*/

//constructs an ethernet header {dMac,sMac,IPv4} -> array of 14 bytes
int etherConstruct()
{
    strncat(packetOut, PingReq.dMac, 6); emptyPointer += 6;
    strncat(packetOut, PingReq.sMac, 6); emptyPointer += 6;
    packetOut[emptyPointer++] = 0x08; packetOut[emptyPointer++] = 0x00; //etherversion?  (IPv4) can't seem to condense it into one line
    return 0;
}

/*TESTING*/
int main()
{
    char sMac[6] = {12,12,12,12,12,12};
    char dMac[6] = {13,13,13,13,13,13};
    etherConstruct(dMac, sMac);
    for (int x = 0; x < 20; x++)
    {
        printf("%c", packetOut[x]);
    }
    puts("");
    return 0;
}

/*END OF TESTING*/