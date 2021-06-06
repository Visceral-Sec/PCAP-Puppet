# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    PCAP_PUPPET GUI    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code Synposis ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Libraries Used For Calling the C Backend
import os
import random

#Libraries Used for the GUI
from tkinter import *
import tkinter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code Synposis ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Pcap Puppet GUI uses the Tkinter Library for creating the GUI.    
# 
#   Pcap_Puppet GUI follows a set metholodogy for each Protocol:
#  
#   Protocol is Chosen --> Input is Taken --> Protocol Information is Displayed/stored in specific Classes --> Input Checked For Errors  --> Input is written into data.txt/Backend is called
#                      
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frames/Master ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Pcap_Puppet GUI Guidance (Good Youtube Tutorial for those wanting to help with GUI)
#https://www.youtube.com/watch?v=YXPyB4XeYLA

#Tkinter works a bit like HTML, but instead of objects etc we have widgets

master = Tk() #This is the root of the entire gui
master.geometry('779x582') # sets default size
master.title("PCAP PUPPET") #Setting the Title
master.resizable(False, False) #Prevents the GUI from being resizable

#change this depending on path
path = "Project"

#Path to the C backend: (Looks for "PcapPuppet_BackEnd")
#Compiled Using "Gcc - shared puppet-backend.C -o puppet-backend "
backend_file = "puppet-backend"
#Pcap Puppet BackEnd

#call the c compiled executable
puppet_backend = "./puppet-backend"

#Frame for Pcap Settings
sConfig_Frame= Frame(master)
sConfig_Frame.place(x=510, y = 40)

#Frame for Pcap History
cConfig_Frame= Frame(master)
cConfig_Frame.place(x=510, y = 250)

#Frame for layer configuraiton
lconfig_Frame = Frame(master)
lconfig_Frame.place(x=0,y=50, width=500)

#Frame for Titles "Protocols"/"Configuration"/"PCAP Settings"
tConfig_Frame = LabelFrame(master)
tConfig_Frame.place(x=0,y=0, width=780)

#Frame for Protocol Configuraiton Settings

pConfig_Frame = Frame(master)
pConfig_Frame.grid(row = (0), column = 1, sticky = W)

#Pcap Button Frame

pCreate_Frame = Frame(master)
pCreate_Frame.place(x=515, y = 445)


#Frame for Pcap History/Current Traffic Configuraiton
cConfigLabel = LabelFrame(master, text = "", width=268, height=195)
cConfigLabel.place(x=510, y= 268)

#Frame for Traffic Configuration
TrafficConfigFrame = LabelFrame(master, text = "", width=160, height=174)
TrafficConfigFrame.place(x = 618, y = 66)

#Traffic Size Frame

TrafficSizeFrame = LabelFrame(master, text = "", width=108, height=174)
TrafficSizeFrame.place(x = 511, y = 66)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start_Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Popup window for the GUI 

Startup = Toplevel(master)
Startup.title("Pcap Puppet Introduction")
Startup.resizable(False, False)
StartupLabel = LabelFrame(Startup, text="", width=250, height=250)
StartupLabel.pack()
StartupWelcome = Label(StartupLabel, text="Welcome to Pcap_Puppet!")
StartupHelp = Label(StartupLabel, text="If this is the first time you've used Pcap_Puppet please refer to PcapPuppetIntroduction.pdf for guidance")
StartupSupported = Label(StartupLabel, text="Our currently support Protocols are: ")
StartupProtocol1 = Label(StartupLabel, text="ICMP")
StartupProtocol2 = Label(StartupLabel, text="ARP")
StartupProtocol3 = Label(StartupLabel, text="DNS")
StartupWelcome.pack()
StartupHelp.pack()
StartupSupported.pack()
StartupProtocol1.pack()
StartupProtocol2.pack()
StartupProtocol3.pack()



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Labels ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#This is the label widget + postioning for the top left "Protocol"
tProtocol = Label(tConfig_Frame, text = "PROTOCOLS", font=("Arial", 25), borderwidth=1,  relief="solid",)
tProtocol.grid(row = 0, column = 0, sticky = W)

#This is the label widget + postioning for the middle "Configuration"
tConfiguration = Label(tConfig_Frame, text = " CONFIGURATION", font=("Arial", 25), borderwidth=1,  relief="solid",)
tConfiguration.grid(row = 0, column = 1, sticky = W)

#This is the label widget + postioning for the top left "Protocol"
tPcapConfig = Label(tConfig_Frame, text = "PCAP SETTINGS", font=("Arial", 25), borderwidth=1,  relief="solid",)
tPcapConfig.grid(row = 0, column = 2, sticky = W)

#Current Traffic Label
CurrentTraffic = Label(master, text = "Current Traffic", font=("Arial", 16), borderwidth=1,  relief="solid", width=22)
CurrentTraffic.place(x = 510, y = 240)

#Current Traffic Configuration Label
TrafficConfiguration = Label(master, text = "Traffic  Configuration", font=("Arial", 13), borderwidth=1,  relief="solid",)
TrafficConfiguration.place(x = 617, y = 43)

#Pcap Specific Settings
TrafficConfiguration = Label(master, text = " Traffic Size   ", font=("Arial", 13), borderwidth=1,  relief="solid",)
TrafficConfiguration.place(x = 510, y = 43)

#Pcap Size Entry:
SizeEntry = Entry(TrafficSizeFrame, width=10)
SizeEntry.place(x=4, y=30)

#Pcap Max Packet Size
SizeEntryLabel = Label(TrafficSizeFrame,text="Max Packet Size:")
SizeEntryLabel.place(x=1, y=5)

#Wireshark Label 
WireSharkLabel = Label(TrafficSizeFrame,text="Wireshark Version:")
WireSharkLabel.place(x=1, y=50)

#Wiresharkvar
wiresharkVar = StringVar(TrafficSizeFrame)
wiresharkVar.set("3.4.5")
wiresharkOption = OptionMenu(TrafficSizeFrame, wiresharkVar,"3.4.5")
wiresharkOption.place(x=1, y=70)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Classes are used for holding user inputs as well as potential errors.
# Classes are pivotal to Pcap_Puppet. They can be used in Tkinter to return values in functions. 
# Functions used in Tkinter are unable to return Values, therefore we need to make classes to store and load values through.

#Layer 2 Classes

class ethernetConfig:
    dmac = ""
    smac = ""
    smacerror = [0,0,0,0]
    dmacerror = [0,0,0,0]
    size = ""

class wifiConfig:
    reciver = ""
    transmitter = ""
    destination = ""
    source = ""
    bss = ""
    bssErrors = [0,0,0,0]
    reciverErrors = [0,0,0,0]
    transmitterErrors = [0,0,0,0]
    destinationErrors = [0,0,0,0]
    sourceErrors = [0,0,0,0]
    phy = ""
    mcs = ""
    Freq = ""
    DataR = ""
    Channel = ""
    size = ""

class arpConfig:
    sendermac = ""
    targetmac = ""
    senderip = ""
    targetip = ""
    macerror = [0,0,0,0]
    dmacerror = [0,0,0,0]
    iperror = [0,0]
    diperror = [0,0]
    size = ""

#Layer 3 Classes
class ipConfig:
    destinationIp = ""
    sourceIp = ""
    TIL = ""
    iperror = [0,0]
    diperror = [0,0]
    size = ""
class icmpConfig:
    icmptext = ""
    ip = ""
    mac = ""
    dip = ""
    dmac = ""
    macerror = [0,0,0,0]
    dmacerror = [0,0,0,0]
    iperror = [0,0]
    diperror = [0,0]
    size = ""
    Text = ""
class ripConfig:
    ResponseIP = ""
    ip = ""
    port = ""
    dport = ""
    dip = ""
    port = ""
    RipVer = ""
    size = ""
    ipError = [0,0]
class ospfConfig:
    sourcerouter = ""
    backuprouter = ""
    mask = ""
    sourcerouterError = [0,0]
    backuprouterError = [0,0]
    maskError = [0,0]
    message = ""
    size = ""
    dip = ""
    TIL = ""


#Layer 4 UDP/TCP
class udpConfig:
    port = ""
    dport = ""
    ip = ""
    dip = ""
    ipError = [0,0]
    dipError = [0,0]
    size = ""
class tcpConfig:
    port = ""
    dport = ""
    ip = ""
    dip = ""
    window = ""
    padding = ""
    ipError = [0,0]
    dipError = [0,0]
    size = ""
#Layer 5

class socksConfig:
    Auth = ""
    DIP = ""
    ipError = [0,0]
    DPort = ""
    ID = ""
    Config = ""
    size = ""
class netbiosConfig:
    Name = ""
    gName = ""
    Session = ""
    Datagram = ""
    Service = ""
    size  = ""
    port = ""
    dport = "187"
    ip = ""
    window = ""
    padding = ""
    dip = ""

class smbConfig:
    cid = ""
    command = ""
    implementation = ""
    size = ""
    ip = ""
    dip = ""
    sport = ""
    dport = "137"

#layer 6

class tlsConfig:
    cert = ""
    CipherSuite = ""
    size = ""
class sshConfig:
    placeholder = ""
    size = ""

#Layer 7

class dhcpConfig:
    dip =  ""
    ReqIP = ""
    mType = ""
    Lease = ""
    DomainName = ""
    DomainIP = ""
    Host = ""
    RouterIP = ""
    SubnetMask = ""
    size = ""
    ip = ""
    dipError = [0,0]
    reqError = [0,0]
    domainError = [0,0]
    RouterError = [0,0]
    maskError = [0,0]
    port = "68"
    sport = "67"
class telnetConfig:
    Rcomand1 = ""
    Rcomand2 = ""
    Rcomand3 = ""
    Rcomand4 = ""
    Rcomand5 = ""
    command = ""
    operation = ""
    operationOption = ""
    size = ""
    dport = ""
    port = ""
    ip = ""
    dip = ""
    padding = ""
    window = ""
class ircConfig:
    command = ""
    message = ""
    Name = ""
    size = ""
    sport = ""
    dport = "6666"
    window = ""
    padding = ""
    port = "6667"
    dip = ""
    ip = ""
class ftpConfig:
    ip = ""
    dip = ""
    port = ""
    data = ""
    file = ""
    size = ""
    type = [0,0]
    iperror = [0,0]
    diperror = [0,0]
    window = ""
    padding = ""
    dport = "21"
    port = "20"
class httpConfig:
    URL = ""
    UserAgent = ""
    PostUri = ""
    GetUri = ""
    GetReferrer = ""
    PostData = ""
    size = ""
    ip = ""
    dip = ""
    dport = "80"
    port = ""
    window = ""
    padding = ""
class httpsConfig:
    URL = ""
    UserAgent = ""
    PostUri = ""
    GetUri = ""
    GetReferrer = ""
    PostData = ""
    size = ""
    SSLKey = ""
    ip = ""
    dip = ""
    dport = "443"
    port = ""
    window = ""
    padding = ""
class dnsConfig:
    dip = ""
    Cport = ""
    Type = ""
    Class = ""
    AnswerIP = ""
    TIL = ""
    AnswerName = ""
    dipError = [0,0]
    size = ""
    ip = ""
    port = "57"
    dport = "58"

# Misc Classes:

#Used for Spinboxes
class TrafficSize:
    size = 0

    #Used for configuring where to put spinboxes (Locations change depending on previous choices (e.g dynamic locations))
class LocationConfiguration:
        size = 1
        x = 0
        y = 0
        xl = 0
        yl = 0

#These Classes exist for error checking purposes and checks if the protocol is being used
    #First Array indicates their is an error
    #Second array indicates if it's been chosen
    # third array value indicates if it's been displayed (to prevent from it display again)
class Config:
    Ethernet=[0,0,0]
    Wifi=[0,0,0]
    #Layer 3
    ICMP=[0,0,0]
    ARP=[0,0,0]
    RIP=[0,0,0]
    OSPF=[0,0,0]
    IP=[0,0,0]
    #Layer 4 
    UDP=[0,0,0]
    TCP=[0,0,0]
    #Layer 5 
    SOCKS=[0,0,0]
    NetBIOS=[0,0,0]
    SMB=[0,0,0]
    #Layer 6
    TLS=[0,0,0]
    SSL=[0,0,0]
    FTP=[0,0,0]
    SSH=[0,0,0]
    #Layer 7
    SOAP=[0,0,0]
    DHCP=[0,0,0]
    TELNET=[0,0,0]
    IRC=[0,0,0]
    FTP=[0,0,0]
    HTTP=[0,0,0]
    HTTPS=[0,0,0]
    DNS=[0,0,0]

#Error Checking Classes. Thesea are used in the Error checking functions, They exist as seperate classes so that they can be used in error checking functions and then set into other classes (Allows modular use of the error checking function)
class IPErrors:
    error = [0,0]
class MACErrors:
    error = [0,0,0,0]
class PcapConfig:
    wiresharkVER = "3.4.5"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def returnHexNums():
    hexString = "0123456789abcdef"
    return str(random.choice(hexString))+str(random.choice(hexString))+"."+str(random.choice(hexString))+str(random.choice(hexString))

#This Function is called right at the End of the Program. It writes as the information stored in the classes above to a data.txt to be used by the Backend to generate the pcap
def pcapWrite():
    
    #The library to write to files is very similar to that of C file.io library
    pcap_path = os.path.join("Data.txt")
    f = open(pcap_path, "w")
    #More meta information can be added here

    if Config.ARP[1] == 1:
        f.write("ar\n")
        # add icmp arp etc here
        f.write(arpConfig.sendermac + "\n")
        f.write("00:00:00:00:00:00"+ "\n")
        f.write(arpConfig.senderip + "\n")
        f.write(arpConfig.targetip + "\n")
        f.write("00.00\n")
        f.write("00.00\n")
        f.write("placeholder\n")
        f.write("00\n")
        f.write("00\n")
        f.write("aa\n")
        f.write(arpConfig.targetmac + "\n")
        f.write(arpConfig.sendermac + "\n")
        f.write(arpConfig.targetip + "\n")
        f.write(arpConfig.senderip + "\n")
        f.write("00\n")
        f.write("00\n")
        f.write("placeholder\n")
        f.write("00\n")
        f.write("00\n")

    #if ICMP is selected.
    if Config.ICMP[1] == 1:
        icmpID = returnHexNums()
        seqNum = returnHexNums()
        f.write("ir\n") #request
        # add icmp data etc here
        f.write(icmpConfig.mac + "\n")
        f.write(icmpConfig.dmac + "\n")
        f.write(icmpConfig.ip + "\n")
        f.write(icmpConfig.dip + "\n")
        f.write("00.00\n")
        f.write("00.00\n")
        f.write(icmpConfig.Text)
        f.write(icmpID + "\n")
        f.write(seqNum + "\n")
        f.write("ia\n") #reply to request
        f.write(icmpConfig.dmac + "\n")
        f.write(icmpConfig.mac + "\n")
        f.write(icmpConfig.dip + "\n")
        f.write(icmpConfig.ip + "\n")
        f.write("00.00\n")
        f.write("00.00\n")
        f.write(icmpConfig.Text)
        f.write(icmpID + "\n")
        f.write(seqNum + "\n")

    # Unsupported Functions: (Functional on FrontEnd, Backend does not support them)
    # CRTL K CRTL C  To comment
    # CRTL K CRTL U  to uncomment  

    # if Config.Ethernet[1] == 1:
    #     f.write("Eth\r\n")
    #     f.write(ethernetConfig.dmac + "\r\n")
    #     f.write(ethernetConfig.smac + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.Wifi[1] == 1:
    #     f.write("Wifi\n")
    #     f.write(wifiConfig.reciver + "\r\n")
    #     f.write(wifiConfig.transmitter + "\r\n")
    #     f.write(wifiConfig.source + "\r\n")
    #     f.write(wifiConfig.destination + "\r\n")
    #     f.write(wifiConfig.bss + "\r\n")
    #     f.write(wifiConfig.phy + "\r\n")
    #     f.write(wifiConfig.mcs + "\r\n")
    #     f.write(wifiConfig.Freq + "\r\n")
    #     f.write(wifiConfig.DataR + "\r\n")
    #     f.write(wifiConfig.Channel + "\r\n")
    #     f.write("0\r\n")
     #   f.write("\r\n")

    # if Config.RIP[1] == 1:
    #     f.write("RIP\n")
    #     # add icmp data etc here
    #     f.write(ripConfig.ResponseIP + "\r\n")
    #     f.write(ripConfig.RipVer + "\r\n")
    #      f.write(ripConfig.ip + "\r\n")
    #      f.write(ripConfig.dip + "\r\n")
    #      f.write(ripConfig.port + "\r\n")
    #      f.write(ripConfig.dport + "\r\n")
    #     f.write(ripConfig.size + "\r\n")
    #     f.write("00\n")
    #     f.write("0\r\n")
    
    # if Config.OSPF[1] == 1:
    #     f.write("OSPF\n")
    #     # add icmp data etc here
    #     f.write(ospfConfig.sourcerouter + "\r\n")
    #     f.write(ospfConfig.backuprouter + "\r\n")
    #     f.write(ospfConfig.dip + "\r\n")
    #     f.write(ospfConfig.TIL + "\r\n")
    #     f.write(ospfConfig.mask + "\r\n")
    #     f.write(ospfConfig.message + "\r\n")
    #     f.write(ospfConfig.size + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")
    
    # if Config.SOCKS[1] == 1:
    #     f.write("SOCKS\n")
    #     # add icmp data etc here
    #     f.write(socksConfig.DIP + "\r\n")
    #     f.write(socksConfig.DPort + "\r\n")
    #     f.write(socksConfig.ID + "\r\n")
    #     f.write(socksConfig.Config + "\r\n")
    #     f.write(socksConfig.Auth + "\r\n")
    #     f.write("0\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.NetBIOS[1] == 1:
    #     f.write("NetBIOS\n")
    #     # add icmp data etc here
    #     f.write(netbiosConfig.Name + "\r\n")
    #     f.write(netbiosConfig.gName + "\r\n")
    #     f.write(netbiosConfig.Session + "\r\n")
    #     f.write(netbiosConfig.Datagram + "\r\n")
    #     f.write(netbiosConfig.Service + "\r\n")
    #     f.write(netbiosConfig.Size + "\r\n")
    #     f.write(netbiosConfig.port + "\r\n")
    #     f.write(netbiosConfig.dport + "\r\n")
    #     f.write(netbiosConfig.ip + "\r\n")
    #     f.write(netbiosConfig.window + "\r\n")
    #     f.write(netbiosConfig.padding + "\r\n")
    #     f.write(netbiosConfig.dip + "\r\n")
    #     f.write("0\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.SMB[1] == 1:
    #     f.write("SMB\n")
    #     f.write(smbConfig.cid + "\r\n")
    #     f.write(smbConfig.command + "\r\n")
    #     f.write(smbConfig.implementation + "\r\n")
    #     f.write(smbConfig.dip + "\r\n")
    #     f.write(smbConfig.ip + "\r\n")
    #     f.write(smbConfig.sport + "\r\n")
    #     f.write(smbConfig.dport + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.TLS[1] == 1:
    #     f.write("TLS\n")
    #     f.write(tlsConfig.cert + "\r\n")
    #     f.write(tlsConfig.CipherSuite + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.SSH[1] == 1:
    #     f.write("SSH\n")
    #     f.write(sshConfig.placeholder + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.DHCP[1] == 1:
    #     f.write("DHCP\n")
    #     f.write(dhcpConfig.dip + "\r\n")
    #     f.write(dhcpConfig.ip + "\r\n")
    #     f.write(dhcpConfig.ReqIP + "\r\n")
    #     f.write(dhcpConfig.mType + "\r\n")
    #     f.write(dhcpConfig.Lease + "\r\n")
    #     f.write(dhcpConfig.DomainName + "\r\n")
    #     f.write(dhcpConfig.DomainIP + "\r\n")
    #     f.write(dhcpConfig.Host + "\r\n")
    #     f.write(dhcpConfig.RouterIP + "\r\n")
    #     f.write(dhcpConfig.SubnetMask + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.TELNET[1] == 1:
    #     f.write("Telnet\n")
    #     f.write(telnetConfig.Rcomand1 + "\r\n")
    #     f.write(telnetConfig.Rcomand2 + "\r\n")
    #     f.write(telnetConfig.Rcomand3 + "\r\n")
    #     f.write(telnetConfig.Rcomand4 + "\r\n")
    #     f.write(telnetConfig.Rcomand5 + "\r\n")
    #     f.write(telnetConfig.command + "\r\n")
    #     f.write(telnetConfig.operation + "\r\n")
    #     f.write(telnetConfig.operationOption + "\r\n")
    #     f.write(telnetConfig.dport + "\r\n")
    #     f.write(telnetConfig.port + "\r\n")
    #     f.write(telnetConfig.window + "\r\n")
    #     f.write(telnetConfig.padding + "\r\n")
    #     f.write(telnetConfig.dip + "\r\n")
    #     f.write(telnetConfig.ip + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.FTP[1] == 1:
    #     f.write("FTP\n")
    #     f.write(ftpConfig.ip + "\r\n")
    #     f.write(ftpConfig.dip + "\r\n")
    #     f.write(ftpConfig.port + "\r\n")
    #     f.write(ftpConfig.data + "\r\n")
    #     f.write(ftpConfig.file + "\r\n")
    #     f.write(ftpConfig.data + "\r\n")
    #     f.write(ftpConfig.window + "\r\n")
    #     f.write(ftpConfig.padding + "\r\n")
    #     f.write(ftpconfig.size + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")
    
    # if Config.IRC[1] == 1:
    #     f.write("IRC\n")
    #     f.write(ircConfig.command + "\r\n")
    #     f.write(ircConfig.message + "\r\n")
    #     f.write(ircConfig.Name + "\r\n")
    #     f.write(ircConfig.window + "\r\n")
    #     f.write(ircConfig.padding + "\r\n")
    #     f.write(ircConfig.dip + "\r\n")
    #     f.write(ircConfig.ip + "\r\n")
    #     f.write(ircConfig.size + "\r\n")
    #     f.write("0\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    # if Config.HTTP[1] == 1:
    #     f.write("HTTP\n")
    #     f.write(httpConfig.URL + "\r\n")
    #     f.write(httpConfig.UserAgent + "\r\n")
    #     f.write(httpConfig.PostUri + "\r\n")
    #     f.write(httpConfig.GetUri + "\r\n")
    #     f.write(httpConfig.GetReferrer + "\r\n")
    #     f.write(httpConfig.PostData + "\r\n")
    #     f.write(httpConfig.size + "\r\n")
    #     f.write(httpConfig.ip + "\r\n")
    #     f.write(httpConfig.dip + "\r\n")
    #     f.write(httpConfig.window + "\r\n")
    #     f.write(httpConfig.padding + "\r\n")
    #     f.write(httpConfig.port + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")
    
    # if Config.HTTPS[1] == 1:
    #     f.write("HTTPS\r\n")
    #     f.write(httpsConfig.URL + "\r\n")
    #     f.write(httpsConfig.UserAgent + "\r\n")
    #     f.write(httpsConfig.PostUri + "\r\n")
    #     f.write(httpsConfig.GetUri + "\r\n")
    #     f.write(httpsConfig.GetReferrer + "\r\n")
    #     f.write(httpsConfig.PostData + "\r\n")
    #     f.write(httpsConfig.size + "\r\n")
    #     f.write(httpsConfig.SSLKey + "\r\n")
    #     f.write(httpsConfig.ip + "\r\n")
    #     f.write(httpsConfig.dip + "\r\n")
    #     f.write(httpsConfig.window + "\r\n")
    #     f.write(httpsConfig.padding + "\r\n")
    #     f.write(httpsConfig.port + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")
    
    # if Config.DNS[1] == 1:
    #     f.write("DNS\r\n")
    #     f.write(dnsConfig.dip + "\r\n")
   #       f.write(dnsConfig.ip + "\r\n")
    #     f.write(dnsConfig.Cport + "\r\n")
    #     f.write(dnsConfig.Type + "\r\n")
    #     f.write(dnsConfig.Class + "\r\n")
    #     f.write(dnsConfig.AnswerIP + "\r\n")
    #     f.write(dnsConfig.TIL + "\r\n")
    #     f.write(dnsConfig.AnswerName + "\r\n")
    #     f.write("0\r\n")
    #     f.write("\r\n")

    f.write("\0")

