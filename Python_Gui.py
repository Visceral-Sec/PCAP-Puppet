import os
from tkinter import *  # Importing tkinter

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    PCAP_PUPPET GUI    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frames/Master ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#https://www.youtube.com/watch?v=YXPyB4XeYLA

#Tkinter works a bit like HTML, but instead of objects etc we have widgets

master = Tk() #This is the root of the entire gui
master.geometry('779x582') # sets default size
master.title("PCAP PUPPET")
#master.resizable(width=False, height=False) # prevents the size from being adjusted

#change this depending on path
path = "Project"

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

#


#Frame for Pcap History/Current Traffic Configuraiton
cConfigLabel = LabelFrame(master, text = "", width=268, height=195)
cConfigLabel.place(x=510, y= 268)

#Frame for Traffic Configuration
TrafficConfigFrame = LabelFrame(master, text = "", width=160, height=174)
TrafficConfigFrame.place(x = 618, y = 66)

#Traffic Size Frame

TrafficSizeFrame = LabelFrame(master, text = "", width=108, height=174)
TrafficSizeFrame.place(x = 511, y = 66)


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

#History
CurrentTraffic = Label(master, text = "Current Traffic", font=("Arial", 16), borderwidth=1,  relief="solid", width=22)
CurrentTraffic.place(x = 510, y = 240)


TrafficConfiguration = Label(master, text = "Traffic  Configuration", font=("Arial", 13), borderwidth=1,  relief="solid",)
TrafficConfiguration.place(x = 617, y = 43)


#Pcap Specific Settings

TrafficConfiguration = Label(master, text = " Traffic Size   ", font=("Arial", 13), borderwidth=1,  relief="solid",)
TrafficConfiguration.place(x = 510, y = 43)

SizeEntry = Entry(TrafficSizeFrame, width=4)
SizeEntry.place(x=70, y=5)

SizeEntryLabel = Label(TrafficSizeFrame,text="Traffic Size:")
SizeEntryLabel.place(x=1, y=5)

#### Code to be organised once Matthew is finished so I can combine it (cba to do pull requests)

class LocationConfiguration:
        size = 1
    



####
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This all classes. Currently, Classes are used for holding user inputs as well as potential errors.
# Classes are used because they have a wider scope than the function they are in, so they are used for returning values.

#Layer 2 Classes
class ethernetConfig:
    placeholder = ""
class tokenringConfig:
    placeholder = ""
class WIFI:
    placeholder = ""
class arpConfig:
    icmptext = ""
    ip = ""
    mac = ""
    dip = ""
    dmac = ""
    macerror = [0,0,0,0]
    dmacerror = [0,0,0,0]
    iperror = [0,0]
    diperror = [0,0]
    size = [0]


#Layer 3 Classes
class natConfig:
    placeholder = ""
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
    size = [0]
    Text = ""
class ripConfig:
    placeholder = ""
class OSPF:
    placeholder = ""
class IP:
    placeholder = ""

#Layer 4 UDP/TCP
class udpConfig:
    placeholder = ""
class tcpConfig:
    placeholder = ""

#Layer 5

class socksConfig:
    placeholder = ""
class netbiosConfig:
    placeholder = ""
class smbConfig:
    placeholder = ""

#layer 6

class tlsConfig:
    placeholder = ""
class sslConfig:
    placeholder = ""
class sshConfig:
    placeholder = ""


#Layer 7

class soapConfig:
    placeholder = ""
class dhcpConfig:
    placeholder = ""
class telnetConfig:
    placeholder = ""
class ircConfig:
    command = ""
    message = ""
    Name = ""
    size = ""
class ftpConfig:
    ip = ""
    dip = ""
    port = ""
    data = ""
    file = ""
    size = ""
    type = [0,0]
class httpConfig:
    URL = ""
    UserAgent = ""
    PostUri = ""
    GetUri = ""
    GetReferrer = ""
    PostData = ""
    size = ""
