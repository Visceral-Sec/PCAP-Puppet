//construct all of the arrays into one frame array
int constructPacket()
{
    etherConstruct();
    ipConstruct();
    icmpConstruct();
    return 0;
}