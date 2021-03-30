int icmpConstruct())
{
    strncat(packetOut, 0x08, 1);//icmp ping request
    strncat(packetOut, 0x00, 1);//code is 0
    strncat(packetOut, 0x????, 2);//icmp check sum, I'll figure it out later
    strncat(packetOut, 0x0001, 2);//identifier
    strncat(packetOut, 0x0004, 2);//sequence number 
    strncat(packetOut, PingReq.data, PingReq.data.length());
    
    return 0;
}
