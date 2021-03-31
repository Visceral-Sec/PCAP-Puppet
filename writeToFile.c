//write the frame's array to the pcap file
int writeToFile(char packetOut[114])
{
    FILE *fp;
    fp = fopen("pingReq.pcapng","wb");
    fwrite(packetOut, 114, 1, fp);
    return 0;
}
