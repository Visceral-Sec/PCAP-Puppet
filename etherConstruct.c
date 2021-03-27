int etherConstruct()
{
    strncat(packetOut, PingReq.dMac, 6);
    strncat(packetOut, PingReq.sMac, 6);
    strncat(packetOut, 0x0800, 2);
    return 0;
}