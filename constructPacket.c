#include <stdio.h>
#include <string.h>

struct packet
{
    int sPort;
    int dPort;
    int sMac[];
    int dMac[];
    int target[];
    int source[];
    char data[];
}

int main()
{
    return 0;
}