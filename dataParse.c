struct packet
{
    //char sPort;
    //char dPort;
    char sMac[6];
    char dMac[6];
    char target[4];
    char source[4];
    char data[];
};

int dataParse(/*int sPort, int dPort, */int sMac[], int dMac[], int target[], int source[], char data[])
{   
    struct packet PingReq;
    
    for(int i = 0; i < sMac.length(); i += 3)
    {
        int digit1 = sMac[i] - 48;
        int digit2 = sMac[i + 1] - 48;
        if(digit1 > 9)
        {
            digit1 -= 39;
        }
        if(digit2 > 9)
        {
            digit2 -= 39;
        }
        
        PingReq.sMac[i/3] = digit1*16 + digit2
    }
    
    PingReq.sMac = sMac;
    PingReq.dMac = dMac;
    PingReq.target = target;
    PingReq.source = source;
    strcpy(PingReq.data, data);
    
    return 0;
}
