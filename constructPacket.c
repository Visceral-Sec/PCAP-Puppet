#include <stdio.h>
#include <string.h>

struct packet
{
    int sport;
    int dport;
    int smac[];
    int dmac[];
    int target[];
    int source[];
    char data[];
}

int main()
{
    return 0;
}