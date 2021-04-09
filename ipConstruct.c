/*TESTING*/
#include <stdio.h>
#include <string.h>

char packetOut[200]; //placeholder length - will fix

int emptyPointer = 0;//points to the first empty space in the array

/*END OF TESTING*/

//slaps an IP header into the array
int ipConstruct()
{
    packetOut[emptyPointer++] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    packetOut[emptyPointer++] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    packetOut[emptyPointer++] = 0x00; packetOut[emptyPointer++] = strlen(PingReq.payload) + 28; //Identification? will check
    packetOut[emptyPointer++] = 0x00; packetOut[emptyPointer++] = 0x00; //flags and fragment offset
    packetOut[emptyPointer++] = 0x80; //ttl of 128
    packetOut[emptyPointer++] = 0x01; //icmp is 01
    packetOut[emptyPointer++] = 0x00; packetOut[emptyPointer++] = 0x00; //header checksum, 0000 means no validation
    strncat(packetOut, PingReq.source, 4); emptyPointer += 4;
    strncat(packetOut, PingReq.target, 4); emptyPointer += 4;
    return 0;
}