class httpsConfig:
    URL = ""
    UserAgent = ""
    PostUri = ""
    GetUri = ""
    GetReferrer = ""
    PostData = ""
    size = ""
    SSLKey = ""
class dnsConfig:
    dip = ""
    Cport = ""
    Type = ""
    Class = ""
    AnswerIP = ""
    TIL = ""
    AnswerName = ""

# Misc:

class TrafficSize:
    size = ""

    #Used for configuring where to put spinboxes (Locations change depending on previous choices (e.g dynamic locations))
class LocationConfiguration:
        size = 1
        x = 0
        y = 0
        xl = 0
        yl = 0

#These Classes exist for error checking purposes and checks if the protocol is being used
class Config:
    #Layer 2
    #First Array indicates their is an error
    # Second array indicates if it's been chosen
    # third array value indicates if it's been displayed (to prevent from it display again)
    Ethernet=[0,0,0]
    TokenRing=[0,0,0]
    Wifi=[0,0,0]
    #Layer 3
    NAT=[0,0,0]
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

class IPErrors:
    error = [0,0]
class MACErrors:
    error = [0,0,0,0]

class PcapConfig:
    wiresharkVER = "3.4.5"

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This contains every function used in the program.
# layer 3 is now the prefered method. Issues with layer 2 were only solved using a new geometry manage (.place()) which allows for more precise placement.
#This function writes to a txt doc which the c function will use to create the pcap
def pcapWrite():
    #The library to write to files is very similar to that of C file.io library
    pcap_path = os.path.join(path, "PlaceholderPcap.txt")
    f = open(pcap_path, "w")

    f.write("meta\n") 
    f.write(PcapConfig.wiresharkVER + "\n")
    #add more meta information here
    f.write("end\n")

    f.write("packet data\n")

    #if ICMP is selected.
    if Config.ICMP[1] == 1:
        f.write("ICMP\n")
        # add icmp data etc here
        f.write(icmpConfig.ip + "\n")
        f.write(icmpConfig.mac + "\n")
        f.write(icmpConfig.dip + "\n")
        f.write(icmpConfig.dmac + "\n")
        f.write(icmpConfig.Text +"\n")
        f.write("end\n")

    if Config.ARP[1] == 1:
        f.write("ARP\n")
        # add icmp data etc here
        f.write(arpConfig.ip + "\n")
        f.write(arpConfig.mac + "\n")
        f.write(arpConfig.dip + "\n")
        f.write(arpConfig.dmac + "\n")
        f.write("end\n")

    f.write("end\n")

def LocationConfig():
    placed = 0 
    print(LocationConfiguration.size)
    LocationConfiguration.x = 0 
    LocationConfiguration.y = 0
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



    #ICMP Errors
    Config.ICMP[0] = 0
    icmpConfig.macerror[0] = 0
    icmpConfig.macerror[1] = 0
    icmpConfig.macerror[2] = 0
    icmpConfig.macerror[3] = 0
    icmpConfig.iperror[0] = 0
    icmpConfig.iperror[1] = 0 
    
    #ARP Errors
    #ICMP Errors
    Config.ARP[0] = 0
    arpConfig.macerror[0] = 0
    arpConfig.macerror[1] = 0
    arpConfig.macerror[2] = 0
    icmpConfig.macerror[3] = 0
    icmpConfig.iperror[0] = 0
    icmpConfig.iperror[1] = 0

def CMPErrorRest():     # This resets each compare error (This is to prevent previous protocol errors effecting other checks)
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
    print('Legit IP given')

#Slight edited by Archer, but mainly coded by Matt. This function checks the validatility of the MAC.
def MAC_checker(MAC): # Coded by Matt
    acceptable_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ':']
    acceptable_placesforcolon = [2, 5, 8, 11, 14]
    MAC = MAC.lower()
    if len(MAC) != 17: #Num of chars in MAC address is 17
        print('Incorrect MAC length')
        MACErrors.error[0] = 1
    if MAC[2] != ':' or MAC[5] != ':' or MAC[8] != ':' or MAC[11] != ':' or MAC[14] != ':': #If no colon at specific points
        print('Not enough colons')
        MACErrors.error[1] = 2
    for i in range(len(MAC)):
        if MAC[i] == ':' and i not in acceptable_placesforcolon: #Colon not used to identify address, only chars and digits
            print('Colon(s) not at an acceptable place(s)')
            MACErrors.error[2] = 3
    for i in range(len(MAC)):
        if MAC[i] not in acceptable_chars: #Only letters numbers and colons excepted
            print('Mac address contains unacceptable characters')
            MACErrors.error[3] = 4
    return(0) # Edited to allow for easier user parsing


