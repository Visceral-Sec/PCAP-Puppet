#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int len;
	int line = 0;
	char currentLine[1000]; //variable holds current line in textfile
	char  sMac[17];
	char  dMac[17];
	char target[11];
	char source[11];
	char sPort[5];
	char dPort[5];
	char data[65507]; //max number of bytes for ICMP currentLine
	FILE *fptr; //Declaring a pointer
    fptr = fopen("templatePass.txt", "r"); //read
	if (fptr == NULL) { //check to see if file exists
		printf("Unable to open file");
		exit(1);
	}
	while (fscanf(fptr, "%s", currentLine) != EOF) { //EOF = End of file
		line = 0;
		if (strcmp(currentLine, "icmp8") == 0) {
			while (fgets(currentLine, sizeof(currentLine), fptr) != NULL && line < 8) { //reads the 7 lines under icmp8 
				fputs(currentLine, stdout);
				if (line == 1){
					strcpy(sMac, currentLine);
				}
				if (line == 2) {
					strcpy(dMac, currentLine);
				}
				if (line == 3) {
					strcpy(target, currentLine);
				}
				if (line == 4) {
					strcpy(source, currentLine);
				}
				if (line == 5) {
					strcpy(sPort, currentLine);
				}
				if (line == 6) {
					strcpy(dPort, currentLine);
				}
				if (line == 7) {
					strcpy(data, currentLine);
				}
				line += 1;
			}
		}
		//run dataparse with each set of variables?
	}
	fclose(fptr);
}