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

int* condenseChar(int[] currentParam)//Turns a two digit string into a number
{
    int returnParam[currentParam.length()];
    
    for(int i = 0; i < currentParam.length(); i += 3)
    {
        int digit1 = currentParam[i] - 48;
        int digit2 = currentParam[i + 1] - 48;
        if(digit1 > 9)
        {
            digit1 -= 39;
        }
        if(digit2 > 9)
        {
            digit2 -= 39;
        }
        
        returnParam.append(digit1*16 + digit2);
    }
    
    return returnParam;
}

int dataParse(/*int sPort, int dPort, */int sMac[], int dMac[], int target[], int source[], char data[])
{   
    struct packet PingReq;
    
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in PingReq.sMac
    PingReq.sMac = condenseChar(sMac);
    PingReq.dMac = condenseChar(dMac);
    PingReq.target = condenseChar(target);
    PingReq.source = condenseChar(source);
    strcpy(PingReq.data, data);
    
    return 0;
}
