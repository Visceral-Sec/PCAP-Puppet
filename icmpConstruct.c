/*TESTING*/
#include <stdio.h>
#include <string.h>

char packetOut[200]; //placeholder length - will fix

int emptyPointer = 0;//points to the first empty space in the array

/*END OF TESTING*/

//slaps icmp ¿packet? into the frame
int icmpConstruct()
{
    packetOut[emptyPointer++] = 0x08;//icmp ping request
    packetOut[emptyPointer++] = 0x00;//code is 0
    packetOut[emptyPointer++] = 0x00; packetOut[emptyPointer++] = 0x00;/*placeholder valueicmp check sum, I'll figure it out later */
    packetOut[emptyPointer++] = 0x00; packetOut[emptyPointer++] = 0x01;//identifier
    packetOut[emptyPointer++] = 0x00; packetOut[emptyPointer++] = 0x04;//sequence number 
    strncat(packetOut, PingReq.payload, strlen(PingReq.payload)); emptyPointer += strlen(PingReq.payload); 
    return 0;
}
