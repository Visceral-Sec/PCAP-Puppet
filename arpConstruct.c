//creates arp ¿query? part packet
void arpConstruct(char icmpSegment[])
{
    int l_emptyPointer = 0;
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Hardware type
    arpSegment[l_emptyPointer++] = 0x08; arpSegment[l_emptyPointer++] = 0x00;//IPv4
    arpSegment[l_emptyPointer++] = 0x06;//Hardware size
    arpSegment[l_emptyPointer++] = 0x04;//Protocal size
    arpSegment[l_emptyPointer++] = 0x00; arpSegment[l_emptyPointer++] = 0x01;//Request
    insertVarInto(PingReq.sMac, arpSegment, l_emptyPointer, 6);
    insertVarInto(PingReq.source, arpSegment, l_emptyPointer, 4);
    insertVarInto(0x000000000000, arpSegment, l_emptyPointer, 6);
    insertVarInto(PingReq.target, arpSegment, l_emptyPointer, 4);
    return;
}