# Layer 2 Display function. (Needs to be updated as of 15/05/2021)
def layer2_Displayer(l): # The purpose of this functions is that every layer menu option will call one of this funcitons followed with the selection option. In this case that is L.
    layer2_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration") # This then prints the label heading as the name of the chosen protocol + the option
    layer2_Frame.place(x=50, y=50)# Postioning

    # currently the only options we have is the ip entry setting. (That is why they are all protcol + labled_IP)
    eth_Ip = Entry(layer2_Frame) 
    token_Ip = Entry(layer2_Frame, text="IP") # text won't show up apparently
    wifi_Ip = Entry(layer2_Frame, text="IP") 
    arp_Ip = Entry(layer2_Frame, text="IP")

def layer3_Displayer(l):
    #Defining the tkinter type
    layer3_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration", width=284, height=529)    # Using .place geomotry manager under the label frame in order to position correctly
    layer3_Frame.place(x=217, y=0)
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
    # Done function. This concatenates all of the octects into 2 strings and then loads into the class mentioned earlier.
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
        icmpConfig.Text = icmpText.get(1.0,255.0)
        Config.ICMP[1] = 1
        History_Displayer()
        
        
    #Button that links the previous function. 
    if l == "ICMP":
        icmpb = Button(layer3_Frame, text = "✓", command=icmpdone,)
        icmpPingData = Label(layer3_Frame, text="ICMP Ping Data:")
        icmpText = Text(layer3_Frame, height=10, width=33)
        icmpb.place(x=175, y=475, width=100) # postioning on the button
        icmpText.place(x=5, y=140)
        icmpPingData.place(x=5, y=120)


    def arpdone():
        arpConfig.ip = ""
        arpConfig.mac = ""
        colon = ":"
        dot = "."
        ip = ip1.get() + dot + ip2.get() + dot + ip3.get() + dot + ip4.get() # concatating all of the octects
        mac = mac1.get() + colon + mac2.get() + colon + mac3.get() + colon + mac4.get() + colon + mac5.get() + colon + mac6.get()
        dip = ip5.get() + dot + ip6.get() + dot + ip7.get() + dot + ip8.get()
        dmac = mac7.get() + colon + mac8.get() + colon + mac9.get() + colon + mac10.get() + colon + mac11.get() + colon + mac12.get()
        arpConfig.ip = ip
        arpConfig.mac = mac
        arpConfig.dip = dip
        arpConfig.dmac = dmac
        Config.ARP[1] = 1
        History_Displayer()
     
    if l == "ARP":
        arpb = Button(layer3_Frame, text = "✓", command=arpdone)
        arpb.place(x=220, y=30) # postioning on the button


    if l == layersArray[2][0]: #nat
        nat_ip = Entry(layer3_Frame)
        
    if l == layersArray[2][1]: #icmp
        icmp_ip = Entry(layer3_Frame)
        
    if l == layersArray[2][2]: #rip
        rip_Ip = Entry(layer3_Frame)


    if l == layersArray[2][3]: #ospf
        ospf_Ip = Entry(layer3_Frame)


    if l == layersArray[2][4]: #ip
        ip_Ip = Entry(layer3_Frame)

def layer4_Displayer(l):
    layer4_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration")
    layer4_Frame.place(x=100, y=50)
    udp_Ip = Entry(layer4_Frame)
    tcp_Ip = Entry(layer4_Frame)

    if l == layersArray[3][0]:
        udp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)  

    if l == layersArray[3][1]:
        tcp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

