
void udpConstruct(char icmpSegment[])
{
    int l_emptyPointer = 0;
    insertVarInto(PingReq.sPort, udpSegment, l_emptyPointer, 2);
    insertVarInto(PingReq.dPort, udpSegment, l_emptyPointer, 2);
    insertVarInto(8 + strlen(PingReq.payload), udpSegment, l_emptyPointer, 2);
    insertVarInto(checkSum, udpSegment, l_emptyPointer, 2);
    insertVarInto(PingReq.payload, udpSegment, l_emptyPointer, strlen(PingReq.payload));
    return;
}