#Location Configuration is a dynamic function used for placing Protocol Information in the right places when called by the GUI. 
def LocationConfig():
    placed = 0 
    #XY are used for placing the Spin/Tick boxes
    LocationConfiguration.x = 0 
    LocationConfiguration.y = 0 
    #XlYl are used for placing the Spin/Tick Labels
    LocationConfiguration.xl = 0
    LocationConfiguration.yl = 0
    if (LocationConfiguration.size % 2) != 0 or LocationConfiguration.size == 1:
            if LocationConfiguration.size == 1:
                LocationConfiguration.xl = 0
                LocationConfiguration.yl = 3
                LocationConfiguration.x = 40
                LocationConfiguration.y = 3
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1 
            if LocationConfiguration.size == 3:
                LocationConfiguration.xl = 0
                LocationConfiguration.yl = 28
                LocationConfiguration.x = 40
                LocationConfiguration.y = 28
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1 
            if LocationConfiguration.size == 5:
                LocationConfiguration.xl = 0
                LocationConfiguration.yl = 53
                LocationConfiguration.x = 40
                LocationConfiguration.y = 53
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1
            if LocationConfiguration.size == 7:
                LocationConfiguration.xl = 0
                LocationConfiguration.yl = 78
                LocationConfiguration.x = 40
                LocationConfiguration.y = 78
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1 
        #If the option is even then the option is displayed on the right
    if (LocationConfiguration.size % 2) == 0 and placed == 0:
        if LocationConfiguration.size == 2:
                LocationConfiguration.xl = 80
                LocationConfiguration.yl = 3
                LocationConfiguration.x = 110
                LocationConfiguration.y = 3
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1
        if LocationConfiguration.size == 4:
                LocationConfiguration.xl = 80
                LocationConfiguration.yl = 28
                LocationConfiguration.x = 110
                LocationConfiguration.y = 53
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1
        if LocationConfiguration.size == 6:
                LocationConfiguration.xl = 80
                LocationConfiguration.yl = 53
                LocationConfiguration.x = 110
                LocationConfiguration.y = 53
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1
        if LocationConfiguration.size == 8:
                LocationConfiguration.xl = 80
                LocationConfiguration.yl = 78
                LocationConfiguration.x = 110
                LocationConfiguration.y = 78
                LocationConfiguration.size = LocationConfiguration.size + 1
                placed = 1


def ErrorReset():   # This function resets every error, (This is used to prevent from previous errors displaying) 
    IPErrors.error[0] = 0
    IPErrors.error[1] = 0
    MACErrors.error[0] = 0
    MACErrors.error[1] = 0
    MACErrors.error[2] = 0
    MACErrors.error[3] = 0

    #Ethernet Errors
    Config.Ethernet[0] = 0
    for x in range(0,3):
        ethernetConfig.dmacerror[x] = 0
        ethernetConfig.smacerror[x] = 0

    #Wifi Errors
    Config.Wifi[0] = 0
    for x in range(0,3):
        wifiConfig.bssErrors[x] = 0
        wifiConfig.reciverErrors[x] = 0
        wifiConfig.transmitterErrors[x] = 0
        wifiConfig.destinationErrors[x] = 0
        wifiConfig.sourceErrors[x] = 0

    #Arp Errors
    Config.ARP[0] = 0
    for x in range(0,3):
        arpConfig.macerror[x] = 0
        arpConfig.dmacerror[x] = 0
    arpConfig.iperror[0] = 0
    arpConfig.diperror[1] = 0
    arpConfig.iperror[0] = 0
    arpConfig.diperror[1] = 0

    #Ip Errors
    Config.IP[0] = 0
    ipConfig.iperror[0] = 0
    ipConfig.iperror[1] = 0
    ipConfig.diperror[0] = 0
    ipConfig.diperror[1] = 0

    #ICMP Errors
    Config.ICMP[0] = 0
    icmpConfig.macerror[0] = 0
    icmpConfig.macerror[1] = 0
    icmpConfig.macerror[2] = 0
    icmpConfig.macerror[3] = 0
    icmpConfig.iperror[0] = 0
    icmpConfig.iperror[1] = 0 
    
    #rip Error
    Config.RIP[0] = 0
    ripConfig.ipError[0] = 0
    ripConfig.ipError[1] = 0

    #ospf
    Config.OSPF[0] = 0
    for x in range(0,1):
        ospfConfig.sourcerouterError[x] = 0
        ospfConfig.backuprouterError[x] = 0
        ospfConfig.maskError[x] = 0
    
    #UDP
    Config.UDP[0] = 0
    udpConfig.ipError[0] = 0
    udpConfig.ipError[1] = 0
    udpConfig.dipError[0] = 0
    udpConfig.dipError[1] = 0

    #TCP
    Config.TCP[0] = 0
    tcpConfig.ipError[0] = 0
    tcpConfig.ipError[1] = 0
    tcpConfig.dipError[0] = 0
    tcpConfig.dipError[1] = 0 

    #socks
    Config.SOCKS[0] = 0
    socksConfig.ipError[0] = 0
    socksConfig.ipError[1] = 0
    #Netbios
    Config.NetBIOS[0] = 0
    #smb
    Config.SMB[0] = 0
    #tls
    Config.TLS[0] = 0
    #dhcp
    Config.DHCP[0] = 0
    for x in range(0,1):
        dhcpConfig.dipError[x] = 0
        dhcpConfig.reqError[x] = 0
        dhcpConfig.maskError[x] = 0
        dhcpConfig.RouterError[x] = 0
        dhcpConfig.domainError[x] = 0
    #Telnet
    Config.TELNET[0] = 0
    #irc
    Config.IRC[0] = 0
    #ftp
    Config.FTP[0] = 0
    for x in range(0,1):
        ftpConfig.diperror[x] = 0
        ftpConfig.iperror[x] = 0
    #http
    Config.HTTP[0] = 0
    #https
    Config.HTTPS[0] = 0
    #DNS
    Config.DNS[0] = 0
    dnsConfig.dipError[0] = 0
    dnsConfig.dipError[1] = 0


def CMPErrorReset():     # This resets each compare error (This is to prevent previous protocol errors effecting other checks)
    IPErrors.error[0] = 0
    IPErrors.error[1] = 0
    MACErrors.error[0] = 0
    MACErrors.error[1] = 0
    MACErrors.error[2] = 0
    MACErrors.error[3] = 0



#Slight edited by Archer, but mainly coded by Matt. This function checks the validatility of the IP.
def IP_checker(IP): # Coded by Matt
    IP_breakdown = [] #Storage for each part of the IP
    points_count = 0 #Verifying given address has 3 points
    IP_part = ''
    for i in range(len(IP)):
        if IP[i] == '.':
            points_count += 1
            IP_breakdown.append(IP_part) #After each point, the concatenated string collected is put into a list
            IP_part = '' #IP_part cleared for new section
        else:
            IP_part += str(IP[i])
    IP_breakdown.append(IP_part)
    if points_count == 3:
        IP_breakdown = [int(i) for i in IP_breakdown] #Converting elements from string to int
        for i in range(len(IP_breakdown)):
            if 0 <= IP_breakdown[i] <= 255: #Checking IP numbers are in valid range
                pass
            else:
                IPErrors.error[0] = 1 #Ips aren't valid
                return 
    else:
        IPErrors.error[1] = 2 #Ip doesn't have enough octects
        return



#Loads the overall size of the traffic (The entry box)
def SizeLoader():
    TrafficSize.size = SizeEntry.get()

#Slight edited by Archer, but mainly coded by Matt. This function checks the validatility of the MAC.
def MAC_checker(MAC): # Coded by Matt
    acceptable_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ':']
    acceptable_placesforcolon = [2, 5, 8, 11, 14]
    MAC = MAC.lower()
    if len(MAC) != 17: #Num of chars in MAC address is 17
        MACErrors.error[0] = 1
    if MAC[2] != ':' or MAC[5] != ':' or MAC[8] != ':' or MAC[11] != ':' or MAC[14] != ':': #If no colon at specific points
        MACErrors.error[1] = 2
    for i in range(len(MAC)):
        if MAC[i] == ':' and i not in acceptable_placesforcolon: #Colon not used to identify address, only chars and digits
            MACErrors.error[2] = 3
    for i in range(len(MAC)):
        if MAC[i] not in acceptable_chars: #Only letters numbers and colons excepted
            MACErrors.error[3] = 4
    return(0) # Edited to allow for easier user parsing


# The Follow Functions apply to the buttons on the left side of the GUI. Each Displayer function refers to one of the buttons of the left in ascending order

