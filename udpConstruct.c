
void udpConstruct(char icmpSegment[])
{
    int l_emptyPointer = 0;
    insertVarInto(PingReq.sPort, udpSegment, l_emptyPointer, 2);
    insertVarInto(PingReq.dPort, udpSegment, l_emptyPointer, 2);
    insertVarInto(8 + pingReq.data, tcpSegment, l_emptyPointer, 2);
    insertVarInto(checkSum, tcpSegment, l_emptyPointer, 2);
    return;
}