def layer5_Displayer(l):
    layer5_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration")
    layer5_Frame.place(x=100, y=50)
    socks_Ip = Entry(layer5_Frame)
    netBIOS_Ip = Entry(layer5_Frame)
    smb_Ip = Entry(layer5_Frame)

    if l == layersArray[4][0]:
        socks_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)  

    if l == layersArray[4][1]:
        netBIOS_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[4][2]:
        smb_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

def layer6_Displayer(l):    
    layer6_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration")
    layer6_Frame.place(x=100, y=50)

    tls_Ip = Entry(layer6_Frame)
    ssl_Ip = Entry(layer6_Frame)
    ftp_Ip = Entry(layer6_Frame)
    ssh_Ip = Entry(layer6_Frame)


    if l == layersArray[5][0]:
        tls_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[5][1]:
        ssl_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[5][2]:
        ftp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)
    
    if l == layersArray[5][3]:
        ssh_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

#Loads the overall size of the traffic (The entry box)
def SizeLoader():
    TrafficSize.size = SizeEntry.get()

def layer7_Displayer(l):
    layer7_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration", width=284, height=529)
    layer7_Frame.place(x=217, y=0)
    soap_Ip = Entry(layer7_Frame)
    dhcp_Ip = Entry(layer7_Frame)


    if l == "SOAP":
        soap_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == "DHCP":
        dhcp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)
    
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
        

        TelnetCommandText = Label(layer7_Frame, text="Telnet Commands:")
        TelnetCommandVar = StringVar(layer7_Frame)
        TelnetCommandVar.set("COMMAND:")
        TelnetCommand = OptionMenu(layer7_Frame, TelnetCommandVar, "SE","NOP","DM","BRK","IP","AO","AYT","EC","GA","SB","WILL","WONT","DO","DON'T","IAC")
        TelnetCommand.place(x=4,y=250)
        TelnetCommandText.place(x=4,y=230)


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
            dnsConfig.Type = DNSType.get()
            dnsConfig.Class = DNSClass.get()
            dnsConfig.Cport= DNSCommunicationPort.get()
            dnsConfig.AnswerIP = Ansip1.get() + dot + Ansip2.get() + dot + Ansip3.get() + dot + Ansip4.get()
            dnsConfig.TIL = DNSTime.get()
            dnsConfig.AnswerName = DNSName.get()
            History_Displayer()
        dnsb = Button(layer7_Frame, text = "✓", command=dnsdone)
        dnsb.place(x=175, y=475, width=100) 

















