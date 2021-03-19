#include <stdio.h>
#include <string.h>

int constructPacket(struct packet PingReq)
{
    char packetOut[200];
    strncat(packetOut, etherHeader, 14);
    packetOut[13] = 0x45;
    packetOut[14] = 0x00;
    packetOut[15] = datalen;
    return 0;
}