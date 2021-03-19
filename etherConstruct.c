int etherConstruct()
{
    strncat(packetOut, PingReq.dMac, 6);
    strncat(packetOut, PingReq.sMac, 6);
    packetOut[11] = 0x08;
    packetOut[12] = 0x00;
    return 0;
}