#Layer 2 Button Displayer
def layer2_Displayer(l): # The purpose of this functions is that every layer menu option will call one of this funcitons followed with the selection option. In this case that is L.
    layer2_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration", width=284, height=529) # This then prints the label heading as the name of the chosen protocol + the option
    layer2_Frame.place(x=217, y=0)# Postioning

    # Ethernet Configuration
    if l == "Ethernet":
        EthDestinationLabel =  Label(layer2_Frame, text = "Ethernet Destination Mac Address:")
        dmac1 = Entry(layer2_Frame, width=4)
        dmac2 = Entry(layer2_Frame, width=4)
        dmac3 = Entry(layer2_Frame, width=4) 
        dmac4 = Entry(layer2_Frame, width=4)
        dmac5 = Entry(layer2_Frame, width=4)
        dmac6 = Entry(layer2_Frame, width=4)

        dcolon1 = Label(layer2_Frame, text = ":")
        dcolon2 = Label(layer2_Frame, text = ":")
        dcolon3 = Label(layer2_Frame, text = ":")    
        dcolon4 = Label(layer2_Frame, text = ":")
        dcolon5 = Label(layer2_Frame, text = ":")

        EthSourceLabel =  Label(layer2_Frame, text = "Ethernet Source Mac Address:")
        mac1 = Entry(layer2_Frame, width=4)
        mac2 = Entry(layer2_Frame, width=4)
        mac3 = Entry(layer2_Frame, width=4) 
        mac4 = Entry(layer2_Frame, width=4)
        mac5 = Entry(layer2_Frame, width=4)
        mac6 = Entry(layer2_Frame, width=4)

        colon1 = Label(layer2_Frame, text = ":")
        colon2 = Label(layer2_Frame, text = ":")
        colon3 = Label(layer2_Frame, text = ":")    
        colon4 = Label(layer2_Frame, text = ":")
        colon5 = Label(layer2_Frame, text = ":")

        #Postioning:
        EthDestinationLabel.place(x=4,y=1)
        dmac1.place(x=5,y=21)
        dmac2.place(x=45,y=21)
        dmac3.place(x=85,y=21)
        dmac4.place(x=125,y=21)
        dmac5.place(x=165,y=21)
        dmac6.place(x=205,y=21)

        dcolon1.place(x=35,y=21)
        dcolon2.place(x=75,y=21)
        dcolon3.place(x=115,y=21)
        dcolon4.place(x=155,y=21)
        dcolon5.place(x=195,y=21)

        EthSourceLabel.place(x=4,y=41)
        mac1.place(x=5,y=61)
        mac2.place(x=45,y=61)
        mac3.place(x=85,y=61)
        mac4.place(x=125,y=61)
        mac5.place(x=165,y=61)
        mac6.place(x=205,y=61)

        colon1.place(x=35,y=61)
        colon2.place(x=75,y=61)
        colon3.place(x=115,y=61)
        colon4.place(x=155,y=61)
        colon5.place(x=195,y=61)

        #Same methodology for each protocol, The button at the bottom saves each input into the class
        def Ethdone():
            Config.Ethernet[1] = 1
            colon = ":"
            ethernetConfig.dmac = dmac1.get() + colon + dmac2.get() + colon + dmac3.get() + colon + dmac4.get() + colon + dmac5.get() + colon + dmac6.get()
            ethernetConfig.smac = mac1.get() + colon + mac2.get() + colon + mac3.get() + colon + mac4.get() + colon + mac5.get() + colon + mac6.get()
            History_Displayer()
        ethb = Button(layer2_Frame, text = "✓", command=Ethdone)
        ethb.place(x=175, y=475, width=100) 
    

    if l == "WIFI (IEEE 802.11)":
        WifiPhyLabel = Label(layer2_Frame, text = "PHY Type: ")
        WifiPhyvar = StringVar(layer2_Frame)
        WifiPhyvar.set("PHY")
        WifiPhy = OptionMenu(layer2_Frame, WifiPhyvar, "802.11","802.11b","802.11a","802.11g","802.11n","802.11ac","802.11ax")
        WifiPhyLabel.place(x=2,y=200)
        WifiPhy.place(x=2,y=220)
        
        
        WifiMCSIndexLabel = Label(layer2_Frame, text = "MCS Index: ")
        WifiMCSIndex = Spinbox(layer2_Frame, from_=0, to= 31)
        WifiMCSIndexLabel.place(x=2,y=250)
        WifiMCSIndex.place(x=4,y=270)

        WifiFrequencyLabel = Label(layer2_Frame, text = "Frequency: (MHZ)")
        WifiFrequency = Entry(layer2_Frame, width=6) #Octect 1 of the IP
        WifiFrequencyLabel.place(x=2,y=290)
        WifiFrequency.place(x=4,y=310)

        WifiDataRateLabel = Label(layer2_Frame, text = "Data Rate: ")
        WifiDataRate = Entry(layer2_Frame, width=7) #Octect 1 of the IP
        WifiDataRateLabel.place(x=2,y=330)
        WifiDataRate.place(x=4,y=350)

        WifiChannelLabel = Label(layer2_Frame, text = "Wifi Channel: ")
        WifiChannelIndex = Spinbox(layer2_Frame, from_=0, to= 10)
        WifiChannelLabel.place(x=2,y=370)
        WifiChannelIndex.place(x=4,y=390)

        noiseLevelLabel = Label(layer2_Frame, text = "Noise Level (dBm): ")
        SignalStrengthlLabel = Label(layer2_Frame, text = "Signal Strength (dBm): ")
        SignalNoiseLabel = Label(layer2_Frame, text = "Signal Noise (dBm): ")

        WifiRecieverLabel =  Label(layer2_Frame, text = "Reciever Mac Address:")
        Rmac1 = Entry(layer2_Frame, width=4)
        Rmac2 = Entry(layer2_Frame, width=4)
        Rmac3 = Entry(layer2_Frame, width=4) 
        Rmac4 = Entry(layer2_Frame, width=4)
        Rmac5 = Entry(layer2_Frame, width=4)
        Rmac6 = Entry(layer2_Frame, width=4)

        Rcolon1 = Label(layer2_Frame, text = ":")
        Rcolon2 = Label(layer2_Frame, text = ":")
        Rcolon3 = Label(layer2_Frame, text = ":")    
        Rcolon4 = Label(layer2_Frame, text = ":")
        Rcolon5 = Label(layer2_Frame, text = ":")

        WifiTransmitterLabel =  Label(layer2_Frame, text = "Transmitter Mac Address:")
        Tmac1 = Entry(layer2_Frame, width=4)
        Tmac2 = Entry(layer2_Frame, width=4)
        Tmac3 = Entry(layer2_Frame, width=4) 
        Tmac4 = Entry(layer2_Frame, width=4)
        Tmac5 = Entry(layer2_Frame, width=4)
        Tmac6 = Entry(layer2_Frame, width=4)

        Tcolon1 = Label(layer2_Frame, text = ":")
        Tcolon2 = Label(layer2_Frame, text = ":")
        Tcolon3 = Label(layer2_Frame, text = ":")    
        Tcolon4 = Label(layer2_Frame, text = ":")
        Tcolon5 = Label(layer2_Frame, text = ":")

        WifiDestinationLabel =  Label(layer2_Frame, text = "Destination Mac Address:")
        Dmac1 = Entry(layer2_Frame, width=4)
        Dmac2 = Entry(layer2_Frame, width=4)
        Dmac3 = Entry(layer2_Frame, width=4) 
        Dmac4 = Entry(layer2_Frame, width=4)
        Dmac5 = Entry(layer2_Frame, width=4)
        Dmac6 = Entry(layer2_Frame, width=4)

        Dcolon1 = Label(layer2_Frame, text = ":")
        Dcolon2 = Label(layer2_Frame, text = ":")
        Dcolon3 = Label(layer2_Frame, text = ":")    
        Dcolon4 = Label(layer2_Frame, text = ":")
        Dcolon5 = Label(layer2_Frame, text = ":")

        WifiSourceLabel =  Label(layer2_Frame, text = "Source Mac Address:")
        Smac1 = Entry(layer2_Frame, width=4)
        Smac2 = Entry(layer2_Frame, width=4)
        Smac3 = Entry(layer2_Frame, width=4) 
        Smac4 = Entry(layer2_Frame, width=4)
        Smac5 = Entry(layer2_Frame, width=4)
        Smac6 = Entry(layer2_Frame, width=4)

        Scolon1 = Label(layer2_Frame, text = ":")
        Scolon2 = Label(layer2_Frame, text = ":")
        Scolon3 = Label(layer2_Frame, text = ":")    
        Scolon4 = Label(layer2_Frame, text = ":")
        Scolon5 = Label(layer2_Frame, text = ":")

        WifiBSSLabel =  Label(layer2_Frame, text = "BSS ID Address:")
        Bmac1 = Entry(layer2_Frame, width=4)
        Bmac2 = Entry(layer2_Frame, width=4)
        Bmac3 = Entry(layer2_Frame, width=4) 
        Bmac4 = Entry(layer2_Frame, width=4)
        Bmac5 = Entry(layer2_Frame, width=4)
        Bmac6 = Entry(layer2_Frame, width=4)

        Bcolon1 = Label(layer2_Frame, text = ":")
        Bcolon2 = Label(layer2_Frame, text = ":")
        Bcolon3 = Label(layer2_Frame, text = ":")    
        Bcolon4 = Label(layer2_Frame, text = ":")
        Bcolon5 = Label(layer2_Frame, text = ":")


        #Postioning:
        WifiRecieverLabel.place(x=4,y=1)
        Rmac1.place(x=5,y=21)
        Rmac2.place(x=45,y=21)
        Rmac3.place(x=85,y=21)
        Rmac4.place(x=125,y=21)
        Rmac5.place(x=165,y=21)
        Rmac6.place(x=205,y=21)

        Rcolon1.place(x=35,y=21)
        Rcolon2.place(x=75,y=21)
        Rcolon3.place(x=115,y=21)
        Rcolon4.place(x=155,y=21)
        Rcolon5.place(x=195,y=21)

        WifiTransmitterLabel.place(x=4,y=41)
        Tmac1.place(x=5,y=61)
        Tmac2.place(x=45,y=61)
        Tmac3.place(x=85,y=61)
        Tmac4.place(x=125,y=61)
        Tmac5.place(x=165,y=61)
        Tmac6.place(x=205,y=61)

        Tcolon1.place(x=35,y=61)
        Tcolon2.place(x=75,y=61)
        Tcolon3.place(x=115,y=61)
        Tcolon4.place(x=155,y=61)
        Tcolon5.place(x=195,y=61)


        WifiDestinationLabel.place(x=4,y=81)
        Dmac1.place(x=5,y=101)
        Dmac2.place(x=45,y=101)
        Dmac3.place(x=85,y=101)
        Dmac4.place(x=125,y=101)
        Dmac5.place(x=165,y=101)
        Dmac6.place(x=205,y=101)

        Dcolon1.place(x=35,y=101)
        Dcolon2.place(x=75,y=101)
        Dcolon3.place(x=115,y=101)
        Dcolon4.place(x=155,y=101)
        Dcolon5.place(x=195,y=101)

        WifiSourceLabel.place(x=4,y=121)
        Smac1.place(x=5,y=141)
        Smac2.place(x=45,y=141)
        Smac3.place(x=85,y=141)
        Smac4.place(x=125,y=141)
        Smac5.place(x=165,y=141)
        Smac6.place(x=205,y=141)

        Scolon1.place(x=35,y=141)
        Scolon2.place(x=75,y=141)
        Scolon3.place(x=115,y=141)
        Scolon4.place(x=155,y=141)
        Scolon5.place(x=195,y=141)

        WifiBSSLabel.place(x=4,y=161)
        Bmac1.place(x=5,y=181)
        Bmac2.place(x=45,y=181)
        Bmac3.place(x=85,y=181)
        Bmac4.place(x=125,y=181)
        Bmac5.place(x=165,y=181)
        Bmac6.place(x=205,y=181)

        Bcolon1.place(x=35,y=181)
        Bcolon2.place(x=75,y=181)
        Bcolon3.place(x=115,y=181)
        Bcolon4.place(x=155,y=181)
        Bcolon5.place(x=195,y=181)

        def wifidone():
            Config.Wifi[1] = 1
            colon = ":"
            wifiConfig.reciver = Rmac1.get() + colon + Rmac2.get() + colon + Rmac3.get() + colon + Rmac4.get() + colon + Rmac5.get() + colon + Rmac6.get()
            wifiConfig.transmitter = Tmac1.get() + colon + Tmac2.get() + colon + Tmac3.get() + colon + Tmac4.get() + colon + Tmac5.get() + colon + Tmac6.get()
            wifiConfig.destination = Dmac1.get() + colon + Dmac2.get() + colon + Dmac3.get() + colon + Dmac4.get() + colon + Dmac5.get() + colon + Dmac6.get()
            wifiConfig.source = Smac1.get() + colon + Smac2.get() + colon + Smac3.get() + colon + Smac4.get() + colon + Smac5.get() + colon + Smac6.get()
            wifiConfig.bss = Bmac1.get() + colon + Bmac2.get() + colon + Bmac3.get() + colon + Bmac4.get() + colon + Bmac5.get() + colon + Bmac6.get()
            wifiConfig.phy = WifiPhyvar.get()
            wifiConfig.mcs = WifiMCSIndex.get()
            wifiConfig.Freq = WifiFrequency.get()
            wifiConfig.DataR = WifiDataRate.get()
            wifiConfig.Channel = WifiChannelIndex.get()
            History_Displayer()
        wifib = Button(layer2_Frame, text = "✓", command=wifidone)
        wifib.place(x=175, y=475, width=100)

    if l == "ARP":
        arpSenderLabel =  Label(layer2_Frame, text = "ARP Sender Mac Address:")
        arpSmac1 = Entry(layer2_Frame, width=4)
        arpSmac2 = Entry(layer2_Frame, width=4)
        arpSmac3 = Entry(layer2_Frame, width=4) 
        arpSmac4 = Entry(layer2_Frame, width=4)
        arpSmac5 = Entry(layer2_Frame, width=4)
        arpSmac6 = Entry(layer2_Frame, width=4)

        arpScolon1 = Label(layer2_Frame, text = ":")
        arpScolon2 = Label(layer2_Frame, text = ":")
        arpScolon3 = Label(layer2_Frame, text = ":")    
        arpScolon4 = Label(layer2_Frame, text = ":")
        arpScolon5 = Label(layer2_Frame, text = ":")

        EthTargetLabel =  Label(layer2_Frame, text = "ARP Target Mac Address:")
        arpTmac1 = Entry(layer2_Frame, width=4)
        arpTmac2 = Entry(layer2_Frame, width=4)
        arpTmac3 = Entry(layer2_Frame, width=4) 
        arpTmac4 = Entry(layer2_Frame, width=4)
        arpTmac5 = Entry(layer2_Frame, width=4)
        arpTmac6 = Entry(layer2_Frame, width=4)

        arpTcolon1 = Label(layer2_Frame, text = ":")
        arpTcolon2 = Label(layer2_Frame, text = ":")
        arpTcolon3 = Label(layer2_Frame, text = ":")    
        arpTcolon4 = Label(layer2_Frame, text = ":")
        arpTcolon5 = Label(layer2_Frame, text = ":")

        #Postioning:
        arpSenderLabel.place(x=4,y=1)
        arpSmac1.place(x=5,y=21)
        arpSmac2.place(x=45,y=21)
        arpSmac3.place(x=85,y=21)
        arpSmac4.place(x=125,y=21)
        arpSmac5.place(x=165,y=21)
        arpSmac6.place(x=205,y=21)

        arpScolon1.place(x=35,y=21)
        arpScolon2.place(x=75,y=21)
        arpScolon3.place(x=115,y=21)
        arpScolon4.place(x=155,y=21)
        arpScolon5.place(x=195,y=21)

        EthTargetLabel.place(x=4,y=41)
        arpTmac1.place(x=5,y=61)
        arpTmac2.place(x=45,y=61)
        arpTmac3.place(x=85,y=61)
        arpTmac4.place(x=125,y=61)
        arpTmac5.place(x=165,y=61)
        arpTmac6.place(x=205,y=61)

        arpTcolon1.place(x=35,y=61)
        arpTcolon2.place(x=75,y=61)
        arpTcolon3.place(x=115,y=61)
        arpTcolon4.place(x=155,y=61)
        arpTcolon5.place(x=195,y=61)


        arpTargetIPLabel = Label(layer2_Frame, text="Target IP Address: ")
        arpTargetIPLabel.place(x=1,y=81)
        arpTip1 = Entry(layer2_Frame, width=3) #Octect 1 of the IP
        arpTip2 = Entry(layer2_Frame, width=3) #Octect 2 of the ip 
        arpTip3 = Entry(layer2_Frame, width=3) #Octect 3 of the ip 
        arpTip4 = Entry(layer2_Frame, width=3) #Octect 4 of the ip 
        arpTdot1 = Label(layer2_Frame, text = ".") # Three dots seperating the fields
        arpTdot2 = Label(layer2_Frame, text = ".")
        arpTdot3 = Label(layer2_Frame, text = ".")
        arpTip1.place(x=6,y=101)     
        arpTip2.place(x=46,y=101)
        arpTip3.place(x=86,y=101)
        arpTip4.place(x=126,y=101)
        arpTdot1.place(x=31,y=101)
        arpTdot2.place(x=71,y=101)
        arpTdot3.place(x=111,y=101)

        arpSourceIPLabel = Label(layer2_Frame, text="Source IP Address: ")
        arpSourceIPLabel.place(x=1,y=121)
        arpSip1 = Entry(layer2_Frame, width=3) #Octect 1 of the IP
        arpSip2 = Entry(layer2_Frame, width=3) #Octect 2 of the ip 
        arpSip3 = Entry(layer2_Frame, width=3) #Octect 3 of the ip 
        arpSip4 = Entry(layer2_Frame, width=3) #Octect 4 of the ip 
        arpSdot1 = Label(layer2_Frame, text = ".") # Three dots seperating the fields
        arpSdot2 = Label(layer2_Frame, text = ".")
        arpSdot3 = Label(layer2_Frame, text = ".")
        arpSip1.place(x=6,y=141)     
        arpSip2.place(x=46,y=141)
        arpSip3.place(x=86,y=141)
        arpSip4.place(x=126,y=141)
        arpSdot1.place(x=31,y=141)
        arpSdot2.place(x=71,y=141)
        arpSdot3.place(x=111,y=141)


        def arpdone():
            Config.ARP[1] = 1
            colon = ":"
            dot = "."
            arpConfig.sendermac = arpSmac1.get() + colon + arpSmac2.get() + colon + arpSmac3.get() + colon + arpSmac4.get() + colon + arpSmac5.get() + colon + arpSmac6.get()
            arpConfig.targetmac = arpTmac1.get() + colon + arpTmac2.get() + colon + arpTmac3.get() + colon + arpTmac4.get() + colon + arpTmac5.get() + colon + arpTmac6.get()
            arpConfig.senderip = arpSip1.get() + dot + arpSip2.get() + dot + arpSip3.get() + dot + arpSip4.get()
            arpConfig.targetip = arpTip1.get() + dot + arpTip2.get() + dot + arpTip3.get() + dot + arpTip4.get()
            History_Displayer()

        arpb = Button(layer2_Frame, text = "✓", command=arpdone)
        arpb.place(x=175, y=475, width=100) # postioning on the button

#layer 3 
def layer3_Displayer(l):
    #Defining the tkinter type
    layer3_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration", width=284, height=529)    # Using .place geomotry manager under the label frame in order to position correctly
    layer3_Frame.place(x=217, y=0)
    #Button that links the previous function. 
    if l == "ICMP":
         # defining the ip octect entires
        ip1 = Entry(layer3_Frame, width=2) #Octect 1 of the IP
        ip2 = Entry(layer3_Frame, width=2) #Octect 2 of the ip 
        ip3 = Entry(layer3_Frame, width=2) #Octect 3 of the ip 
        ip4 = Entry(layer3_Frame, width=2) #Octect 4 of the ip 
        dot1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        dot2 = Label(layer3_Frame, text = ".")
        dot3 = Label(layer3_Frame, text = ".")

        #Destination Ip
        ip5 = Entry(layer3_Frame, width=2) #Octect 1 of the IP
        ip6 = Entry(layer3_Frame, width=2) #Octect 2 of the ip 
        ip7 = Entry(layer3_Frame, width=2) #Octect 3 of the ip 
        ip8 = Entry(layer3_Frame, width=2) #Octect 4 of the ip 
        dot4 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        dot5 = Label(layer3_Frame, text = ".")
        dot6 = Label(layer3_Frame, text = ".")

        # Defining the mac octect Entries
        #Source mac
        mac1 = Entry(layer3_Frame, width=3)
        mac2 = Entry(layer3_Frame, width=3)
        mac3 = Entry(layer3_Frame, width=3) 
        mac4 = Entry(layer3_Frame, width=3)
        mac5 = Entry(layer3_Frame, width=3)
        mac6 = Entry(layer3_Frame, width=3)

        #Destination Mac
        mac7 = Entry(layer3_Frame, width=3)
        mac8 = Entry(layer3_Frame, width=3)
        mac9 = Entry(layer3_Frame, width=3) 
        mac10 = Entry(layer3_Frame, width=3)
        mac11 = Entry(layer3_Frame, width=3)
        mac12 = Entry(layer3_Frame, width=3)

        # The colons seperate the label
        colon1 = Label(layer3_Frame, text = ":")
        colon2 = Label(layer3_Frame, text = ":")
        colon3 = Label(layer3_Frame, text = ":")    
        colon4 = Label(layer3_Frame, text = ":")
        colon5 = Label(layer3_Frame, text = ":")

        colon6 = Label(layer3_Frame, text = ":")
        colon7 = Label(layer3_Frame, text = ":")
        colon8 = Label(layer3_Frame, text = ":")    
        colon9 = Label(layer3_Frame, text = ":")
        colon10 = Label(layer3_Frame, text = ":")   

        #Defining the text (like literally the words that say "IP:")
        iptext = Label(layer3_Frame, text = "Source IP:")
        mactext = Label(layer3_Frame, text = "Source MAC:")
        diptext = Label(layer3_Frame, text = "Destination IP:")
        dmactext = Label(layer3_Frame, text = "Destination MAC:")

        #source Ip text postioning
        iptext.place(x=2,y=4) 
        #source mac text postioning
        mactext.place(x=2,y=34) 
        #desitination ip text postioning
        diptext.place(x=2,y=64)
        #desitination mac text postioning
        dmactext.place(x=2,y=94)


        #Placing all of the previously defined labels. using .place for more accurate location (This does take a while to do tho)
        ip1.place(x=65,y=5)     
        ip2.place(x=95,y=5)
        ip3.place(x=125,y=5)
        ip4.place(x=155,y=5)

        dot1.place(x=85,y=5)
        dot2.place(x=115,y=5)
        dot3.place(x=145,y=5)

        ip5.place(x=90,y=65)     
        ip6.place(x=120,y=65)
        ip7.place(x=150,y=65)
        ip8.place(x=180,y=65)

        dot4.place(x=110,y=65)
        dot5.place(x=140,y=65)
        dot6.place(x=170,y=65)

        mac1.place(x=80,y=35)   
        mac2.place(x=110,y=35)
        mac3.place(x=140,y=35)
        mac4.place(x=170,y=35)
        mac5.place(x=200,y=35)
        mac6.place(x=230,y=35)

        colon1.place(x=100,y=35)
        colon2.place(x=130,y=35)
        colon3.place(x=160,y=35)
        colon4.place(x=190,y=35)
        colon5.place(x=220,y=35)

        mac7.place(x=105,y=95)   
        mac8.place(x=135,y=95)
        mac9.place(x=165,y=95)
        mac10.place(x=195,y=95)
        mac11.place(x=225,y=95)
        mac12.place(x=255,y=95)

        colon6.place(x=125,y=95)
        colon7.place(x=155,y=95)
        colon8.place(x=185,y=95)
        colon9.place(x=215,y=95)
        colon10.place(x=245,y=95)
        icmpPingData = Label(layer3_Frame, text="ICMP Ping Data:")
        icmpText = Text(layer3_Frame, height=10, width=33)
        icmpText.place(x=5, y=140)
        icmpPingData.place(x=5, y=120)
        def icmpdone():
                icmpConfig.ip = ""
                icmpConfig.mac = ""
                colon = ":"
                dot = "."
                ip = ip1.get() + dot + ip2.get() + dot + ip3.get() + dot + ip4.get() # concatating all of the octects
                mac = mac1.get() + colon + mac2.get() + colon + mac3.get() + colon + mac4.get() + colon + mac5.get() + colon + mac6.get()
                dip = ip5.get() + dot + ip6.get() + dot + ip7.get() + dot + ip8.get()
                dmac = mac7.get() + colon + mac8.get() + colon + mac9.get() + colon + mac10.get() + colon + mac11.get() + colon + mac12.get()
                icmpConfig.ip = ip
                icmpConfig.mac = mac
                icmpConfig.dip = dip
                icmpConfig.dmac = dmac
                print(icmpConfig.dmac)
                icmpConfig.Text = icmpText.get(1.0,255.0)
                Config.ICMP[1] = 1
                History_Displayer()
        icmpb = Button(layer3_Frame, text = "✓", command=icmpdone,)
        icmpb.place(x=175, y=475, width=100) # postioning on the button

    if l == "IP":
        IPLabel = Label(layer3_Frame, text = "IP Traffic is considered Default." )
        IPLabel2 = Label(layer3_Frame, text = "All IP Protcols will use this as default config" )
        IPLabel.place(x=1,y=1)
        IPLabel2.place(x=1,y=21)

        IPLabel = Label(layer3_Frame, text = "Source Ip Address: ")
        IPip1 = Entry(layer3_Frame, width=2) #Octect 1 of the IP
        IPip2 = Entry(layer3_Frame, width=2) #Octect 2 of the ip 
        IPip3 = Entry(layer3_Frame, width=2) #Octect 3 of the ip 
        IPip4 = Entry(layer3_Frame, width=2) #Octect 4 of the ip 

        IPdot1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        IPdot2 = Label(layer3_Frame, text = ".")
        IPdot3 = Label(layer3_Frame, text = ".")

        IPDIPLabel = Label(layer3_Frame, text = "Destination Ip Address: ")
        IPdip1 = Entry(layer3_Frame, width=2) #Octect 1 of the IP
        IPdip2 = Entry(layer3_Frame, width=2) #Octect 2 of the ip 
        IPdip3 = Entry(layer3_Frame, width=2) #Octect 3 of the ip 
        IPdip4 = Entry(layer3_Frame, width=2) #Octect 4 of the ip 

        IPddot1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        IPddot2 = Label(layer3_Frame, text = ".")
        IPddot3 = Label(layer3_Frame, text = ".")


        IPLabel.place(x=1,y=45)
        IPip1.place(x=4,y=65)     
        IPip2.place(x=34,y=65)
        IPip3.place(x=64,y=65)
        IPip4.place(x=94,y=65)
        IPdot1.place(x=19,y=65)
        IPdot2.place(x=49,y=65)
        IPdot3.place(x=79,y=65)

        IPDIPLabel.place(x=1,y=85)
        IPdip1.place(x=4,y=105)     
        IPdip2.place(x=34,y=105)
        IPdip3.place(x=64,y=105)
        IPdip4.place(x=94,y=105)

        IPddot1.place(x=19,y=105)
        IPddot2.place(x=49,y=105)
        IPddot3.place(x=79,y=105)

        IPTILLabel = Label(layer3_Frame, text = "Default Time to Live: ")
        IPTILEntry = Entry(layer3_Frame, width=4) 
        IPTILLabel.place(x=1,y=135)
        IPTILEntry.place(x=4,y=155)

        def IPdone():
            Config.IP[1] = 1
            dot = "."
            ipConfig.destinationIp = IPdip1.get() + dot + IPdip2.get() + dot + IPdip3.get() + dot + IPdip4.get()
            ipConfig.sourceIp = IPip1.get() + dot + IPip2.get() + dot + IPip3.get() + dot + IPip4.get()
            ipConfig.TIL = IPTILEntry.get()
            #Setting other Protocols:
            #ospf
            ospfConfig.dip = ipConfig.destinationIp
            ospfConfig.sourcerouter = ipConfig.sourceIp
            ospfConfig.TIL = ipConfig.TIL
            #ICMP
            icmpConfig.dip = ipConfig.destinationIp
            icmpConfig.ip = ipConfig.sourceIp
            History_Displayer()
        ipb = Button(layer3_Frame, text = "✓", command=IPdone)
        ipb.place(x=175, y=475, width=100) 
        
    if l == "RIP":
        ripCommandLabel = Label(layer3_Frame, text="RIP Response Paramters: ")
        ripCommandvar = StringVar(layer3_Frame)
        ripCommandvar.set("RIP Verison")
        ripCommand = OptionMenu(layer3_Frame, ripCommandvar, "RIPv1" ,"RIPv2")
        ripCommand.place(x=2,y=21)
        ripCommandLabel.place(x=2,y=1)

        ripRepIPLabel = Label(layer3_Frame, text="RIP Response IP: ")
        ripRepIPLabel.place(x=2,y=51)
        ripRepip1 = Entry(layer3_Frame, width=3) #Octect 1 of the IP
        ripRepip2 = Entry(layer3_Frame, width=3) #Octect 2 of the ip 
        ripRepip3 = Entry(layer3_Frame, width=3) #Octect 3 of the ip 
        ripRepip4 = Entry(layer3_Frame, width=3) #Octect 4 of the ip 
        ripRepdot1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        ripRepdot2 = Label(layer3_Frame, text = ".")
        ripRepdot3 = Label(layer3_Frame, text = ".")
        ripRepip1.place(x=6,y=76)     
        ripRepip2.place(x=46,y=76)
        ripRepip3.place(x=86,y=76)
        ripRepip4.place(x=126,y=76)
        ripRepdot1.place(x=31,y=76)
        ripRepdot2.place(x=71,y=76)
        ripRepdot3.place(x=111,y=76)

        def ripdone():
            Config.RIP[1] = 1
            dot = "."
            ripConfig.ResponseIP = ripRepip1.get() + dot + ripRepip2.get() + ripRepip3.get() + dot + ripRepip4.get() 
            ripConfig.RipVer = ripCommandvar.get()
            History_Displayer()
        ripb = Button(layer3_Frame, text = "✓", command=ripdone,)
        ripb.place(x=175, y=475, width=100) # postioning on the button

    if l == "OSPF":
        ospfSourceRouter = Label(layer3_Frame, text="OSPF Source router: ")
        ospfSourceRouter.place(x=2,y=1)
        ospfSip1 = Entry(layer3_Frame, width=3) #Octect 1 of the IP
        ospfSip2 = Entry(layer3_Frame, width=3) #Octect 2 of the ip 
        ospfSip3 = Entry(layer3_Frame, width=3) #Octect 3 of the ip 
        ospfSip4 = Entry(layer3_Frame, width=3) #Octect 4 of the ip 
        ospfSdot1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        ospfSdot2 = Label(layer3_Frame, text = ".")
        ospfSdot3 = Label(layer3_Frame, text = ".")
        ospfSip1.place(x=6,y=26)     
        ospfSip2.place(x=46,y=26)
        ospfSip3.place(x=86,y=26)
        ospfSip4.place(x=126,y=26)
        ospfSdot1.place(x=31,y=26)
        ospfSdot2.place(x=71,y=26)
        ospfSdot3.place(x=111,y=26)

        ospfMaskText = Label(layer3_Frame, text="OSPF Network Mask:")
        ospfMaskText.place(x=2,y=145)
        ospfMaskip1 = Entry(layer3_Frame, width=4) #Octect 1 of the IP
        ospfMaskip2 = Entry(layer3_Frame, width=4) #Octect 2 of the ip 
        ospfMaskip3 = Entry(layer3_Frame, width=4) #Octect 3 of the ip 
        ospfMaskip4 = Entry(layer3_Frame, width=4) #Octect 4 of the ip 
        ospfMask1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        ospfMask2 = Label(layer3_Frame, text = ".")
        ospfMask3 = Label(layer3_Frame, text = ".")
        ospfMaskip1.place(x=4,y=165)     
        ospfMaskip2.place(x=44,y=165)
        ospfMaskip3.place(x=84,y=165)
        ospfMaskip4.place(x=124,y=165)
        ospfMask1.place(x=34,y=165)
        ospfMask2.place(x=74,y=165)
        ospfMask3.place(x=114,y=165)

        ospfMessageLabel = Label(layer3_Frame, text = "OSPF Message Type: ")
        ospfMessagevar = StringVar(layer3_Frame)
        ospfMessagevar.set("Message Type")
        ospfMessageAuth = OptionMenu(layer3_Frame, ospfMessagevar, "Hello Packet", "Database Description", "Link-State Request", "Link-State Update", "Link-State Acknowledgement")
        ospfMessageAuth.place(x=2,y=111)
        ospfMessageLabel.place(x=2,y=91)

        ospfBackRouter = Label(layer3_Frame, text="OSPF Backup router IP: ")
        ospfBackRouter.place(x=2,y=46)
        ospfBip1 = Entry(layer3_Frame, width=3) #Octect 1 of the IP
        ospfBip2 = Entry(layer3_Frame, width=3) #Octect 2 of the ip 
        ospfBip3 = Entry(layer3_Frame, width=3) #Octect 3 of the ip 
        ospfBip4 = Entry(layer3_Frame, width=3) #Octect 4 of the ip 
        ospfBdot1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
        ospfBdot2 = Label(layer3_Frame, text = ".")
        ospfBdot3 = Label(layer3_Frame, text = ".")
        ospfBip1.place(x=6,y=71)     
        ospfBip2.place(x=46,y=71)
        ospfBip3.place(x=86,y=71)
        ospfBip4.place(x=126,y=71)
        ospfBdot1.place(x=31,y=71)
        ospfBdot2.place(x=71,y=71)
        ospfBdot3.place(x=111,y=71)

        def ospfdone():
            Config.OSPF[1] = 1
            dot = "."
            ospfConfig.sourcerouter = ospfSip1.get() + dot + ospfSip2.get() + dot + ospfSip3.get() + dot + ospfSip4.get() 
            ospfConfig.backuprouter = ospfBip1.get() + dot + ospfBip2.get() + dot + ospfBip3.get() + dot + ospfBip4.get() 
            ospfConfig.message = ospfMessagevar.get()
            ospfConfig.mask = ospfMaskip1.get() + dot + ospfMaskip2.get() + dot + ospfMaskip3.get() + dot + ospfMaskip4.get()
            History_Displayer()
        ospfb = Button(layer3_Frame, text = "✓", command=ospfdone,)
        ospfb.place(x=175, y=475, width=100) # postioning on the button

        

