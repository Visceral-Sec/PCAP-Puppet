//#include <stdio.h>
//#include <string.h>

//create ip header on array
int ipConstruct()
{
    packetOut[14] = 0x45;
    packetOut[15] = PingReq.data.length(); //i dont know if this works - someone else test is please. - fin
    return 0;
}