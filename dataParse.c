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
    return 0;
}
