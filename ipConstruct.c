//#include <stdio.h>
//#include <string.h>

//create ip header on array
int ipConstruct()
{
    packetOut[14] = 0x45; //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    packetOut[15] = 0x00; //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    strncat(packetOut, PingReq.length() + 20, 2); //Identification? will check
    strncat(packetOut, 0x0000, 2); //flags and fragment offset
    packetOut[20] = 0x80; //ttl of 128
    packetOut[21] = 0x01; //icmp is 01
    strncat(packetOut, 0x0000, 2); //header checksum, 0000 means no validation
    strncat(packetOut, PingReq.source, 4);
    strncat(packetOut, PingReq.target, 4);
    return 0;
}