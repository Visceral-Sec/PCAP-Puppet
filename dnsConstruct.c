void dnsConstruct(char dnsSegment[])
{
    int l_emptyPointer = 0;
    insertVarInto(TransactionID, dnsSegment, l_emptyPointer, 2);//remains static throughout interaction
    insertVarInto(flags, dnsSegment, l_emptyPointer, 2);//0100 for standard query, 8580 for standard query response
    insertVarInto(0x0001, dnsSegment, l_emptyPointer, 2);//questions
    insertVarInto(0x0000, dnsSegment, l_emptyPointer, 2);//answers, would be 0x0001 for a response
    insertVarInto(0x00000000, dnsSegment, l_emptyPointer, 2);//RRses and stuff
    insertVarInto(query, dnsSegment, l_emptyPointer, strlen(query));//the query response repeats the query's data in its own data section
    return;
}