def layer4_Displayer(l):
    layer4_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration",width=284, height=529)
    layer4_Frame.place(x=217, y=0)

    if l == "UDP":
        UDPLabel = Label(layer4_Frame, text = "UDP Traffic is considered Default." )
        UDPLabel2 = Label(layer4_Frame, text = "All UDP Protcols will use this as default config" )
        UDPLabel.place(x=1,y=1)
        UDPLabel2.place(x=1,y=21)

        UDPIPLabel = Label(layer4_Frame, text = "Source Ip Address: ")
        udpip1 = Entry(layer4_Frame, width=2) #Octect 1 of the IP
        udpip2 = Entry(layer4_Frame, width=2) #Octect 2 of the ip 
        udpip3 = Entry(layer4_Frame, width=2) #Octect 3 of the ip 
        udpip4 = Entry(layer4_Frame, width=2) #Octect 4 of the ip 

        udpdot1 = Label(layer4_Frame, text = ".") # Three dots seperating the fields
        udpdot2 = Label(layer4_Frame, text = ".")
        udpdot3 = Label(layer4_Frame, text = ".")

        UDPDIPLabel = Label(layer4_Frame, text = "Destination Ip Address: ")
        udpdip1 = Entry(layer4_Frame, width=2) #Octect 1 of the IP
        udpdip2 = Entry(layer4_Frame, width=2) #Octect 2 of the ip 
        udpdip3 = Entry(layer4_Frame, width=2) #Octect 3 of the ip 
        udpdip4 = Entry(layer4_Frame, width=2) #Octect 4 of the ip 

        udpddot1 = Label(layer4_Frame, text = ".") # Three dots seperating the fields
        udpddot2 = Label(layer4_Frame, text = ".")
        udpddot3 = Label(layer4_Frame, text = ".")

        UDPPortLabel = Label(layer4_Frame, text = "Destination Port: ")
        udpPort = Entry(layer4_Frame, width=4) #Octect 4 of the ip 

        UDPSPortLabel = Label(layer4_Frame, text = "Source Port: ")
        udpSPort = Entry(layer4_Frame, width=4) #Octect 4 of the ip 

        UDPIPLabel.place(x=1,y=70)
        udpip1.place(x=105,y=70)     
        udpip2.place(x=135,y=70)
        udpip3.place(x=165,y=70)
        udpip4.place(x=195,y=70)
        udpdot1.place(x=125,y=70)
        udpdot2.place(x=155,y=70)
        udpdot3.place(x=185,y=70)

        UDPDIPLabel.place(x=1,y=135)
        udpdip1.place(x=4,y=155)     
        udpdip2.place(x=34,y=155)
        udpdip3.place(x=64,y=155)
        udpdip4.place(x=94,y=155)

        udpddot1.place(x=20,y=155)
        udpddot2.place(x=50,y=155)
        udpddot3.place(x=80,y=155)

        #Source Label
        UDPSPortLabel.place(x=1,y=40)
        #Destination Label
        UDPPortLabel.place(x=1,y=98)

        #Source port
        udpSPort.place(x=70,y=40)
        #Destination Port
        udpPort.place(x=4,y=118)

        def udpdone():
            Config.UDP[1] = 1
            dot = "."
            udpConfig.port = udpSPort.get()
            udpConfig.dport = udpPort.get()
            udpConfig.ip = udpip1.get() + dot + udpip2.get() + dot + udpip3.get() + dot + udpip4.get()
            udpConfig.dip = udpdip1.get() + dot + udpdip2.get() + dot + udpdip3.get() + dot + udpdip4.get()
            History_Displayer()
            #Setting UDP Protocol:
            #RIP
            ripConfig.ip = udpConfig.ip
            ripConfig.port = udpConfig.port
            ripConfig.dport = udpConfig.dport
            #smb
            smbConfig.sport = udpConfig.port
            smbConfig.ip = udpConfig.ip
            smbConfig.dip = udpConfig.dip
            #dhcp
            dhcpConfig.dip = udpConfig.dip
            dhcpConfig.ip = udpConfig.ip
            #dns
            dnsConfig.ip = udpConfig.ip
            dnsConfig.dip = udpConfig.dip
        udpb = Button(layer4_Frame, text = "✓", command=udpdone)
        udpb.place(x=175, y=475, width=100) 


    if l == "TCP":
        tcpLabel = Label(layer4_Frame, text = "TCP Traffic is considered Default." )
        tcpLabel2 = Label(layer4_Frame, text = "All TCP Protcols will use this as default config" )
        tcpLabel.place(x=1,y=1)
        tcpLabel2.place(x=1,y=21)

        tcpIPLabel = Label(layer4_Frame, text = "Source Ip Address: ")
        tcpip1 = Entry(layer4_Frame, width=2) #Octect 1 of the IP
        tcpip2 = Entry(layer4_Frame, width=2) #Octect 2 of the ip 
        tcpip3 = Entry(layer4_Frame, width=2) #Octect 3 of the ip 
        tcpip4 = Entry(layer4_Frame, width=2) #Octect 4 of the ip 

        tcpdot1 = Label(layer4_Frame, text = ".") # Three dots seperating the fields
        tcpdot2 = Label(layer4_Frame, text = ".")
        tcpdot3 = Label(layer4_Frame, text = ".")

        tcpDIPLabel = Label(layer4_Frame, text = "Destination Ip Address: ")
        tcpdip1 = Entry(layer4_Frame, width=2) #Octect 1 of the IP
        tcpdip2 = Entry(layer4_Frame, width=2) #Octect 2 of the ip 
        tcpdip3 = Entry(layer4_Frame, width=2) #Octect 3 of the ip 
        tcpdip4 = Entry(layer4_Frame, width=2) #Octect 4 of the ip 

        tcpddot1 = Label(layer4_Frame, text = ".") # Three dots seperating the fields
        tcpddot2 = Label(layer4_Frame, text = ".")
        tcpddot3 = Label(layer4_Frame, text = ".")

        tcpPortLabel = Label(layer4_Frame, text = "Destination Port: ")
        tcpPort = Entry(layer4_Frame, width=4) #Octect 4 of the ip 

        tcpSPortLabel = Label(layer4_Frame, text = "Source Port: ")
        tcpSPort = Entry(layer4_Frame, width=4) #Octect 4 of the ip 

        tcpIPLabel.place(x=1,y=70)
        tcpip1.place(x=105,y=70)     
        tcpip2.place(x=135,y=70)
        tcpip3.place(x=165,y=70)
        tcpip4.place(x=195,y=70)
        tcpdot1.place(x=125,y=70)
        tcpdot2.place(x=155,y=70)
        tcpdot3.place(x=185,y=70)

        tcpDIPLabel.place(x=1,y=135)
        tcpdip1.place(x=4,y=155)     
        tcpdip2.place(x=34,y=155)
        tcpdip3.place(x=64,y=155)
        tcpdip4.place(x=94,y=155)

        tcpddot1.place(x=20,y=155)
        tcpddot2.place(x=50,y=155)
        tcpddot3.place(x=80,y=155)

        #Source Label
        tcpSPortLabel.place(x=1,y=40)
        #Destination Label
        tcpPortLabel.place(x=1,y=98)

        #Source port
        tcpSPort.place(x=70,y=40)
        #Destination Port
        tcpPort.place(x=4,y=118)

        tcpWindowLabel = Label(layer4_Frame, text = "TCP Windowing Size: ")
        tcpWindow = Entry(layer4_Frame, width=4) #Octect 4 of the ip 
        tcpWindowLabel.place(x=2,y=180)
        tcpWindow.place(x=4,y=200)

        tcppaddinglabel = Label(layer4_Frame, text = "TCP Padding Size: ")
        tcppadding = Entry(layer4_Frame, width=4) #Octect 4 of the ip 
        tcppaddinglabel.place(x=2,y=220)
        tcppadding.place(x=4,y=240)

        def tcpdone():
            Config.TCP[1] = 1
            dot = "."
            tcpConfig.port = tcpSPort.get()
            tcpConfig.dport = tcpPort.get()
            tcpConfig.ip = tcpip1.get() + dot + tcpip2.get() + dot + tcpip3.get() + dot + tcpip4.get()
            tcpConfig.window = tcpWindow.get()
            tcpConfig.padding= tcppadding.get()
            tcpConfig.dip = tcpdip1.get() + dot + tcpdip2.get() + dot + tcpdip3.get() + dot + tcpdip4.get()
            #Setting other protocols:
            #netBios
            History_Displayer()
            netbiosConfig.port = tcpConfig.port
            netbiosConfig.dip = tcpConfig.dip
            netbiosConfig.ip = tcpConfig.ip
            netbiosConfig.window = tcpConfig.window
            netbiosConfig.padding = tcpConfig.padding
            #telnet
            telnetConfig.dport = tcpConfig.dport
            telnetConfig.ip = tcpConfig.ip
            telnetConfig.dip = tcpConfig.dip
            telnetConfig.window = tcpConfig.window
            telnetConfig.padding = tcpConfig.padding
            telnetConfig.port = tcpConfig.port
            #irc
            ircConfig.ip = tcpConfig.ip
            ircConfig.dip = tcpConfig.dip
            ircConfig.window = tcpConfig.window
            ircConfig.padding = tcpConfig.padding
            #ftp    
            ftpConfig.ip = tcpConfig.ip
            ftpConfig.dip = tcpConfig.dip
            ftpConfig.window = tcpConfig.window
            ftpConfig.padding = tcpConfig.padding
            #http
            httpConfig.ip = tcpConfig.ip
            httpConfig.dip = tcpConfig.dip
            httpConfig.window = tcpConfig.window
            httpConfig.padding = tcpConfig.padding
            httpConfig.port = tcpConfig.port
            #https
            httpsConfig.ip = tcpConfig.ip
            httpsConfig.dip = tcpConfig.dip
            httpsConfig.window = tcpConfig.window
            httpsConfig.padding = tcpConfig.padding
            httpsConfig.port = ""

        tcpb = Button(layer4_Frame, text = "✓", command=tcpdone)
        tcpb.place(x=175, y=475, width=100) 

def layer5_Displayer(l):
    layer5_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration",width=284, height=529)
    layer5_Frame.place(x=217, y=0)
    
    if l == "SOCKS":
        sockLabel = Label(layer5_Frame, text = "SOCKS Proxy Configuration:")
        sockvar = StringVar(layer5_Frame)
        sockvar.set("Name Service")
        sockOption = OptionMenu(layer5_Frame, sockvar, "Stream Connection", "Port Binding", "UDP Port")
        sockLabel.place(x=2,y=2)
        sockOption.place(x=2,y=20)

        sockProxyLabel = Label(layer5_Frame, text="SOCKS  Proxy IP:")
        sockProxyLabel.place(x=1,y=55)
        sockProxyip1 = Entry(layer5_Frame, width=2) #Octect 1 of the IP
        sockProxyip2 = Entry(layer5_Frame, width=2) #Octect 2 of the ip 
        sockProxyip3 = Entry(layer5_Frame, width=2) #Octect 3 of the ip 
        sockProxyip4 = Entry(layer5_Frame, width=2) #Octect 4 of the ip 
        dot1 = Label(layer5_Frame, text = ".") # Three dots seperating the fields
        dot2 = Label(layer5_Frame, text = ".")
        dot3 = Label(layer5_Frame, text = ".")
        sockProxyip1.place(x=105,y=55)     
        sockProxyip2.place(x=135,y=55)
        sockProxyip3.place(x=165,y=55)
        sockProxyip4.place(x=195,y=55)
        dot1.place(x=125,y=55)
        dot2.place(x=155,y=55)
        dot3.place(x=185,y=55)

        sockProxyPortLabel = Label(layer5_Frame, text="SOCKS  Port IP:")
        sockProxyPortLabel.place(x=1,y=85)
        sockProxyPort = Entry(layer5_Frame, width=4)
        sockProxyPort.place(x=90,y=85)


        sockIDLabel = Label(layer5_Frame, text="SOCKS User Identification")
        sockIDLabel.place(x=1,y=115)
        sockID = Entry(layer5_Frame, width=20)
        sockID.place(x=1,y=135)

        sockAuthLabel = Label(layer5_Frame, text = "NetBios Name Service:")
        sockAuthvar = StringVar(layer5_Frame)
        sockAuthvar.set("Name Service")
        sockAuth = OptionMenu(layer5_Frame, sockAuthvar, "No Auth", "GSSAPI", "User/Pass", "IANA")
        sockAuth.place(x=2,y=175)
        sockAuthLabel.place(x=2,y=155)

        def sockdone():
            Config.SOCKS[1] = 1
            dot = "."
            socksConfig.DPort = sockProxyPort.get()
            socksConfig.Auth = sockAuthvar.get()
            socksConfig.ID = sockID.get()
            socksConfig.Config = sockvar.get()
            socksConfig.DIP = sockProxyip1.get() + dot + sockProxyip2.get() + dot + sockProxyip3.get() + dot + sockProxyip4.get()
            History_Displayer()
        sockb = Button(layer5_Frame, text = "✓", command=sockdone)
        sockb.place(x=175, y=475, width=100) 

    if l == "NetBIOS":
        netNameLabel = Label(layer5_Frame, text = "NetBios Name Service:")
        netNamevar = StringVar(layer5_Frame)
        netNamevar.set("Name Service")
        netName = OptionMenu(layer5_Frame, netNamevar, "Add name", "Add Group Name", "Delete Name", "Find Name")
        netName.place(x=2,y=17)
        netNameLabel.place(x=2,y=2)

        netdatagramLabel = Label(layer5_Frame, text = "NetBios Datagram Parameters:")
        netDatavar = StringVar(layer5_Frame)
        netDatavar.set("Datagram Parameters")
        netData = OptionMenu(layer5_Frame, netDatavar, "Send Datagram", "Send Broadcast Datagram", "Recieve Datagram", "Receive Broadcast Datagram")
        netdatagramLabel.place(x=2,y=45)
        netData.place(x=2,y=65)


        netsessionLabel = Label(layer5_Frame, text = "NetBios Session Parameters:")
        netSessionvar = StringVar(layer5_Frame)
        netSessionvar.set("Session Parameters")
        netSession = OptionMenu(layer5_Frame, netSessionvar, "Call", "Listen", "Hang up", "Send", "Send No Ack", "Recieve")
        netsessionLabel.place(x=2,y=95)
        netSession.place(x=2,y=115)

        netNameEntryLabel = Label(layer5_Frame, text = "NetBios Name:")
        netNameEntry = Entry(layer5_Frame, width=10)
        netNameEntry.place(x=2,y=165)
        netNameEntryLabel.place(x=2,y=145)

        netGroupEntryLabel = Label(layer5_Frame, text = "NetBios Group Name:")
        netGroupEntry = Entry(layer5_Frame, width=10)
        netGroupEntry.place(x=2,y=205)
        netGroupEntryLabel.place(x=2,y=185)

        def netdone():
            Config.NetBIOS[1] = 1
            netbiosConfig.Name = netNameEntry.get()
            netbiosConfig.gName = netGroupEntry.get()
            netbiosConfig.Session = netSessionvar.get()
            netbiosConfig.Datagram = netDatavar.get()
            History_Displayer()
        tlsb = Button(layer5_Frame, text = "✓", command=netdone)
        tlsb.place(x=175, y=475, width=100) 
    
    if l == "SMB":
        #https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/69a29f73-de0c-45a6-a1aa-8ceeea42217f
        smb_IpLabel =  Label(layer5_Frame, text = "SMB Implementation:" )
        smb_IpLabel.place(x=2,y=5)

        smbImpelmentationvar = StringVar(layer5_Frame)
        smbImpelmentationvar.set("Implementation")
        smbImpelmentation = OptionMenu(layer5_Frame, smbImpelmentationvar, "Samba", "Netsmb", "NQ", "MoSMB", "Tuxera SMB", "Likewise", "CIFSD")
        smbImpelmentation.place(x=2,y=25)
    
        smbCommandLabel =  Label(layer5_Frame, text = "SMB Command:" )
        smbCommandvar= StringVar(layer5_Frame)
        smbCommandvar.set("Command")
        smbCommand = OptionMenu(layer5_Frame, smbCommandvar,  "SMBmkdir", "SMBrmdir","SMBopen","SMBcreate","SMBclose", "SMBflush","SMBclose","SMBflush","SMBunlink",)
        smbCommandLabel.place(x=2,y=55)
        smbCommand.place(x=2,y=75)
        
        smbCidLabel =  Label(layer5_Frame, text = "SMB Connection Identifier:" )
        smbCid = Entry(layer5_Frame, width=15)
        smbCidLabel.place(x=2,y=105)
        smbCid.place(x=4,y=125)

        def smbdone():
            Config.SMB[1] = 1
            smbConfig.implementation = smbImpelmentationvar.get()
            smbConfig.cid = smbCid.get()
            smbConfig.command = smbCommandvar.get()
            History_Displayer()
        smbb = Button(layer5_Frame, text = "✓", command=smbdone)
        smbb.place(x=175, y=475, width=100) 


