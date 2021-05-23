void tcpConstruct(char tcpSegment[])
{
    int l_emptyPointer = 0;
    insertVarInto(PingReq.sPort, tcpSegment, l_emptyPointer, 2);
    insertVarInto(PingReq.dPort, tcpSegment, l_emptyPointer, 2);
    insertVarInto(seqNum, tcpSegment, l_emptyPointer, 4);
    insertVarInto(AckNum, tcpSegment, l_emptyPointer, 4);
    tcpSegment[l_emptyPointer++] = flags;
    insertVarInto(windowSize, tcpSegment, l_emptyPointer, 2);
    insertVarInto(checkSum, tcpSegment, l_emptyPointer, 2);
    tcpSegment[l_emptyPointer++] = 0x00; tcpSegment[l_emptyPointer++] = 0x00;//Urgent pointer?
    //then a bunch of options that are scary
    return;
}