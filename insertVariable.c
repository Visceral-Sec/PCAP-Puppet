//TESTING
#include <stdio.h>
#include <string.h>

char g_packetOut[100];
int g_emptyPointer = 6;
//END OF TESTING


//takes an array in and inserts it into the correct place, keeping emptyPointer safe
int insertVariable(char arrIn[], int bytesToWrite)
{
    for (int x = 0; x < bytesToWrite; x++)
    {
        g_packetOut[g_emptyPointer++] = arrIn[x];
    }
    return 0;
}

//TESTING
int main()
{
    char macAddr[6] = {11,11,11,11,11,11};
    insertVariable(macAddr, 6);
    for (int x = 0; x < 100; x++)
    {
        printf("|%d|", g_packetOut[x]);
    }
}

//TESTING