def layer6_Displayer(l):    
    layer6_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration",width=284, height=529)
    layer6_Frame.place(x=217, y=0)

    if l == "TLS/SSL":
        tlsLabel = Label(layer6_Frame, text = "TLS (WIP): ")
        layer7label = Label(layer6_Frame, text = "Enabling TLS will directly affect all traffic (WIP) ",)
        tlsLabel.place(x=2,y=25)
        layer7label.place(x=2,y=1)

        tlsLabel = Label(layer6_Frame, text = "TLS Encryption Cipher Suite: ")
        tlsLabel.place(x=2,y=45)
        
        tlsExchangeVar = StringVar(layer6_Frame)
        tlsExchangeVar.set("Key Exchange")
        tlsExchange = OptionMenu(layer6_Frame, tlsExchangeVar, "RSA", "Diffie-Hellmen", "ECDH", "SRP", "PSK")
        tlsExchange.place(x=2,y=65)

        tlsAuthVar = StringVar(layer6_Frame)
        tlsAuthVar.set("Authentication")
        tlsAuth = OptionMenu(layer6_Frame, tlsAuthVar, "RSA", "DSA", "ECDSA")
        tlsAuth.place(x=2,y=95)

        tlsCipherVar = StringVar(layer6_Frame)
        tlsCipherVar.set("Cipher")
        tlsCipher = OptionMenu(layer6_Frame, tlsCipherVar, "RC4", "Triple DES", "AES", "IDEA", "DES", "Camellia", "ChaCha20")
        tlsCipher.place(x=2,y=125)

        tlsMsgVar = StringVar(layer6_Frame)
        tlsMsgVar.set("Message Auth")
        tlsMsg = OptionMenu(layer6_Frame, tlsMsgVar, "Hash-based MD5", "SHA hash function")
        tlsMsg.place(x=2,y=155)

        tlsCertLabel = Label(layer6_Frame, text = "TLS Certificate: ")
        tlscert = Text(layer6_Frame, height=10, width=34)
        tlsCertLabel.place(x=2,y=185)
        tlscert.place(x=2,y=205)

        def tlsdone():
            Config.TLS[1] = 1
            underscore = "_"
            tlsConfig.CipherSuite = "TLS" + underscore + tlsExchangeVar.get() + underscore + tlsAuthVar.get() + "WITH" + underscore + tlsCipherVar.get() + "GCM" + tlsMsgVar.get()
            tlsConfig.cert = tlscert.get(1.0,5000.0)
            History_Displayer()
        tlsb = Button(layer6_Frame, text = "✓", command=tlsdone)
        tlsb.place(x=175, y=475, width=100) 


    if l == "SSH":
        sslLabel = Label(layer6_Frame, text = "SSH (WIP): ")
        sslLabel = Label(layer6_Frame, text = "If SSH is enabled then wireshark will be enabled with a SSH view")
        sslLabel.pack()
        sslLabel.pack()

def layer7_Displayer(l):
    layer7_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration", width=284, height=529)
    layer7_Frame.place(x=217, y=0)
    if l == "DHCP":
        dhcpServerText = Label(layer7_Frame, text="DHCP Server IP:")
        dhcpServerText.place(x=1,y=10)
        dhcpiptext = Label(layer7_Frame, text = "DHCP Server IP:")
        dhcpiptext.place(x=2,y=4) 
        dhcpip1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        dhcpip2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        dhcpip3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        dhcpip4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        dot1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dot2 = Label(layer7_Frame, text = ".")
        dot3 = Label(layer7_Frame, text = ".")
        dhcpip1.place(x=105,y=5)     
        dhcpip2.place(x=135,y=5)
        dhcpip3.place(x=165,y=5)
        dhcpip4.place(x=195,y=5)
        dot1.place(x=125,y=5)
        dot2.place(x=155,y=5)
        dot3.place(x=185,y=5)


        dhcpReqServerText = Label(layer7_Frame, text="DHCP Requested IP:")
        dhcpReqServerText.place(x=1,y=30)
        dhcpReqip1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        dhcpReqip2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        dhcpReqip3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        dhcpReqip4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        dotReq1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dotReq2 = Label(layer7_Frame, text = ".")
        dotReq3 = Label(layer7_Frame, text = ".")
        dhcpReqip1.place(x=115,y=35)     
        dhcpReqip2.place(x=145,y=35)
        dhcpReqip3.place(x=175,y=35)
        dhcpReqip4.place(x=205,y=35)
        dotReq1.place(x=135,y=35)
        dotReq2.place(x=165,y=35)
        dotReq3.place(x=195,y=35)

        dhcpMessageText = Label(layer7_Frame, text="DHCP Message Type:")
        dhcpMessageVar = StringVar(layer7_Frame)
        dhcpMessageVar.set("TYPE")
        dhcpMessage = OptionMenu(layer7_Frame, dhcpMessageVar, "DHCP Discover" ,"DHCP Offer", "DHCP Request", "DHCP Pack", "DHCP Nak", "DHCP Release", "DHCP Decline")
        dhcpMessage.place(x=2,y=80)
        dhcpMessageText.place(x=2,y=60)

        dhcpLeaseText = Label(layer7_Frame, text="DHCP Lease Time:")
        dhcpLease = Entry(layer7_Frame, width=5)
        dhcpLeaseText.place(x=2,y=120)
        dhcpLease.place(x=4,y=140)

        
        dhcpDomainText = Label(layer7_Frame, text="DHCP (Offer) Domain Name:")
        dhcpDomain = Entry(layer7_Frame, width=20)
        dhcpDomainText.place(x=2,y=160)
        dhcpDomain.place(x=4,y=180)

        dhcpDNSText = Label(layer7_Frame, text="DHCP (Offer) DNS Server IP:")
        dhcpDNSText.place(x=2,y=205)
        dhcpDomainip1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        dhcpDomainip2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        dhcpDomainip3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        dhcpDomainip4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        dotDomain1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dotDomain2 = Label(layer7_Frame, text = ".")
        dotDomain3 = Label(layer7_Frame, text = ".")
        dhcpDomainip1.place(x=155,y=205)     
        dhcpDomainip2.place(x=185,y=205)
        dhcpDomainip3.place(x=215,y=205)
        dhcpDomainip4.place(x=245,y=205)
        dotDomain1.place(x=175,y=205)
        dotDomain2.place(x=205,y=205)
        dotDomain3.place(x=235,y=205)

        dhcpHostText = Label(layer7_Frame, text="DHCP (Offer) Host Name:")
        dhcpHost = Entry(layer7_Frame, width=20)
        dhcpHostText.place(x=2,y=230)
        dhcpHost.place(x=4,y=250)


        dhcpRouterText = Label(layer7_Frame, text="DHCP (Offer) Router IP:")
        dhcpRouterText.place(x=2,y=275)
        dhcpRouterip1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        dhcpRouterip2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        dhcpRouterip3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        dhcpRouterip4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        dotRouter1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dotRouter2 = Label(layer7_Frame, text = ".")
        dotRouter3 = Label(layer7_Frame, text = ".")
        dhcpRouterip1.place(x=135,y=275)     
        dhcpRouterip2.place(x=165,y=275)
        dhcpRouterip3.place(x=195,y=275)
        dhcpRouterip4.place(x=225,y=275)
        dotRouter1.place(x=155,y=275)
        dotRouter2.place(x=185,y=275)
        dotRouter3.place(x=215,y=275)

        dhcpMaskText = Label(layer7_Frame, text="DHCP (Offer) Subnet Mask:")
        dhcpMaskText.place(x=2,y=305)
        dhcpMaskip1 = Entry(layer7_Frame, width=4) #Octect 1 of the IP
        dhcpMaskip2 = Entry(layer7_Frame, width=4) #Octect 2 of the ip 
        dhcpMaskip3 = Entry(layer7_Frame, width=4) #Octect 3 of the ip 
        dhcpMaskip4 = Entry(layer7_Frame, width=4) #Octect 4 of the ip 
        dotMask1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dotMask2 = Label(layer7_Frame, text = ".")
        dotMask3 = Label(layer7_Frame, text = ".")
        dhcpMaskip1.place(x=4,y=325)     
        dhcpMaskip2.place(x=44,y=325)
        dhcpMaskip3.place(x=84,y=325)
        dhcpMaskip4.place(x=124,y=325)
        dotMask1.place(x=34,y=325)
        dotMask2.place(x=74,y=325)
        dotMask3.place(x=114,y=325)

        def dhcpdone():
            Config.DHCP[1] = 1
            dot = "."
            dhcpConfig.dip = dhcpip1.get() + dot + dhcpip2.get() + dot + dhcpip3.get() + dot + dhcpip4.get()
            dhcpConfig.ReqIP = dhcpReqip1.get() + dot + dhcpReqip2.get() + dot + dhcpReqip3.get() + dot + dhcpReqip4.get()
            dhcpConfig.mType = dhcpMessageVar.get()
            dhcpConfig.Lease = dhcpLease.get()
            dhcpConfig.DomainName = dhcpDomain.get()
            dhcpConfig.DomainIP = dhcpDomainip1.get() + dot + dhcpDomainip1.get() + dot + dhcpDomainip1.get() + dot + dhcpDomainip1.get()
            dhcpConfig.Host = dhcpHost.get()
            dhcpConfig.RouterIP = dhcpRouterip1.get() + dot + dhcpRouterip2.get() + dot  + dhcpRouterip3.get() + dot + dhcpRouterip4.get()
            dhcpConfig.SubnetMask = dhcpMaskip1.get() + dot + dhcpMaskip2.get() + dot  + dhcpMaskip3.get() + dot + dhcpMaskip4.get()
            History_Displayer()
        dhcpb = Button(layer7_Frame, text = "✓", command=dhcpdone)
        dhcpb.place(x=175, y=475, width=100) 



    if l == "TELNET":
        TelCommandVar = StringVar(layer7_Frame)
        TelCommandVar.set("COMMAND:")
        TelCommandText = Label(layer7_Frame, text="Telnet Remote Machine Commands (WIP):")
        TelCommandText.place(x=1,y=2)

        TelCommand1Text = Label(layer7_Frame, text="Telnet Command 1:")
        TelCommand1Text.place(x=1,y=25)
        TelCommand1 = Entry(layer7_Frame, width=30)
        TelCommand1.place(x=4,y=50)

        TelCommand2Text = Label(layer7_Frame, text="Telnet Command 2:")
        TelCommand2Text.place(x=1,y=65)
        TelCommand2 = Entry(layer7_Frame, width=30)
        TelCommand2.place(x=4,y=90)
      
        TelCommand3Text = Label(layer7_Frame, text="Telnet Command 3:")
        TelCommand3Text.place(x=1,y=105)
        TelCommand3 = Entry(layer7_Frame, width=30)
        TelCommand3.place(x=4,y=130)

        TelCommand4Text = Label(layer7_Frame, text="Telnet Command 4:")
        TelCommand4Text.place(x=1,y=145)
        TelCommand4 = Entry(layer7_Frame, width=30)
        TelCommand4.place(x=4,y=170)

        TelCommand5Text = Label(layer7_Frame, text="Telnet Command 5:")
        TelCommand5Text.place(x=1,y=185)
        TelCommand5 = Entry(layer7_Frame, width=30)
        TelCommand5.place(x=4,y=210)

        TelnetCommandText = Label(layer7_Frame, text="Telnet Commands:")
        TelnetCommandVar = StringVar(layer7_Frame)
        TelnetCommandVar.set("COMMAND:")
        TelnetCommand = OptionMenu(layer7_Frame, TelnetCommandVar, "SE","NOP","DM","BRK","IP","AO","AYT","EC","GA","SB","WILL","WONT","DO","DON'T","IAC")
        TelnetCommand.place(x=4,y=250)
        TelnetCommandText.place(x=4,y=230)
        

        TelnetOperationText = Label(layer7_Frame, text="Telnet Operation :")
        TelnetOperationVar = StringVar(layer7_Frame)
        TelnetOperationVar.set("Operation:")
        TelnetOperation = OptionMenu(layer7_Frame, TelnetOperationVar, "WILL", "DO","WONT","DONT")
        TelnetOperation.place(x=4,y=300)
        TelnetOperationText.place(x=4,y=280)
        
        TelnetOperationOptionText = Label(layer7_Frame, text="Telnet Operation Option :")
        TelnetOperationOptionVar = StringVar(layer7_Frame)
        TelnetOperationOptionVar.set("Operation Option")
        TelnetOperationOption = OptionMenu(layer7_Frame, TelnetOperationOptionVar, "Echo", "Suppress go ahead","status","Timing Mark","Terminal Type", "Window Size","Terminal Speed","Remote Flow Control","Linemode","Environmental Variables")
        TelnetOperationOption.place(x=4,y=350)
        TelnetOperationOptionText.place(x=4,y=330)

        def telnetdone():
            Config.TELNET[1] = 1
            telnetConfig.Rcomand1 = TelCommand1.get()
            telnetConfig.Rcomand2 = TelCommand2.get()
            telnetConfig.Rcomand3 = TelCommand3.get()
            telnetConfig.Rcomand4 = TelCommand4.get()
            telnetConfig.Rcomand5 = TelCommand5.get()
            telnetConfig.command = TelnetCommandVar.get()
            telnetConfig.operation = TelnetOperationVar.get()
            telnetConfig.operationOption = TelnetOperationOptionVar.get()
            History_Displayer()
        telnetb = Button(layer7_Frame, text = "✓", command=telnetdone)
        telnetb.place(x=175, y=475, width=100) 

    if l == "IRC":
        IRCCommandVar = StringVar(layer7_Frame)
        IRCCommandVar.set("COMMAND:")
        IRCCommandText = Label(layer7_Frame, text="IRC Command (WIP): ") 
        IRCCommand = OptionMenu(layer7_Frame, IRCCommandVar, "ADMIN", "AWAY", "CNOTICE", "CPRIVMSG", "CONNECT", "DIE" ,"ENCAP", "ERROR", "HELP","INFO", "INVITE", "JOIN", "KICK", "KILL", "KNOCK", "LINKS","LIST","LUSERS","MODE","MOTD","NAMES","NAMESX","OPER","PART","PASS","PING","PONG","PRIVMSG","QUIT","REHASH","RESTART","RULES","SERVER","SERVICE","SERVLIST","SQUERY","SQUIT","SETNAME","SILENCE","STATS","SUMMON","TOPIC","TRACE","UHNAMES","USER","VERISON","WALLOPS","WATCH","WHO","WHOIS","WHOWAS")
        IRCCommand.place(x=120,y=5)
        IRCCommandText.place(x=2,y=10)

        IRCMessageText = Label(layer7_Frame, text="IRC Message:") 
        IRCMessage = Text(layer7_Frame, height=5, width=34)
        IRCMessage.place(x=4,y=60)
        IRCMessageText.place(x=2,y=40)


        IRCUserText = Label(layer7_Frame, text="IRC User Name:")
        IRCUserText.place(x=2,y=140)
        IRCUser = Entry(layer7_Frame, width=30)
        IRCUser.place(x=4,y=160)

        def ircdone():
            Config.IRC[1] = 1
            ircConfig.command = IRCCommandVar.get()
            ircConfig.message = IRCMessage.get(1.0,1000.0)
            ircConfig.Name = IRCUser.get()
            History_Displayer()

        ircb = Button(layer7_Frame, text = "✓", command=ircdone)
        ircb.place(x=175, y=475, width=100) 

    if l == "FTP":
        #Destination IP Placement
        iptext = Label(layer7_Frame, text = "FTP Destination IP:")
        iptext.place(x=2,y=4) 
        ip1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        ip2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        ip3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        ip4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        dot1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dot2 = Label(layer7_Frame, text = ".")
        dot3 = Label(layer7_Frame, text = ".")
        ip1.place(x=105,y=5)     
        ip2.place(x=135,y=5)
        ip3.place(x=165,y=5)
        ip4.place(x=195,y=5)
        dot1.place(x=125,y=5)
        dot2.place(x=155,y=5)
        dot3.place(x=185,y=5)
        # Source Port Placement
        sourcePortText = Label(layer7_Frame, text = "FTP Source Port:")
        sourcePort = Entry(layer7_Frame, width=6)
        sourcePortText.place(x=2, y=30)
        sourcePort.place(x=100,y=30)
        # Source Ip
        ipsrctext = Label(layer7_Frame, text = "FTP Destination IP:")
        ipsrctext.place(x=2,y=55)
        ipsrc1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        ipsrc2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        ipsrc3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        ipsrc4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        ipsrc1.place(x=105,y=55)     
        ipsrc2.place(x=135,y=55)
        ipsrc3.place(x=165,y=55)
        ipsrc4.place(x=195,y=55)
        dotsrc1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dotsrc2 = Label(layer7_Frame, text = ".")
        dotsrc3 = Label(layer7_Frame, text = ".")
        dotsrc1.place(x=125,y=60)
        dotsrc2.place(x=155,y=60)
        dotsrc3.place(x=185,y=60)

        #Radio button (ftp protocol ver)
        ftptext = Label(layer7_Frame, text = "FTP Protocol Verison:")
        ftptext.place(x=2,y=85)
        uftptext = Label(layer7_Frame, text = "TFTP File Name:")
        uftpFile = Entry(layer7_Frame, width=30)
        tftptext = Label(layer7_Frame, text = "UFTP File Name:")
        tftpFile = Entry(layer7_Frame, width=30)
        varftp = IntVar()
        def uftpcmd():
            uftptext.place(x=30, y=150)
            uftpFile.place(x=34, y=170)
            ftpConfig.type[1] = 0
            ftpConfig.type[0] = 1
        def tftpcmd():
            tftptext.place(x=30, y=150)
            tftpFile.place(x=34, y=170)
            ftpConfig.type[1] = 1
            ftpConfig.type[0] = 0

        uftp = Radiobutton(layer7_Frame, text="UFTP", variable=varftp, value= 1, command=uftpcmd)
        tftp = Radiobutton(layer7_Frame, text="TFTP", variable=varftp, value= 2, command=tftpcmd)
        uftp.place(x=40, y=110)
        tftp.place(x=120, y=110)
        #data
        ftpfiledata = Text(layer7_Frame, height=10, width=33)
        ftpfiledata.place(x=5, y=250)
        icmpfiledatatext = Label(layer7_Frame, text="FTP File Data (WIP):")
        icmpfiledatatext.place(x=5, y=225)
        def ftpdone():
            Config.FTP[1] = 1
            dot = "."
            dip = ip1.get() + dot + ip2.get() + dot + ip3.get() + dot + ip4.get()
            sip = ipsrc1.get() + dot + ipsrc2.get() + dot + ipsrc3.get() + dot + ipsrc4.get()
            if ftpConfig.type[1] == 1:
                ftpConfig.file = ""
                ftpConfig.file = uftpFile.get()
            if ftpConfig.type[0] == 1:
                ftpConfig.file = ""
                ftpConfig.file = tftpFile.get()
            ftpConfig.ip = sip
            ftpConfig.dip = dip
            ftpConfig.port = sourcePort.get()
            ftpConfig.data = ftpfiledata.get(1.0,1000.0)
            History_Displayer()
        ftpb = Button(layer7_Frame, text = "✓", command=ftpdone,)
        ftpb.place(x=175, y=475, width=100) 

        #Potentially The data being transferrred (might be hard)        ftp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)
        #Destination Address and Source Address
        #Type of FTP (UFTP or TFTP)
        #Source File (Wip)
        
    if l == "HTTP":
        #Target Website
        httptext = Label(layer7_Frame, text = "Host URL:")
        httptext.place(x=2,y=4)
        websiteEntry = Entry(layer7_Frame, width=30)
        websiteEntry.place(x=80,y=4)
        #User Agent
        httpAgenttext = Label(layer7_Frame, text = "User-Agent:")
        agentvar = StringVar(layer7_Frame)
        agentvar.set("User Agent")
        httpAgent = OptionMenu(layer7_Frame, agentvar, "Chrome", "Firefox", "Microsoft Edge", "Internet Explorer 11.0", "Google Bot", "Apple Ipad", "HTC", "CURL", "WGET")
        httpAgenttext.place(x=2,y=28)
        httpAgent.place(x=80, y=24)
        #Radio Button (Get/Post) (Only supported atm)
        postVar = IntVar()
        getVar = IntVar()
        GetUriEntry = Text(layer7_Frame, height=2, width=34)
        referer = Text(layer7_Frame, height=2, width=34)
        PosturiEntry = Text(layer7_Frame, height=2, width=34)
        PostDataEntry = Text(layer7_Frame, height=4, width=34)
        def POST():
            text = Label(layer7_Frame, text = "Post Request Paramaters")
            text.place(x=80, y= 90)
            PosturiLabel = Label(layer7_Frame, text = "POST Request URI:")
            PosturiLabel.place(x=2,y=115)
            PosturiEntry.place(x=2,y=140)
            PostDataLabel = Label(layer7_Frame, text = "POST Request Data:")
            PostDataLabel.place(x=2,y=175)
            PostDataEntry.place(x=2,y=200)
        def GET():
            text = Label(layer7_Frame, text = "GET Request Paramaters")
            text.place(x=80, y= 270)
            geturi = Label(layer7_Frame, text = "GET Request URI:")
            geturi.place(x=2, y=290)
            GetUriEntry.place(x=2, y=320)
            referertext = Label(layer7_Frame, text = "Referrer:")
            referertext.place(x=2, y = 355)
            referer.place(x=2, y = 380)

        postButton = Radiobutton(layer7_Frame, text = "POST Request", variable=postVar, command=POST)
        getButton = Radiobutton(layer7_Frame, text = "GET Request", variable=getVar, command=GET)
        postButton.place(x=40, y=60)
        getButton.place(x=140, y=60)
        def httpdone():
            Config.HTTP[1] = 1
            httpConfig.URL = websiteEntry.get()
            httpConfig.UserAgent = agentvar.get()
            httpConfig.PostUri = PosturiEntry.get(1.0,1000.0)
            httpConfig.GetUri = GetUriEntry.get(1.0,1000.0)
            httpConfig.GetReferrer = referer.get(1.0,200.0)
            httpConfig.PostData = PostDataEntry.get(1.0,5000.0)
            History_Displayer()


        httpb = Button(layer7_Frame, text = "✓", command=httpdone)
        httpb.place(x=175, y=475, width=100) 
    if l == "HTTPS":
        HTTPStext = Label(layer7_Frame, text = "Host URL:")
        HTTPStext.place(x=2,y=4)
        HTTPSwebsiteEntry = Entry(layer7_Frame, width=30)
        HTTPSwebsiteEntry.place(x=80,y=4)
        #User Agent
        HTTPSAgenttext = Label(layer7_Frame, text = "User-Agent:")
        HTTPSagentvar = StringVar(layer7_Frame)
        HTTPSagentvar.set("User Agent")
        HTTPSAgent = OptionMenu(layer7_Frame, HTTPSagentvar, "Chrome", "Firefox", "Microsoft Edge", "Internet Explorer 11.0", "Google Bot", "Apple Ipad", "HTC", "CURL", "WGET")
        HTTPSAgenttext.place(x=2,y=28)
        HTTPSAgent.place(x=80, y=24)
        #Radio Button (Get/Post) (Only supported atm)
        HTTPSpostVar = IntVar()
        HTTPSgetVar = IntVar()
        HTTPSGetUriEntry = Text(layer7_Frame, height=2, width=34)
        HTTPSreferer = Text(layer7_Frame, height=2, width=34)
        HTTPSPosturiEntry = Text(layer7_Frame, height=2, width=34)
        HTTPSPostDataEntry = Text(layer7_Frame, height=4, width=34)
        def POST():
            text = Label(layer7_Frame, text = "Post Request Paramaters")
            text.place(x=80, y= 90)
            PosturiLabel = Label(layer7_Frame, text = "POST Request URI:")
            PosturiLabel.place(x=2,y=115)
            HTTPSPosturiEntry.place(x=2,y=140)
            PostDataLabel = Label(layer7_Frame, text = "POST Request Data:")
            PostDataLabel.place(x=2,y=175)
            HTTPSPostDataEntry.place(x=2,y=200)
        def GET():
            text = Label(layer7_Frame, text = "GET Request Paramaters")
            text.place(x=80, y= 270)
            geturi = Label(layer7_Frame, text = "GET Request URI:")
            geturi.place(x=2, y=290)
            HTTPSGetUriEntry.place(x=2, y=320)
            referertext = Label(layer7_Frame, text = "Referrer:")
            referertext.place(x=2, y = 355)
            HTTPSreferer.place(x=2, y = 380)

        HTTPSpostButton = Radiobutton(layer7_Frame, text = "POST Request", variable=HTTPSpostVar, command=POST)
        HTTPSgetButton = Radiobutton(layer7_Frame, text = "GET Request", variable=HTTPSgetVar, command=GET)
        HTTPSpostButton.place(x=40, y=60)
        HTTPSgetButton.place(x=140, y=60)
        SSLEntry = Text(layer7_Frame, height=2, width=34)
        SSLEntryLabel = Label(layer7_Frame, text = "SSL Key (WIP)")
        SSLEntryLabel.place(x=2, y=420)
        SSLEntry.place(x=2,y=442)
        def httpsdone():
            Config.HTTP[1] = 1
            httpsConfig.URL = HTTPSwebsiteEntry.get()
            httpsConfig.UserAgent = HTTPSagentvar.get()
            httpsConfig.PostUri = HTTPSPosturiEntry.get(1.0,1000.0)
            httpsConfig.GetUri = HTTPSGetUriEntry.get(1.0,1000.0)
            httpsConfig.GetReferrer = HTTPSreferer.get(1.0,200.0)
            httpsConfig.PostData = HTTPSPostDataEntry.get(1.0,5000.0)
            httpsConfig.SSLKey = SSLEntry.get(1.0,5000.0)
            History_Displayer()

        HTTPSb = Button(layer7_Frame, text = "✓", command=httpsdone)
        HTTPSb.place(x=175, y=480, width=100) 
    if l == "DNS":
        DNStext = Label(layer7_Frame, text = "Query URL:")
        iptext = Label(layer7_Frame, text = "DNS Destination Server IP:")
        iptext.place(x=2,y=4) 
        ip1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        ip2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        ip3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        ip4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        dot1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        dot2 = Label(layer7_Frame, text = ".")
        dot3 = Label(layer7_Frame, text = ".")
        ip1.place(x=145,y=5)     
        ip2.place(x=175,y=5)
        ip3.place(x=205,y=5)
        ip4.place(x=235,y=5)
        dot1.place(x=165,y=5)
        dot2.place(x=195,y=5)
        dot3.place(x=225,y=5)
        DNSCommunicationPortText = Label(layer7_Frame, text= "DNS Communication Port:")
        DNSCommunicationPortText.place(x=2, y=30)
        DNSCommunicationPort = Entry(layer7_Frame, width=3)
        DNSCommunicationPort.place(x=150,y=30)
        DNStext.place(x=2,y=50)
        DNSQuery = Text(layer7_Frame, height=1, width=33)
        DNSQuery.place(x=4,y=70)

        DNSTypeVar = StringVar(layer7_Frame)
        DNSTypeVar.set("Type")
        DNSTypeText = Label(layer7_Frame, text="DNS Query Type: ") 
        DNSType = OptionMenu(layer7_Frame, DNSTypeVar, "A", "AAAA", "ALIAS", "CNAME", "MX", "NS" ,"SOA", "SRV", "TXT")
        DNSTypeText.place(x=2, y=95)
        DNSType.place(x=100,y=90)
        DNSNameText = Label(layer7_Frame, text= "DNS Answer Name:")
        DNSName = Entry(layer7_Frame, width=33)
        DNSNameText.place(x=2, y=120)
        DNSName.place(x=2,y=140)

        DNSClassText = Label(layer7_Frame, text= "DNS Class:")
        DNSClassText.place(x=2,y=175)
        DNSClassVar = StringVar(layer7_Frame)
        DNSClassVar.set("Class (IN Default)")
        DNSClass = OptionMenu(layer7_Frame, DNSClassVar, "IN", "CS", "CH", "HS")
        DNSClass.place(x=70,y=170)

        DNSClassText = Label(layer7_Frame, text= "DNS Answer Address:")
        DNSClassText.place(x=2,y=215)
        Ansip1 = Entry(layer7_Frame, width=2) #Octect 1 of the IP
        Ansip2 = Entry(layer7_Frame, width=2) #Octect 2 of the ip 
        Ansip3 = Entry(layer7_Frame, width=2) #Octect 3 of the ip 
        Ansip4 = Entry(layer7_Frame, width=2) #Octect 4 of the ip 
        Ansdot1 = Label(layer7_Frame, text = ".") # Three dots seperating the fields
        Ansdot2 = Label(layer7_Frame, text = ".")
        Ansdot3 = Label(layer7_Frame, text = ".")
        Ansip1.place(x=125,y=215)     
        Ansip2.place(x=155,y=215)
        Ansip3.place(x=185,y=215)
        Ansip4.place(x=215,y=215)
        Ansdot1.place(x=145,y=215)
        Ansdot2.place(x=175,y=215)
        Ansdot3.place(x=205,y=215)
        
        DNSTimeText = Label(layer7_Frame, text= "DNS Answer Time to Live: ")
        DNSTimeText.place(x=2,y=245)
        DNSTime = Entry(layer7_Frame, width=5)
        DNSTime.place(x=145,y=245)

        def dnsdone():
            dot = "."
            Config.DNS[1] = 1
            dnsConfig.dip = ip1.get() + dot + ip2.get() + dot + ip3.get() + dot + ip4.get()
            dnsConfig.Type = DNSTypeVar.get()
            dnsConfig.Class = DNSClassVar.get()
            dnsConfig.Cport= DNSCommunicationPort.get()
            dnsConfig.AnswerIP = Ansip1.get() + dot + Ansip2.get() + dot + Ansip3.get() + dot + Ansip4.get()
            dnsConfig.TIL = DNSTime.get()
            dnsConfig.AnswerName = DNSName.get()
            History_Displayer()
        dnsb = Button(layer7_Frame, text = "✓", command=dnsdone)
        dnsb.place(x=175, y=475, width=100) 



