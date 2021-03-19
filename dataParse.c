struct packet
{
    int sPort;
    int dPort;
    int sMac[];
    int dMac[];
    int target[];
    int source[];
    char data[];
};

int dataParse(int sPort, int dPort, int sMac, int dMac, int target[], int source[], char data[])
{   
    struct packet PingReq;
    
    PingReq.sPort = sPort;
    PingReq.dPort = dPort;
    PingReq.sMac = sMac;
    PingReq.dMac = dMac;
    PingReq.target = target;
    PingReq.source = source;
    strcpy(PingReq.data, data);
    
    return 0;
}