# Sets the History and the Size Configuration
def History_Displayer():
    icmpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size,width=4)
    arpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size,width=4)
    ftpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size,width=4)
    httpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size,width=4)
    httpsSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size,width=4)
    ircSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size,width=4)
    #Loads the specific Sizes. (Has to be within this function otherwise TrafficSize won't load)
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

    TrafficSizeButton = Button(TrafficConfigFrame, text = "✓", command=TrafficSize_Loader)
    TrafficSizeButton.place(x=127,y=140)

    #Displays ICMP configuration
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
            Popupdmac = Label(PopupLabel, text=("Destination Mac: " + icmpConfig.mac))
            Popuptext = Label(PopupLabel, text=("ICMP Ping Data: " + icmpConfig.Text))
            PopupIP.pack()
            PopupDIP.pack()
            Popupmac.pack()
            Popupdmac.pack()
            Popuptext.pack()

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
            PopupIP = Label(PopupLabel, text=("Source IP: " + arpConfig.ip))
            PopupDIP = Label(PopupLabel, text=("Destination IP: " + arpConfig.dip))
            Popupmac = Label(PopupLabel, text=("Source Mac: " + arpConfig.mac))
            Popupdmac = Label(PopupLabel, text=("Destination Mac: " + arpConfig.mac))
            PopupIP.pack()
            PopupDIP.pack()
            Popupmac.pack()
            Popupdmac.pack()

        arpHistoryButton = Button(arpHistory, text = "INFO", width=3, height=0, command=ARPDisplay())
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
    
    if Config.HTTP[1] == 1 and Config.HTTP[2] == 0:
        Config.HTTP[2] = 1
        httpsHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        httpsHistory.place(x=0, y=(((LocationConfiguration.size - 1) * 30) + 1))
        LocationConfig()
        httpsHistoryLabel = Label(httpsHistory, text = "HTTPS", font=("Arial", 16), borderwidth=1,  relief="solid",)
        httpsHistoryLabel.place(x=0, y=0)
        placed = 0
        def httpsDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current HTTPS Configuration")
            PopupLabel = LabelFrame(Popup, text="HTTP Configuration", width=250, height=250)
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
        placed = 0
        def ircDisplay(): #Info Button displays all of the currently chosen configuration
            Popup = Toplevel()
            Popup.title("Current IRC Configuration")
            PopupLabel = LabelFrame(Popup, text="IRC Configuration", width=250, height=250)
            PopupLabel.pack()
            PopupName = Label(PopupLabel, text=("User Name: " + ircConfig.Name))
            PopupMessage = Label(PopupLabel, text=("IRC Message" + ircConfig.message))
            PopupCommand = Label(PopupLabel, text=("IRC Commadn" + ircConfig.command))
            PopupName.pack()
            PopupMessage.pack()
            PopupCommand.pack()
        ircHistoryButton = Button(IRCHistory, text = "INFO", width=3, height=0, command=ircDisplay)
        ircHistoryButton.place(x=227, y=1)
        ircSpinboxLabel = Label(TrafficConfigFrame, text="IRC:")
        ircSpinboxLabel.place(x=LocationConfiguration.xl, y=LocationConfiguration.yl)
        ircSpinbox.place(x=LocationConfiguration.x, y=LocationConfiguration.y)
#Function on the "create Pcap button", checks for errors, then calls the main writing function (PcapWrite())
def createPcap():
    ErrorReset()   # clears all previous error checks from previous creations
    #Checker functions (This will be ran on pretty much every protocol, (Don't know how to make this more effective))
    # As tkinter doesn't like values being returned we have to use a place holder class to hold errors. This gets reset after each compare. (This allows for multiple protocols to use the error checking functions)
    if Config.ICMP[1] == 1:
        IP_checker(icmpConfig.ip) #calls the ip parse function
        icmpConfig.iperror[0] = IPErrors.error[0]
        icmpConfig.iperror[1] = IPErrors.error[1]
        IP_checker(icmpConfig.dip)
        icmpConfig.diperror[0] = IPErrors.error[0]
        icmpConfig.diperror[1] = IPErrors.error[1]
        MAC_checker(icmpConfig.mac) #calls the mac parse function
        icmpConfig.macerror[0] = MACErrors.error[0]
        icmpConfig.macerror[1] = MACErrors.error[1]
        icmpConfig.macerror[2] = MACErrors.error[2]
        icmpConfig.macerror[3] = MACErrors.error[3]
        MAC_checker(icmpConfig.dmac) #calls the mac parse function
        icmpConfig.dmacerror[0] = MACErrors.error[0]
        icmpConfig.dmacerror[1] = MACErrors.error[1]
        icmpConfig.dmacerror[2] = MACErrors.error[2]
        icmpConfig.dmacerror[3] = MACErrors.error[3]
        CMPErrorRest()




    if Config.ARP[1] == 1:
        IP_checker(arpConfig.ip) #calls the ip parse function
        arpConfig.iperror[0] = IPErrors.error[0]
        arpConfig.iperror[1] = IPErrors.error[1]
        MAC_checker(arpConfig.mac) #calls the mac parse function
        arpConfig.macerror[0] = MACErrors.error[0]
        arpConfig.macerror[1] = MACErrors.error[1]
        arpConfig.macerror[2] = MACErrors.error[2]
        arpConfig.macerror[3] = MACErrors.error[3]
        CMPErrorRest()


    error_Popup = Toplevel()
    error_Popup.title("Packet Status")
    #If statement checking if there any issues for the different protocols.
    #I'll add more of these once Matthew as finished adding some of the different protocols.
    
    #checks if both the dip/ip and mac/dmac are acceptable.
    if (int(icmpConfig.macerror[0]) > 0 or int(icmpConfig.macerror[1]) > 0 or  int(icmpConfig.macerror[2]) > 0 or int(icmpConfig.macerror[3]) > 0 or int(icmpConfig.iperror[0]) > 0 or int(icmpConfig.iperror[1]) > 0):
        if (int(icmpConfig.dmacerror[0]) > 0 or int(icmpConfig.dmacerror[1]) > 0 or  int(icmpConfig.dmacerror[2]) > 0 or int(icmpConfig.dmacerror[3]) > 0 or int(icmpConfig.diperror[0]) > 0 or int(icmpConfig.diperror[1]) > 0):
            Config.ICMP[0] = 1 #This sets the error 
    
    #Place holder error follow the same syntax

    if (int(arpConfig.macerror[0]) > 0 or int(arpConfig.macerror[1]) > 0 or  int(arpConfig.macerror[2]) > 0 or int(arpConfig.macerror[3]) > 0 or int(arpConfig.iperror[0]) > 0 or int(arpConfig.iperror[1]) > 0):
        if (int(icmpConfig.dmacerror[0]) > 0 or int(icmpConfig.dmacerror[1]) > 0 or  int(icmpConfig.dmacerror[2]) > 0 or int(icmpConfig.dmacerror[3]) > 0 or int(icmpConfig.diperror[0]) > 0 or int(icmpConfig.diperror[1]) > 0):
            Config.ARP[0] = 1 #This sets the error 



    if Config.ICMP[0] != 0:
        IcmpErrorLabel = Label(error_Popup, text="ICMP ERROR: There was an error in your ICMP Configuration.")
        IcmpErrorLabel.pack()
    if Config.ARP[0] != 0:
        arpErrorLabel = Label(error_Popup, text="ARP ERROR: There was an error in your ARP Configuration.")
        arpErrorLabel.pack()




