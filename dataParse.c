/*TESTING*/
#include <stdio.h>
#include <string.h>
struct packet
{
    char sMac[6];
    char dMac[6];
    char source[4];
    char target[4];
    char sPort;
    char dPort;
    char payload[100];
};

struct packet PingReq;
char packetOut[200]; //placeholder length - will fix

/*END OF TESTING*/

//parse data from python frontend
int* condenseChar(int currentParam[])//Turns a two digit string into a number
{
    int paramEndPointer = -1; //points to the last filled entry (ofc -1 isnt filled but it has to start somewhere)
    int returnParam[strlen(currentParam)];

    for(int i = 0; i < strlen(currentParam); i += 3) //robert's magic to convert to suitable int arrays
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
        
        returnParam[++paramEndPointer] = digit1*16 + digit2; //incriment endPointer before assignment
    }
    
    return returnParam;
}

//converts the incoming data into the correct formats for writing
int dataParse(/*int sPort, int dPort, */int sMac[], int dMac[], int target[], int source[], char data[])
{   
    //Goes through each pair of ascii numbers in target parameter and stores them as a single 8 bit char in PingReq.sMac
    PingReq.sMac = condenseChar(sMac);
    PingReq.dMac = condenseChar(dMac);
    PingReq.target = condenseChar(target);
    PingReq.source = condenseChar(source);
    strcpy(PingReq.payload, data);
    
    return 0;
}