# History Displayer uses the size class described earlier, It postions everything dynamically depending on the location of previously placed protocols, it also defines spinboxes and the info tab for each protocol

def History_Displayer():
    icmpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size ,width=4,)
    arpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    ftpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    httpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    httpsSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    ircSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4, )
    telnetSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    dhcpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    smbSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4, )
    biosSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4,)
    ospfSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    ripSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    dnsSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size , width=4)
    #Loads the specific Sizes. (Has to be within this function otherwise TrafficSize won't load)
    tlsLabelTick = Label(TrafficConfigFrame, text="✓")
    socksLabelTick = Label(TrafficConfigFrame, text="✓")
    wifiLabelTick = Label(TrafficConfigFrame, text="✓")
    ipLabelTick = Label(TrafficConfigFrame, text="✓")
    ethLabelTick = Label(TrafficConfigFrame, text="✓")
    tcpLabelTick = Label(TrafficConfigFrame, text="✓")
    udpLabelTick = Label(TrafficConfigFrame, text="✓")
    
    #Loads the spinbox sizes into the right protocols size class value (If statement works fine)
    def TrafficSize_Loader():
        if Config.ICMP[1] == 1:
            icmpConfig.size = icmpSpinbox.get()
        if Config.ARP[1] == 1:
            arpConfig.size = arpSpinbox.get()
        if Config.FTP[1] == 1:
            ftpConfig.size = ftpSpinbox.get()
        if Config.HTTP[1] == 1:
            httpConfig.size = httpSpinbox.get()
        if Config.HTTPS[1] == 1:
            httpsConfig.size = httpsSpinbox.get()
        if Config.IRC[1] == 1:
            ircConfig.size = ircSpinbox.get()
        if Config.TELNET[1] == 1:
            telnetConfig.size = telnetSpinbox.get()
        if Config.DHCP[1] == 1:
            dhcpConfig.size = dhcpSpinbox.get()
        if Config.FTP[1] == 1:
            ftpConfig.size  = ftpSpinbox.get()
        if Config.SMB[1] == 1:
            smbConfig.size  = smbSpinbox.get()
        if Config.NetBIOS[1] == 1:
            netbiosConfig.size  = biosSpinbox.get()
        if Config.OSPF[1] == 1:
            ospfConfig.size  = ospfSpinbox.get()
        if Config.RIP[1] == 1:
            ripConfig.size  = ripSpinbox.get()

    #Button that calls the function above
    TrafficSizeButton = Button(TrafficConfigFrame, text = "✓", command=TrafficSize_Loader)
    TrafficSizeButton.place(x=127,y=140)

    #Next If Statements checks if the Protocol is being used and if so has it already been displayed. If A protocol hits the critera then it is displayed on the gui and a info button is given  which allows a user to check what the protocol configuration has been set to

    if Config.ICMP[1] == 1 and Config.ICMP[2] == 0:
        Config.ICMP[2] = 1
        icmpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        icmpHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1) )
        LocationConfig()
        icmpHistoryLabel = Label(icmpHistory, text = "ICMP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        icmpHistoryLabel.place(x=0, y=0)
        def ICMPDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current ICMP Configuration")
            PopupLabel = LabelFrame(Popup, text="ICMP Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupIP = Label(PopupLabel, text=("Source IP: " + icmpConfig.ip))
            PopupDIP = Label(PopupLabel, text=("Destination IP: " + icmpConfig.dip))
            Popupmac = Label(PopupLabel, text=("Source Mac: " + icmpConfig.mac))
            Popupdmac = Label(PopupLabel, text=("Destination Mac: " + icmpConfig.dmac))
            Popuptext = Label(PopupLabel, text=("ICMP Ping Data: " + icmpConfig.Text))
            Popupsize = Label(PopupLabel, text=("You have Selected " + icmpConfig.size + "ICMP Packet(s)"))
            PopupIP.pack()
            PopupDIP.pack()
            Popupmac.pack()
            Popupdmac.pack()
            Popuptext.pack()
            Popupsize.pack()
        icmpHistoryButton = Button(icmpHistory, text = "INFO", width=3, height=0, command=ICMPDisplay)
        icmpHistoryButton.place(x=227, y=1)
        icmpSpinboxLabel = Label(TrafficConfigFrame, text="ICMP:")
        icmpSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        icmpSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.ARP[1] == 1 and Config.ARP[2] == 0: #Hasn't been displayed and is chosen
        Config.ARP[2] = 1
        arpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        arpHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1) )
        LocationConfig()
        arpHistoryLabel = Label(arpHistory, text = "ARP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        arpHistoryLabel.place(x=0, y=0)
        def ARPDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current ARP Configuration")
            PopupLabel = LabelFrame(Popup, text="ARP Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupIP = Label(PopupLabel, text=("Source IP: " + arpConfig.senderip))
            PopupDIP = Label(PopupLabel, text=("Destination IP: " + arpConfig.targetip))
            Popupmac = Label(PopupLabel, text=("Source Mac: " + arpConfig.sendermac))
            Popupdmac = Label(PopupLabel, text=("Destination Mac: " + arpConfig.targetmac))
            PopupIP.pack()
            PopupDIP.pack()
            Popupmac.pack()
            Popupdmac.pack()

        arpHistoryButton = Button(arpHistory, text = "INFO", width=3, height=0, command=ARPDisplay)
        arpHistoryButton.place(x=227, y=1)
        arpSpinboxLabel = Label(TrafficConfigFrame, text="ARP:")
        arpSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        arpSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)
            

    if Config.FTP[1] == 1 and Config.FTP[2] == 0:
        Config.FTP[2] = 1
        ftpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        ftpHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1) )
        LocationConfig()
        ftpHistoryLabel = Label(ftpHistory, text = "FTP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        ftpHistoryLabel.place(x=0, y=0)
        placed = 0
        def ftpDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current FTP Configuration")
            PopupLabel = LabelFrame(Popup, text="FTP Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupIP = Label(PopupLabel, text=("Source IP: " + ftpConfig.ip))
            PopupDIP = Label(PopupLabel, text=("Destination IP: " + ftpConfig.dip))
            Popupport = Label(PopupLabel, text=("Source Port: " + ftpConfig.port))
            Popupdfile = Label(PopupLabel, text=("Chosen File " + ftpConfig.file))
            Popupdata = Label(PopupLabel, text=("FTP File Data: " + ftpConfig.data))
            PopupIP.pack()
            PopupDIP.pack()
            Popupport.pack()
            Popupdfile.pack()
            Popupdata.pack()

        ftpHistoryButton = Button(ftpHistory, text = "INFO", width=3, height=0, command=ftpDisplay)
        ftpHistoryButton.place(x=227, y=1)
        ftpSpinboxLabel = Label(TrafficConfigFrame, text="FTP:")
        ftpSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        ftpSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)
    
    if Config.HTTP[1] == 1 and Config.HTTP[2] == 0:
        Config.HTTP[2] = 1
        httpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        httpHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        httpHistoryLabel = Label(httpHistory, text = "HTTP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        httpHistoryLabel.place(x=0, y=0)
        placed = 0
        def httpDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current HTTP Configuration")
            PopupLabel = LabelFrame(Popup, text="HTTP Configuration", width=250, height=250)
            PopupLabel.pack()
            Popupurl = Label(PopupLabel, text=("URL: " + httpConfig.URL))
            Popupagent = Label(PopupLabel, text=("User Agent: " + httpConfig.UserAgent))
            PopupPOSTuri = Label(PopupLabel, text=("POST Request URI: " + httpConfig.PostUri))
            PopupGETuri = Label(PopupLabel, text=("GET Request URI: " + httpConfig.GetUri))
            PopupdRef = Label(PopupLabel, text=("GET Request Referrer: " + httpConfig.GetReferrer))
            Popupdata = Label(PopupLabel, text=("POST Data File Data: " + httpConfig.PostData))
            Popupurl.pack()
            Popupagent.pack()
            PopupPOSTuri.pack()
            PopupGETuri.pack()
            PopupdRef.pack()
            Popupdata.pack()
        httpHistoryButton = Button(httpHistory, text = "INFO", width=3, height=0, command=httpDisplay)
        httpHistoryButton.place(x=227, y=1)
        httpSpinboxLabel = Label(TrafficConfigFrame, text="HTTP:")
        httpSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        httpSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)
    
    if Config.HTTPS[1] == 1 and Config.HTTPS[2] == 0:
        Config.HTTPS[2] = 1
        httpsHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        httpsHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        httpsHistoryLabel = Label(httpsHistory, text = "HTTPS", font=("Arial", 16), borderwidth=1,  relief="solid",)
        httpsHistoryLabel.place(x=0, y=0)
        placed = 0
        def httpsDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current HTTPS Configuration")
            PopupLabel = LabelFrame(Popup, text="HTTPS Configuration", width=250, height=250)
            PopupLabel.pack()
            Popupurl = Label(PopupLabel, text=("URL: " + httpsConfig.URL))
            Popupagent = Label(PopupLabel, text=("User Agent: " + httpsConfig.UserAgent))
            PopupPOSTuri = Label(PopupLabel, text=("POST Request URI: " + httpsConfig.PostUri))
            PopupGETuri = Label(PopupLabel, text=("GET Request URI: " + httpsConfig.GetUri))
            PopupdRef = Label(PopupLabel, text=("GET Request Referrer: " + httpsConfig.GetReferrer))
            Popupdata = Label(PopupLabel, text=("POST Data File Data: " + httpsConfig.PostData))
            PopupSSL = Label(PopupLabel, text=("HTTPS SSL KEY: " + httpsConfig.SSLKey))
            PopupSSL.pack()
            Popupurl.pack()
            Popupagent.pack()
            PopupPOSTuri.pack()
            PopupGETuri.pack()
            PopupdRef.pack()
            Popupdata.pack()
        httpsHistoryButton = Button(httpsHistory, text = "INFO", width=3, height=0, command=httpsDisplay)
        httpsHistoryButton.place(x=227, y=1)
        httpsSpinboxLabel = Label(TrafficConfigFrame, text="HTTPS:")
        httpsSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        httpsSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.IRC[1] == 1 and Config.IRC[2] == 0:
        Config.IRC[2] = 1
        IRCHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        IRCHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        IRCHistoryLabel = Label(IRCHistory, text = "IRC", font=("Arial", 16), borderwidth=1,  relief="solid",)
        IRCHistoryLabel.place(x=0, y=0)
        def ircDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current IRC Configuration")
            PopupLabel = LabelFrame(Popup, text="IRC Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupName = Label(PopupLabel, text=("User Name: " + ircConfig.Name))
            PopupMessage = Label(PopupLabel, text=("IRC Message: " + ircConfig.message))
            PopupCommand = Label(PopupLabel, text=("IRC Command: " + ircConfig.command))
            PopupName.pack()
            PopupMessage.pack()
            PopupCommand.pack()
        ircHistoryButton = Button(IRCHistory, text = "INFO", width=3, height=0, command=ircDisplay)
        ircHistoryButton.place(x=227, y=1)
        ircSpinboxLabel = Label(TrafficConfigFrame, text="IRC:")
        ircSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        ircSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.TELNET[1] == 1 and Config.TELNET[2] == 0:
        Config.TELNET[2] = 1
        telnetHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        telnetHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        telnetHistoryLabel = Label(telnetHistory, text = "TELNET", font=("Arial", 16), borderwidth=1,  relief="solid",)
        telnetHistoryLabel.place(x=0, y=0)
        def telnetDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current Telnet Configuration")
            PopupLabel = LabelFrame(Popup, text="Telnet Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupRcommand1 = Label(PopupLabel, text=("Remote Command 1: " + telnetConfig.Rcomand1))
            PopupRcommand2 = Label(PopupLabel, text=("Remote Command 2: " + telnetConfig.Rcomand2))
            PopupRcommand3 = Label(PopupLabel, text=("Remote Command 3: " + telnetConfig.Rcomand3))
            PopupRcommand4 = Label(PopupLabel, text=("Remote Command 4: " + telnetConfig.Rcomand4))
            PopupRcommand5 = Label(PopupLabel, text=("Remote Command 5: " + telnetConfig.Rcomand5))
            Popupcommand = Label(PopupLabel, text=("Remote Command 5: " + telnetConfig.command))
            Popupoperation = Label(PopupLabel, text=("Remote Command 5: " + telnetConfig.operation))
            Popupoperationoption = Label(PopupLabel, text=("Remote Command 5: " + telnetConfig.operationOption))
            PopupRcommand1.pack()
            PopupRcommand2.pack()
            PopupRcommand3.pack()
            PopupRcommand4.pack()
            PopupRcommand5.pack()
            Popupcommand.pack()
            Popupoperation.pack()
            Popupoperationoption.pack()
        telnetHistoryButton = Button(telnetHistory, text = "INFO", width=3, height=0, command=telnetDisplay)
        telnetHistoryButton.place(x=227, y=1)
        telnetSpinboxLabel = Label(TrafficConfigFrame, text="Telnet:")
        telnetSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        telnetSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)
            
    if Config.DHCP[1] == 1 and Config.DHCP[2] == 0:
        Config.DHCP[2] = 1
        dhcpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        dhcpHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        dhcpHistoryLabel = Label(dhcpHistory, text = "DCHP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        dhcpHistoryLabel.place(x=0, y=0)
        def dhcpDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current DHCP Configuration")
            PopupLabel = LabelFrame(Popup, text="DHCP Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupDIP = Label(PopupLabel, text=("DHCP Server:" + dhcpConfig.dip))
            PopupReqIP = Label(PopupLabel, text=("Requested IP Address: " + dhcpConfig.ReqIP))
            PopupReqMessage = Label(PopupLabel, text=("DHCP Message Type: " + dhcpConfig.mType))
            PopupLease = Label(PopupLabel, text=("DHCP Lease " + dhcpConfig.Lease))
            PopupHost = Label(PopupLabel, text=("DHCP Requested Host Name " + dhcpConfig.Host))
            PopupRouter = Label(PopupLabel, text=("DHCP Requested Router IP " + dhcpConfig.RouterIP))
            PopupSubnet = Label(PopupLabel, text=("DHCP Requested Subnet Mask: " + dhcpConfig.SubnetMask))
            PopupDIP.pack()
            PopupReqIP.pack()
            PopupReqMessage.pack()
            PopupLease.pack()
            PopupHost.pack()
            PopupRouter.pack()
            PopupSubnet.pack()
        dhcpHistoryButton = Button(dhcpHistory, text = "INFO", width=3, height=0, command=dhcpDisplay)
        dhcpHistoryButton.place(x=227, y=1)
        dhcpSpinboxLabel = Label(TrafficConfigFrame, text="DHCP")
        dhcpSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        dhcpSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)
        
        #Layer 6
    if Config.TLS[1] == 1 and Config.TLS[2] == 0:
        Config.TLS[2] = 1
        tlsHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        tlsHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        tlsHistoryLabel = Label(tlsHistory, text = "TLS", font=("Arial", 16), borderwidth=1,  relief="solid",)
        tlsHistoryLabel.place(x=0, y=0)
        def tlsDisplay():
            Popup = Toplevel()
            Popup.title("Current TLS Configuration")
            PopupLabel = LabelFrame(Popup, text="TLS Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupCERT = Label(PopupLabel, text=("TLS Cert: " + tlsConfig.cert))
            PopupSuite = Label(PopupLabel, text=("TLS Cipher Suite: \n" + tlsConfig.CipherSuite))
            PopupCERT.pack()
            PopupSuite.pack()
        tlsHistoryButton = Button(tlsHistory, text = "INFO", width=3, height=0, command=tlsDisplay)
        tlsHistoryButton.place(x=227, y=1)
        tlsSpinboxLabel = Label(TrafficConfigFrame, text="TLS:")
        tlsSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        tlsLabelTick.place(x=LocationConfiguration.x, y=LocationConfiguration.y)
        
    if Config.SMB[1] == 1 and Config.SMB[2] == 0:
        Config.SMB[2] = 1
        smbHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        smbHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        smbHistoryLabel = Label(smbHistory, text = "SMB", font=("Arial", 16), borderwidth=1,  relief="solid",)
        smbHistoryLabel.place(x=0, y=0)
        def smbDisplay():
            Popup = Toplevel()
            Popup.title("Current SMB Configuration")
            PopupLabel = LabelFrame(Popup, text="SMB Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupSMBid = Label(PopupLabel, text=("SMB Identifier" + smbConfig.cid))
            PopupSMBcmd = Label(PopupLabel, text=("SMB Command" + smbConfig.command))
            PopupSMBimp = Label(PopupLabel, text=("SMB Implementation" + smbConfig.implementation))
            PopupSMBid.pack()
            PopupSMBcmd.pack()
            PopupSMBimp.pack()
        smbHistoryButton = Button(smbHistory, text = "INFO", width=3, height=0, command=smbDisplay)
        smbHistoryButton.place(x=227, y=1)
        smbSpinboxLabel = Label(TrafficConfigFrame, text="SMB:")
        smbSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        smbSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.NetBIOS[1] == 1 and Config.NetBIOS[2] == 0:
        Config.NetBIOS[2] = 1
        biosHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        biosHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        biosHistoryLabel = Label(biosHistory, text = "BIOS", font=("Arial", 16), borderwidth=1,  relief="solid",)
        biosHistoryLabel.place(x=0, y=0)
        def biosDisplay():
            Popup = Toplevel()
            Popup.title("Current NetBios Configuration")
            PopupLabel = LabelFrame(Popup, text="NetBios Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupbiosName = Label(PopupLabel, text=("NetBios Service Name: " + netbiosConfig.Name))
            PopupbiosGname = Label(PopupLabel, text=("NetBios Group Service Name: "  + netbiosConfig.gName))
            PopupSession = Label(PopupLabel, text=("NetBios Session Configuration: " + netbiosConfig.Session))
            PopupDatagram = Label(PopupLabel, text=("NetBios Datagram Configuration: " + netbiosConfig.Datagram))
            PopupService = Label(PopupLabel, text=("NetBios Service: " + netbiosConfig.Service))
            PopupbiosName.pack()
            PopupbiosGname.pack()
            PopupSession.pack()
            PopupDatagram.pack()
            PopupService.pack()
        biosHistoryButton = Button(biosHistory, text = "INFO", width=3, height=0, command=biosDisplay)
        biosHistoryButton.place(x=227, y=1)
        biosSpinboxLabel = Label(TrafficConfigFrame, text="BIOS:")
        biosSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        biosSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.SOCKS[1] == 1 and Config.SOCKS[2] == 0:
        Config.SOCKS[2] = 1
        socksHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        socksHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        socksHistoryLabel = Label(socksHistory, text = "SOCKS", font=("Arial", 16), borderwidth=1,  relief="solid",)
        socksHistoryLabel.place(x=0, y=0)
        def sockDisplay():
            Popup = Toplevel()
            Popup.title("Current SOCKS Proxy Configuration")
            PopupLabel = LabelFrame(Popup, text="SOCKS Proxy onfiguration", width=250, height=250)
            PopupLabel.pack()
            PopupSockAuth = Label(PopupLabel, text="Sock authentication: " + socksConfig.Auth)
            PopupSockDIP = Label(PopupLabel, text="Sock Proxy IP: " + socksConfig.DIP)
            PopupSockPort = Label(PopupLabel, text="Sock Proxy Port: " + socksConfig.DPort)
            PopupSockID = Label(PopupLabel, text="Sock Proxy User Identification: " + socksConfig.ID)
            PopupSockConfig = Label(PopupLabel, text="Sock Proxy Configuration " + socksConfig.Config)
            PopupSockAuth.pack()
            PopupSockDIP.pack()
            PopupSockPort.pack()
            PopupSockID.pack()
            PopupSockConfig.pack()
        sockHistoryButton = Button(socksHistory, text = "INFO", width=3, height=0, command=sockDisplay)
        sockHistoryButton.place(x=227, y=1)
        sockSpinboxLabel = Label(TrafficConfigFrame, text="SOCKS:")
        sockSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        socksLabelTick.place(x=LocationConfiguration.x, y=LocationConfiguration.y)


    if Config.Wifi[1] == 1 and Config.Wifi[2] == 0:
        Config.Wifi[2] = 1
        wifiHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        wifiHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        wifiHistoryLabel = Label(wifiHistory, text = "Wifi", font=("Arial", 16), borderwidth=1,  relief="solid",)
        wifiHistoryLabel.place(x=0, y=0)
        def wifiDisplay():
            Popup = Toplevel()
            Popup.title("Current Wifi Configuration")
            PopupLabel = LabelFrame(Popup, text="Wifi Proxy onfiguration", width=250, height=250)
            PopupWifiRec = Label(PopupLabel, text="Wifi Reciever address: " + wifiConfig.reciver)
            PopupWifiTrans = Label(PopupLabel, text="Wifi Transmitter address: " + wifiConfig.transmitter)
            PopupWifiDest = Label(PopupLabel, text="Wifi Destination address: " + wifiConfig.destination)
            PopupWifiSource = Label(PopupLabel, text="Wifi Source address: " + wifiConfig.source)
            PopupWifiBss = Label(PopupLabel, text="Wifi BSS ID: " + wifiConfig.bss)
            PopupWifiPhy = Label(PopupLabel, text="Wifi PHY: " + wifiConfig.phy)
            PopupWifimcs = Label(PopupLabel, text="Wifi MCS Index: " + wifiConfig.mcs)
            PopupWifiDataR = Label(PopupLabel, text="Wifi Data Rate: " + wifiConfig.DataR)
            PopupWifiChannel = Label(PopupLabel, text="Wifi Channel: " + wifiConfig.Channel)
            PopupLabel.pack()
            PopupWifiRec.pack()
            PopupWifiTrans.pack()
            PopupWifiDest.pack()
            PopupWifiSource.pack()
            PopupWifiPhy.pack()
            PopupWifiBss.pack()
            PopupWifimcs.pack()
            PopupWifiDataR.pack()
            PopupWifiChannel.pack()

        wifiHistoryButton = Button(wifiHistory, text = "INFO", width=3, height=0, command=wifiDisplay)
        wifiHistoryButton.place(x=227, y=1)
        wifiSpinboxLabel = Label(TrafficConfigFrame, text="WIFI:")
        wifiSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        wifiLabelTick.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.Ethernet[1] == 1 and Config.Ethernet[2] == 0:
        Config.Ethernet[2] = 1
        ethHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        ethHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        ethHistoryLabel = Label(ethHistory, text = "Ethernet", font=("Arial", 16), borderwidth=1,  relief="solid",)
        ethHistoryLabel.place(x=0, y=0)
        def EthDisplay():
            Popup = Toplevel()
            Popup.title("Current Ethernet Configuration")
            PopupLabel = LabelFrame(Popup, text="Ethernet ", width=250, height=250)
            EthDestinationMac = Label(PopupLabel, text="Ethernet Destination Mac: " + ethernetConfig.dmac)
            EthSourceMac = Label(PopupLabel, text="Ethernet Source Mac: " + ethernetConfig.smac)
            PopupLabel.pack()
            EthDestinationMac.pack()
            EthSourceMac.pack()

        ethHistoryButton = Button(ethHistory, text = "INFO", width=3, height=0, command=EthDisplay)
        ethHistoryButton.place(x=227, y=1)
        ethSpinboxLabel = Label(TrafficConfigFrame, text="Eth:")
        ethSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        ethLabelTick.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.OSPF[1] == 1 and Config.OSPF[2] == 0:
        Config.OSPF[2] = 1
        ospfHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        ospfHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        ospfHistoryLabel = Label(ospfHistory, text = "OSPF", font=("Arial", 16), borderwidth=1,  relief="solid",)
        ospfHistoryLabel.place(x=0, y=0)
        def ospfDisplay():      
            Popup = Toplevel()
            Popup.title("Current OSPF Configuration")
            PopupLabel = LabelFrame(Popup, text="OSPF onfiguration", width=250, height=250)
            PopupOSPFSource = Label(PopupLabel, text="OSPF Source Router: " + ospfConfig.sourcerouter)
            PopupOSPFBackup = Label(PopupLabel, text="OSPF Backup Router: " + ospfConfig.backuprouter)
            PopupOSPFMask = Label(PopupLabel, text="OSPF Network Mask: " + ospfConfig.mask)
            PopupOSPFMessage = Label(PopupLabel, text="OSPF Network Message Type: " + ospfConfig.message)
            PopupLabel.pack()
            PopupOSPFSource.pack()
            PopupOSPFBackup.pack()
            PopupOSPFMask.pack()
            PopupOSPFMessage.pack()
        ospfHistoryButton = Button(ospfHistory, text = "INFO", width=3, height=0, command=ospfDisplay)
        ospfHistoryButton.place(x=227, y=1)
        ospfSpinboxLabel = Label(TrafficConfigFrame, text="OSPF:")
        ospfSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        ospfSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)


    if Config.RIP[1] == 1 and Config.RIP[2] == 0:
        Config.RIP[2] = 1
        ripHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        ripHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        ripHistoryLabel = Label(ripHistory, text = "RIP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        ripHistoryLabel.place(x=0, y=0)
        def ripDisplay():  
            Popup = Toplevel()
            Popup.title("Current RIP Configuration")
            PopupLabel = LabelFrame(Popup, text="RIP configuration", width=250, height=250)
            PopupRIPRes = Label(PopupLabel, text="RIP Response IP: " + ripConfig.ResponseIP)
            PopupRIPVer = Label(PopupLabel, text="RIP Ver: " + ripConfig.RipVer)
            PopupLabel.pack()
            PopupRIPRes.pack()
            PopupRIPVer.pack()
        ripHistoryButton = Button(ripHistory, text = "INFO", width=3, height=0, command=ripDisplay)
        ripHistoryButton.place(x=227, y=1)
        ripSpinboxLabel = Label(TrafficConfigFrame, text="RIP:")
        ripSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        ripSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.IP[1] == 1 and Config.IP[2] == 0:
        Config.IP[2] = 1
        ipHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        ipHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        ipHistoryLabel = Label(ipHistory, text = "IP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        ipHistoryLabel.place(x=0, y=0)
        def ipDisplay():      
            Popup = Toplevel()
            Popup.title("Current IP Configuration")
            PopupLabel = LabelFrame(Popup, text="IP Configuration", width=250, height=250)
            PopupIP = Label(PopupLabel, text="This Configuration will be set as default (and overwrite) for all protocols that directly use IP,")
            PopupsrcIP = Label(PopupLabel, text="Default Source IP Address: " + ipConfig.sourceIp)
            PopupdesIP = Label(PopupLabel, text="Default Destination IP Address: " + ipConfig.destinationIp)
            PopupTIL = Label(PopupLabel, text="Default TIL: " + ipConfig.TIL)
            PopupLabel.pack()
            PopupsrcIP.pack()
            PopupdesIP.pack()
            PopupTIL.pack()
            PopupIP.pack()
            PopupIP
        ipHistoryButton = Button(ipHistory, text = "INFO", width=3, height=0, command=ipDisplay)
        ipHistoryButton.place(x=227, y=1)
        ipSpinboxLabel = Label(TrafficConfigFrame, text="IP:")
        ipSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        ipLabelTick.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.TCP[1] == 1 and Config.TCP[2] == 0:
        Config.TCP[2] = 1
        tcpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        tcpHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        tcpHistoryLabel = Label(tcpHistory, text = "IP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        tcpHistoryLabel.place(x=0, y=0)
        def tcpDisplay():      
            Popup = Toplevel()
            Popup.title("Current TCP Configuration")
            PopupLabel = LabelFrame(Popup, text="TCP Configuration", width=250, height=250)
            PopupPort = Label(PopupLabel, text="TCP Source Port: " + tcpConfig.port)
            Popupdport = Label(PopupLabel, text="TCP Destination port: " + tcpConfig.dport)
            Popupip = Label(PopupLabel, text="TCP Source Ip address: " + tcpConfig.ip)
            Popupdip = Label(PopupLabel, text="TCP Destination Ip address: " + tcpConfig.dip)
            PopupWindow = Label(PopupLabel, text="TCP Windowing Size: " + tcpConfig.window)
            PopupPadding = Label(PopupLabel, text="TCP Padding Size: " + tcpConfig.padding)
            PopupLabel.pack()
            PopupPort.pack()
            Popupdport.pack()
            Popupip.pack()
            Popupdip.pack()
            PopupWindow.pack()
            PopupPadding.pack()
        tcpHistoryButton = Button(tcpHistory, text = "INFO", width=3, height=0, command=tcpDisplay)
        tcpHistoryButton.place(x=227, y=1)
        tcpSpinboxLabel = Label(TrafficConfigFrame, text="TCP:")
        tcpSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        tcpLabelTick.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.UDP[1] == 1 and Config.UDP[2] == 0:
        Config.UDP[2] = 1
        udpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        udpHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        udpHistoryLabel = Label(udpHistory, text = "UDP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        udpHistoryLabel.place(x=0, y=0)
        def udpDisplay():      
            Popup = Toplevel()
            Popup.title("Current UDP Configuration")
            PopupLabel = LabelFrame(Popup, text="UDP Configuration", width=250, height=250)
            PopupPort = Label(PopupLabel, text="UDP Source Port: " + udpConfig.port)
            Popupdport = Label(PopupLabel, text="UDP Destination port: " + udpConfig.dport)
            Popupip = Label(PopupLabel, text="UDP Source Ip address: " + udpConfig.ip)
            Popupdip = Label(PopupLabel, text="UDP Destination Ip address: " + udpConfig.dip)
            PopupLabel.pack()
            PopupPort.pack()
            Popupdport.pack()
            Popupip.pack()
            Popupdip.pack()
        udpHistoryButton = Button(udpHistory, text = "INFO", width=3, height=0, command=udpDisplay)
        udpHistoryButton.place(x=227, y=1)
        udpSpinboxLabel = Label(TrafficConfigFrame, text="UDP:")
        udpSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        udpLabelTick.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

    if Config.DNS[1] == 1 and Config.DNS[2] == 0:
        Config.DNS[2] = 1
        dnsHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        dnsHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        dnsHistoryLabel = Label(dnsHistory, text = "DNS", font=("Arial", 16), borderwidth=1,  relief="solid",)
        dnsHistoryLabel.place(x=0, y=0)
        def dnsDisplay():      
            Popup = Toplevel()
            Popup.title("Current DNS Configuration")
            PopupLabel = LabelFrame(Popup, text="DNS Configuration", width=250, height=250)
            PopupPort = Label(PopupLabel, text="DNS Source Port: " + dnsConfig.port)
            Popupdport = Label(PopupLabel, text="DNS Destination port: " + dnsConfig.dport)
            Popupip = Label(PopupLabel, text="DNS Source Ip address: " + dnsConfig.ip)
            Popupdip = Label(PopupLabel, text="DNS Destination Ip address: " + dnsConfig.dip)
            Popupclass = Label(PopupLabel, text="DNS Class: " + dnsConfig.Class)
            Popupcommand = Label(PopupLabel, text="DNS Type: " + dnsConfig.Type)
            PopupresponseIp = Label(PopupLabel, text="DNS Response IP: " + dnsConfig.AnswerIP)
            PopupresponseURL = Label(PopupLabel, text="DNS Response URL: " + dnsConfig.AnswerName)
            PopupLabel.pack()
            PopupPort.pack()
            Popupdport.pack()
            Popupip.pack()
            Popupclass.pack()
            Popupcommand.pack()
            PopupresponseIp.pack()
            PopupresponseURL.pack()
            Popupdip.pack()
        dnsHistoryButton = Button(dnsHistory, text = "INFO", width=3, height=0, command=dnsDisplay)
        dnsHistoryButton.place(x=227, y=1)
        dnsSpinboxLabel = Label(TrafficConfigFrame, text="DNS:")
        dnsSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        dnsSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)

#Function on the "create Pcap button", checks for errors, then calls the main writing function (PcapWrite())
#This function is called by the "Create Pcap" button
def createPcap():
        ErrorReset()   # clears all previous error checks from previous creations (Defined above)

        #Checker functions (This will be ran on pretty much every protocol) 
        # As tkinter doesn't like values being returned we have to use a place holder class to hold errors. This gets reset after each compare. (This allows for multiple protocols to use the error checking functions)
        #
        # Protocol calls ErrorChecker functions --> ErrorHolderClass contains Errors from Errorchecker functions --> Calling Protocol Loads it's Error values to be the same as ErrorHolder Class --> Reset ErrorHolderClass --> Repeat
        if Config.Ethernet[1] == 1:
            MAC_checker(ethernetConfig.smac) #calls the mac parse function
            ethernetConfig.smacerror[0] = MACErrors.error[0]
            ethernetConfig.smacerror[1] = MACErrors.error[1]
            ethernetConfig.smacerror[2] = MACErrors.error[2]
            ethernetConfig.smacerror[3] = MACErrors.error[3]
            CMPErrorReset()
            MAC_checker(ethernetConfig.dmac) #calls the mac parse function
            ethernetConfig.dmacerror[0] = MACErrors.error[0]
            ethernetConfig.dmacerror[1] = MACErrors.error[1]
            ethernetConfig.dmacerror[2] = MACErrors.error[2]
            ethernetConfig.dmacerror[3] = MACErrors.error[3]
            CMPErrorReset()
        
        #Wifi Error Checking
        if Config.Wifi[1] == 1:
            #Checks if the reciver mac is acceptable
            MAC_checker(wifiConfig.reciver) #calls the mac parse function
            for x in range (3):
                wifiConfig.recieverErrors[x] = MACErrors.error[x]
            CMPErrorReset()

            #Checks if the transmitter mac is acceptable
            MAC_checker(wifiConfig.transmitter)
            for x in range (3):
                wifiConfig.transmitterErrors[x] = MACErrors.error[x]
            CMPErrorReset()

            #Checks if the destination mac is acceptable
            MAC_checker(wifiConfig.destination)
            for x in range (3):
                wifiConfig.destinationErrors[x] = MACErrors.error[x]
            CMPErrorReset()

            #Checks if the source mac is acceptable
            MAC_checker(wifiConfig.source)
            for x in range (3):
                wifiConfig.sourceErrors[x] = MACErrors.error[x]
            CMPErrorReset()

        #arp error checking
        if Config.ARP[1] == 1:
            IP_checker(arpConfig.senderip) #calls the ip parse function
            arpConfig.iperror[0] = IPErrors.error[0]
            arpConfig.iperror[1] = IPErrors.error[1]
            MAC_checker(arpConfig.sendermac) #calls the mac parse function
            for x in range (3):
                arpConfig.macerror[x] = MACErrors.error[x]
            CMPErrorReset()

            IP_checker(arpConfig.targetip) #calls the ip parse function
            arpConfig.diperror[0] = IPErrors.error[0]
            arpConfig.diperror[1] = IPErrors.error[1]
            MAC_checker(arpConfig.targetmac) #calls the mac parse function
            for x in range (3):
                arpConfig.dmacerror[x] = MACErrors.error[x]
            CMPErrorReset()

        if Config.IP[1] == 1:
            IP_checker(ipConfig.destinationIp) #calls the ip parse function
            ipConfig.iperror[0] = IPErrors.error[0]
            ipConfig.iperror[1] = IPErrors.error[1]

            IP_checker(ipConfig.sourceIp) #calls the ip parse function
            ipConfig.diperror[0] = IPErrors.error[0]
            ipConfig.diperror[1] = IPErrors.error[1]
            CMPErrorReset()
        
        if Config.ICMP[1] == 1:
            CMPErrorReset()
            IP_checker(icmpConfig.ip) #calls the ip parse function
            icmpConfig.iperror[0] = IPErrors.error[0]
            icmpConfig.iperror[1] = IPErrors.error[1]
            MAC_checker(icmpConfig.mac) #calls the mac parse function
            icmpConfig.macerror[0] = MACErrors.error[0]
            icmpConfig.macerror[1] = MACErrors.error[1]
            icmpConfig.macerror[2] = MACErrors.error[2]
            icmpConfig.macerror[3] = MACErrors.error[3]
            CMPErrorReset()
            MAC_checker(icmpConfig.dmac) #calls the mac parse function
            icmpConfig.dmacerror[0] = MACErrors.error[0]
            icmpConfig.dmacerror[1] = MACErrors.error[1]
            icmpConfig.dmacerror[2] = MACErrors.error[2]
            icmpConfig.dmacerror[3] = MACErrors.error[3]
            IP_checker(icmpConfig.dip)
            icmpConfig.diperror[0] = IPErrors.error[0]
            icmpConfig.diperror[1] = IPErrors.error[1]
            CMPErrorReset()

        if Config.RIP[1] == 1:
            CMPErrorReset()
            IP_checker(ripConfig.ResponseIP) #calls the ip parse function
            ripConfig.ipError[0] = IPErrors.error[0]
            ripConfig.ipError[1] = IPErrors.error[1]
            CMPErrorReset()

        if Config.OSPF[1] == 1:
            CMPErrorReset()
            IP_checker(ospfConfig.mask)
            ospfConfig.maskError[0] = IPErrors.error[0]
            ospfConfig.maskError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(ospfConfig.sourcerouterError)
            ospfConfig.sourcerouterError[0] = IPErrors.error[0]
            ospfConfig.sourcerouterError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(ospfConfig.backuprouterError)
            ospfConfig.backuprouterError[0] = IPErrors.error[0]
            ospfConfig.backuprouterError[1] = IPErrors.error[1]
            CMPErrorReset()

        if  Config.UDP[1] == 1:
            IP_checker(udpConfig.ip)
            udpConfig.ipError[0] = IPErrors.error[0]
            udpConfig.ipError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(udpConfig.dip)
            udpConfig.dipError[0] = IPErrors.error[0]
            udpConfig.dipError[1] = IPErrors.error[1]
            CMPErrorReset()

        if  Config.TCP[1] == 1:
            IP_checker(tcpConfig.ip)
            tcpConfig.ipError[0] = IPErrors.error[0]
            tcpConfig.ipError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(tcpConfig.dip)
            tcpConfig.dipError[0] = IPErrors.error[0]
            tcpConfig.dipError[1] = IPErrors.error[1]
            CMPErrorReset()

        if Config.SOCKS[1] == 1:
            IP_checker(socksConfig.DIP)
            socksConfig.ipError[0] = IPErrors.error[0]
            socksConfig.ipError[1] = IPErrors.error[1]
            CMPErrorReset()

        if Config.DHCP[1] == 1:
            IP_checker(dhcpConfig.dip)
            dhcpConfig.dipError[0] = IPErrors.error[0]
            dhcpConfig.dipError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(dhcpConfig.ReqIP)
            dhcpConfig.reqError[0] = IPErrors.error[0]
            dhcpConfig.reqError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(dhcpConfig.DomainIP)
            dhcpConfig.domainError[0] = IPErrors.error[0]
            dhcpConfig.domainError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(dhcpConfig.RouterIP)
            dhcpConfig.RouterError[0] = IPErrors.error[0]
            dhcpConfig.RouterError[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(dhcpConfig.SubnetMask)
            dhcpConfig.maskError[0] = IPErrors.error[0]
            dhcpConfig.maskError[1] = IPErrors.error[1]
            CMPErrorReset()

        #Still WIP Ftp
        if Config.FTP[1] == 1:
            IP_checker(ftpConfig.ip)
            ftpConfig.iperror[0] = IPErrors.error[0]
            ftpConfig.iperror[1] = IPErrors.error[1]
            CMPErrorReset()
            IP_checker(ftpConfig.dip)
            ftpConfig.diperror[0] = IPErrors.error[0]
            ftpConfig.diperror[1] = IPErrors.error[1]
            CMPErrorReset()

        if Config.DNS[1] == 1:
            IP_checker(dnsConfig.dip)
            dnsConfig.dipError[0] = IPErrors.error[0]
            dnsConfig.dipError[1] = IPErrors.error[1]
            CMPErrorReset
        
        #After All The Errors Have been loaded correctly, they are then tested.
        error_Popup = Toplevel()
        error_Popup.title("Packet Status")

        #If there is a single Error then config.Protocol first array will be loaded with a 1 meaning that is has an Error

        if ((int(icmpConfig.macerror[0]) > 0 or int(icmpConfig.macerror[1]) > 0 or  int(icmpConfig.macerror[2]) > 0 or int(icmpConfig.macerror[3]) > 0 or int(icmpConfig.iperror[0]) > 0 or int(icmpConfig.iperror[1]) > 0) or
        (int(icmpConfig.dmacerror[0]) > 0 or int(icmpConfig.dmacerror[1]) > 0 or  int(icmpConfig.dmacerror[2]) > 0 or int(icmpConfig.dmacerror[3]) > 0 or int(icmpConfig.diperror[0]) > 0 or int(icmpConfig.diperror[1]) > 0)):
                Config.ICMP[0] = 1

        if ((int(ethernetConfig.smacerror[0]) > 0 or int(ethernetConfig.smacerror[1]) > 0 or  int(ethernetConfig.smacerror[2]) > 0 or int(ethernetConfig.smacerror[3]) > 0)  or
            (int(ethernetConfig.dmacerror[0]) > 0 or int(ethernetConfig.dmacerror[1]) > 0 or  int(ethernetConfig.dmacerror[2]) > 0 or int(ethernetConfig.dmacerror[3]) > 0)):
                Config.Ethernet[0] = 1
    
        if ((int(wifiConfig.reciverErrors[0]) > 0 or int(wifiConfig.reciverErrors[1]) > 0 or  int(wifiConfig.reciverErrors[2]) > 0 or int(wifiConfig.reciverErrors[3]) > 0)  or
            (int(wifiConfig.transmitterErrors[0]) > 0 or int(wifiConfig.transmitterErrors[1]) > 0 or  int(wifiConfig.transmitterErrors[2]) > 0 or int(wifiConfig.transmitterErrors[3]) > 0) or
            (int(wifiConfig.sourceErrors[0]) > 0 or int(wifiConfig.sourceErrors[1]) > 0 or  int(wifiConfig.sourceErrors[2]) > 0 or int(wifiConfig.sourceErrors[3]) > 0)  or
            (int(wifiConfig.destinationErrors[0]) > 0 or int(wifiConfig.destinationErrors[1]) > 0 or  int(wifiConfig.destinationErrors[2]) > 0 or int(wifiConfig.destinationErrors[3]) > 0) or 
            (int(wifiConfig.bssErrors[0]) > 0 or int(wifiConfig.bssErrors[1]) > 0 or  int(wifiConfig.bssErrors[2]) > 0 or int(wifiConfig.bssErrors[3]) > 0)):
                Config.Wifi[0] = 1


        if ((int(arpConfig.macerror[0]) > 0 or int(arpConfig.macerror[1]) > 0 or  int(arpConfig.macerror[2]) > 0 or int(arpConfig.macerror[3]) > 0 or int(arpConfig.iperror[0]) > 0 or int(arpConfig.iperror[1]) > 0) or
        (int(arpConfig.dmacerror[0]) > 0 or int(arpConfig.dmacerror[1]) > 0 or  int(arpConfig.dmacerror[2]) > 0 or int(arpConfig.dmacerror[3]) > 0 or int(arpConfig.diperror[0]) > 0 or int(arpConfig.diperror[1]) > 0)):
                Config.ARP[0] = 1

        if ((int(ipConfig.iperror[0]) > 0 or int(ipConfig.iperror[1]) > 0) or
        (int(ipConfig.diperror[0]) > 0 or int(ipConfig.diperror[1]) > 0)):
                Config.IP[0] = 1

        if ((int(ripConfig.ipError[0]) > 0 or int(ripConfig.ipError[1]) > 0)):
            Config.RIP[0] = 1

        if ((int(ospfConfig.sourcerouterError[0]) > 0 or int(ospfConfig.sourcerouterError[1]) > 0) or
        (int(ospfConfig.backuprouterError[0]) > 0 or int(ospfConfig.backuprouterError[1]) > 0) or
        (int(ospfConfig.maskError[0]) > 0 or int(ospfConfig.maskError[1]) > 0)):
                Config.OSPF[0] = 1
        
        if ((int(udpConfig.ipError[0]) > 0 or int(udpConfig.ipError[1]) > 0) or
        (int(udpConfig.dipError[0]) > 0 or int(udpConfig.dipError[1]) > 0)):
                Config.UDP[0] = 1

        if ((int(tcpConfig.ipError[0]) > 0 or int(tcpConfig.ipError[1]) > 0) or
        (int(tcpConfig.dipError[0]) > 0 or int(tcpConfig.dipError[1]) > 0)):
                Config.TCP[0] = 1
        
        #Place holder error follow the same syntax
        if ((int(socksConfig.ipError[0]) > 0 or int(socksConfig.ipError[1]) > 0)):
                Config.SOCKS[0] = 1

        if ((int(dhcpConfig.dipError[0]) > 0 or int(dhcpConfig.dipError[1]) > 0) or
        (int(dhcpConfig.reqError[0]) > 0 or int(dhcpConfig.reqError[1]) > 0) or
        (int(dhcpConfig.domainError[0]) > 0 or int(dhcpConfig.domainError[1]) > 0) or
        (int(dhcpConfig.RouterError[0]) > 0 or int(dhcpConfig.RouterError[1]) > 0) or
        (int(dhcpConfig.maskError[0]) > 0 or int(dhcpConfig.maskError[1]) > 0)):
                Config.DHCP[0] = 1
        
        if ((int(ftpConfig.iperror[0]) > 0 or int(ftpConfig.iperror[1]) > 0) or
        (int(ftpConfig.diperror[0]) > 0 or int(ftpConfig.diperror[1]) > 0)):
                Config.FTP[0] = 1


        if ((int(dnsConfig.dipError[0]) > 0 or int(dnsConfig.dipError[1]) > 0)):
            Config.DNS[0] = 1


        #Error Labels are called depending on the previous outcomes
        if Config.Ethernet[0] != 0:
            ethernetErrorLabel = Label(error_Popup, text="Ethernet ERROR: There was an error in your Ethernet Configuration.")
            ethernetErrorLabel.pack()

        if Config.Wifi[0] != 0:
            WiFiErrorLabel = Label(error_Popup, text="WiFi ERROR: There was an error in your WiFi Configuration.")
            WiFiErrorLabel.pack()

        if Config.ARP[0] != 0:
            arpErrorLabel = Label(error_Popup, text="ARP ERROR: There was an error in your ARP Configuration.")
            arpErrorLabel.pack()
        
        if Config.IP[0] != 0:
            IPErrorLabel = Label(error_Popup, text="IP ERROR: There was an error in your IP Configuration.")
            IPErrorLabel.pack()

        if Config.ICMP[0] != 0:
            icmpErrorLabel = Label(error_Popup, text="ICMP ERROR: There was an error in your ICMP Configuration.")
            icmpErrorLabel.pack()

        if Config.RIP[0] != 0:
            ripErrorLabel = Label(error_Popup, text="RIP ERROR: There was an error in your RIP Configuration.")
            ripErrorLabel.pack()

        if Config.OSPF[0] != 0:
            ospfErrorLabel = Label(error_Popup, text="OSPF ERROR: There was an error in your OSPF Configuration.")
            ospfErrorLabel.pack()

        if Config.UDP[0] != 0:
            udpErrorLabel = Label(error_Popup, text="UDP ERROR: There was an error in your UDP Configuration.")
            udpErrorLabel.pack()

        if Config.TCP[0] != 0:
            tcpErrorLabel = Label(error_Popup, text="TCP ERROR: There was an error in your TCP Configuration.")
            tcpErrorLabel.pack()

        if Config.SOCKS[0] != 0:
            socksErrorLabel = Label(error_Popup, text="SOCKS ERROR: There was an error in your SOCKS Configuration.")
            socksErrorLabel.pack()

        if Config.DHCP[0] != 0:
            dhcpErrorLabel = Label(error_Popup, text="DHCP ERROR: There was an error in your DHCP Configuration.")
            dhcpErrorLabel.pack()

        if Config.DNS[0] != 0:
            DNSErrorLabel = Label(error_Popup, text="DNS ERROR: There was an error in your DNS Configuration.")
            DNSErrorLabel.pack()


        #If There are Zero Errors in the configuration (Currently a big If statement) then the data is written and then backend is called
        if (Config.Ethernet[0] == 0 and Config.Wifi[0] == 0 and Config.ARP[0] == 0 and Config.IP[0] == 0 and Config.ICMP[0] == 0 and
            Config.RIP[0] == 0 and Config.OSPF[0] == 0 and Config.UDP[0] == 0 and Config.TCP[0] == 0 and Config.SOCKS[0] == 0 and Config.NetBIOS[0] == 0 and
            Config.SMB[0] == 0 and Config.TLS[0] == 0 and Config.SSH[0] == 0 and Config.DHCP[0] == 0 and Config.TELNET[0] == 0 and Config.IRC[0] == 0 and
            Config.HTTP[0] == 0 and Config.HTTPS[0] == 0 and Config.DNS[0] == 0):
                PcapStatusLabel = Label(error_Popup, text="The Pcap Creation was successful, find your generated pcap at /placeholder ")
                PcapStatusLabel.pack()
                pcapWrite() #Writes to Data.txt
                os.system(puppet_backend)

# This loops all the layers buttons. Done to save time and add modular programming capability.

#Lists of Lists of Protocols used at differnet layers (easy to add too = modular)
layersArray = [
"null", # Done as Tkinter will cut off the first option Array
#Layer 2
["Ethernet",
"WIFI (IEEE 802.11)",
"ARP",],
#Layer 3
["ICMP",
"RIP",
"OSPF",
"IP"],
#Layer 4
["UDP",
"TCP",],
#Layer 5
["SOCKS",
"NetBIOS",
"SMB",],
 #Layer six
["TLS/SSL",],
 #Layer Seven
["DHCP",
 "TELNET",
 "IRC",
 "FTP",
 "HTTP",
 "HTTPS",
 "DNS"]
]

    

TrafficSizeDone = Button(TrafficSizeFrame, text="✓", command=SizeLoader)
TrafficSizeDone.place(x=75, y=140)


#Setting the titles and general outline of the GUI

#setting variables as string
layerTitle2 = StringVar()
layerTitle3 = StringVar()
layerTitle4 = StringVar()
layerTitle5 = StringVar()
layerTitle6 = StringVar()
layerTitle7 = StringVar()

 #setting the titles
layerTitle2.set("Layer 2")
layerTitle3.set("Layer 3")
layerTitle4.set("Layer 4")
layerTitle5.set("Layer 5")
layerTitle6.set("Layer 6")
layerTitle7.set("Layer 7")


# setting the buttons

pcapCbutton = Button(master, text = "Create Pcap", command=createPcap, height=7, width=37, borderwidth=1, relief=SOLID)
pcapCbutton.place(x=510,y=463)


 #setting the option menus
Layerdrop2 = OptionMenu(lconfig_Frame, layerTitle2, *layersArray[1], command=layer2_Displayer)
Layerdrop3 = OptionMenu(lconfig_Frame, layerTitle3, *layersArray[2], command=layer3_Displayer)
Layerdrop4 = OptionMenu(lconfig_Frame, layerTitle4, *layersArray[3], command=layer4_Displayer)
Layerdrop5 = OptionMenu(lconfig_Frame, layerTitle5, *layersArray[4], command=layer5_Displayer)
Layerdrop6 = OptionMenu(lconfig_Frame, layerTitle6, *layersArray[5], command=layer6_Displayer)
Layerdrop7 = OptionMenu(lconfig_Frame, layerTitle7, *layersArray[6], command=layer7_Displayer)

# setting the configurations 
Layerdrop2.config(width=5, padx=68, pady=5, height=4, font=("Arial", 12))
Layerdrop3.config(width=5, padx=68, pady=5, height=4, font=("Arial", 12))
Layerdrop4.config(width=5, padx=68, pady=5, height=4, font=("Arial", 12))
Layerdrop5.config(width=5, padx=68, pady=5, height=4, font=("Arial", 12))
Layerdrop6.config(width=5, padx=68, pady=5, height=4, font=("Arial", 12))
Layerdrop7.config(width=5, padx=68, pady=5, height=4, font=("Arial", 12))

# setting the postioning
Layerdrop2.grid(row = (2), column = 0, sticky = W)
Layerdrop3.grid(row = (3), column = 0, sticky = W)
Layerdrop4.grid(row = (4), column = 0, sticky = W)
Layerdrop5.grid(row = (5), column = 0, sticky = W)
Layerdrop6.grid(row = (6), column = 0, sticky = W)
Layerdrop7.grid(row = (7), column = 0, sticky = W)

# setting the button postioning

#Program Finished

master.mainloop()