#Final Check

    if Config.ICMP[0] == 0 and Config.ARP[0] == 0: 
        PcapStatusLabel = Label(error_Popup, text="The Pcap Creation was successful, find your generated pcap at /placeholder ")
        PcapStatusLabel.pack()
        pcapWrite()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Menus ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This loops all the layers buttons. Done to save time and add modular programming capability.

    #Lists of Lists of Protocols used at differnet layers (easy to add too = modular)
layersArray = [
"null", # hacky method to prevent stuff from not displaying, unsure why this is happening will ask finlay about this
#Layer 2
["Ethernet",
"Token Ring",
"WIFI (IEEE 802.11)",
"ARP"], 
#Layer 3
["NAT",
"ICMP",
"ARP",
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
 ["TLS",
 "SSL",
"FTP",
"SSH",],
 #Layer Seven
["SOAP",
 "DCHP",
 "TELNET",
 "IRC",
 "FTP",
 "HTTP",
 "HTTPS",
 "DNS"]
]


    

TrafficSizeDone = Button(TrafficSizeFrame, text="✓", command=SizeLoader)
TrafficSizeDone.place(x=75, y=140)



# THIS IS ABOMINATION THAT HURTS ME TO EVEN WRITE BUT IT'S THE ONLY WAY I CURRENTLY KNOW OF HOW TO ENSURE THAT EACH DROP DOWN MENU CAN CAUSE OPTIONS


# SERIOUSLY THIS WAY IS SOO PAINFUL TO LOOK AT BUT ONLY WAY I CURRENTLY KNOW OF TO GET IT TO WORK. Hopefully some insane python programmer can help us in the future (or maybe im just dumb)
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


# agony this was coded nicely with modular programming but unfornutely you can't do anything with the .get function if it's in a localised for statemnent therefore I need to hard code it all
# Adding variables with common protocols at each level




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    PCAP_PUPPET PYTHON       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~













master.mainloop()