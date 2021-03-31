//slaps an IP header into the array
int ipConstruct()
{
    strncat(packetOut, 0x45, 1); //0b0100 version 4 IP + 0101 IP header length (means 20??? but represents 5)
    strncat(packetOut, 0x00, 1); //0b000000 Default differenteiated services codepoint + 00 non ECN-capable transport
    strncat(packetOut, strlen(PingReq.payload) + 28, 2); //Identification? will check
    strncat(packetOut, 0x0000, 2); //flags and fragment offset
    strncat(packetOut, 0x80, 1); //ttl of 128
    strncat(packetOut, 0x01, 1); //icmp is 01
    strncat(packetOut, 0x0000, 2); //header checksum, 0000 means no validation
    strncat(packetOut, PingReq.source, 4);
    strncat(packetOut, PingReq.target, 4);
    return 0;
}