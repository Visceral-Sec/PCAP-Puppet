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
lconfig_Frame.grid(row = (1), column = 0, sticky = W)

#Frame for Titles "Protocols"/"Configuration"/"PCAP Settings"
tConfig_Frame = Frame(master)
tConfig_Frame.grid(row = (0), column = 0, sticky = N)

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This all classes. Currently, Classes are used for holding user inputs as well as potential errors.
# Classes are used because they have a wider scope than the function they are in, so they are used for returning values.

class icmpConfig:
    icmptext = ""
    ip = ""
    mac = ""
    macerror = [0,0,0,0]
    iperror = [0,0]
    size = [0]

class arpConfig:
    icmptext = ""
    ip = ""
    mac = ""
    macerror = [0,0,0,0]
    iperror = [0,0]
    size = [0]

class TrafficSize:
    size = ""

#These Classes exist for error checking purposes and checks if the protocol is being used
class Config:
    #Layer 2
    Ethernet=[0,0]
    TokenRing=[0,0]
    Wifi=[0,0]
    #Layer 3
    NAT=[0,0]
    ICMP=[0,0]
    ARP=[0,0]
    RIP=[0,0]
    OSPF=[0,0]
    IP=[0,0]
    #Layer 4 
    UDP=[0,0]
    TCP=[0,0]
    #Layer 5 
    SOCKS=[0,0]
    NetBIOS=[0,0]
    SMB=[0,0]
    #Layer 6
    TLS=[0,0]
    SSL=[0,0]
    FTP=[0,0]
    SSH=[0,0]
    #Layer 7
    SOAP=[0,0]
    DHCP=[0,0]
    TELNET=[0,0]
    IRC=[0,0]
    FTP=[0,0]
    HTTP=[0,0]
    HTTPS=[0,0]
    DNS=[0,0]

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
        f.write("end\n")

    if Config.ARP[1] == 1:
        f.write("ARP\n")
        # add icmp data etc here
        f.write(arpConfig.ip + "\n")
        f.write(arpConfig.mac + "\n")
        f.write("end\n")

    f.write("end\n")

    

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
    layer2_Frame.grid(row = (2), column = 3, sticky = E) # Postioning

    # currently the only options we have is the ip entry setting. (That is why they are all protcol + labled_IP)
    eth_Ip = Entry(layer2_Frame) 
    token_Ip = Entry(layer2_Frame, text="IP") # text won't show up apparently
    wifi_Ip = Entry(layer2_Frame, text="IP") 
    arp_Ip = Entry(layer2_Frame, text="IP")

    # massive yandere dev if statement. (As far as I know switch statements are cringe in python and an If ladder works fine)
    # A benefit of using this method is that adding extra protocols is really easy

    if l == layersArray[1][0]: 
        eth_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)  # Just adds the grid. It's done this way so that differnet options can show up for different protocols
        
    if l == layersArray[1][1]:
        token_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[1][2]:
        wifi_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)
        
    if l == layersArray[1][3]:
        arp_Ip.grid(row = (1), column = 3, sticky = E,pady=25, padx=82)

def layer3_Displayer(l):
    #Defining the tkinter type
    layer3_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration", width=294, height=90)    # Using .place geomotry manager under the label frame in order to position correctly
    layer3_Frame.grid(row = (3), column = 3,)
    # defining the ip octect entires
    ip1 = Entry(layer3_Frame, width=2) #Octect 1 of the IP
    ip2 = Entry(layer3_Frame, width=2) #Octect 2 of the ip 
    ip3 = Entry(layer3_Frame, width=2) #Octect 3 of the ip 
    ip4 = Entry(layer3_Frame, width=2) #Octect 4 of the ip 
    dot1 = Label(layer3_Frame, text = ".") # Three dots seperating the fields
    dot2 = Label(layer3_Frame, text = ".")
    dot3 = Label(layer3_Frame, text = ".")

    # Defining the mac octect Entries
    mac1 = Entry(layer3_Frame, width=3)
    mac2 = Entry(layer3_Frame, width=3)
    mac3 = Entry(layer3_Frame, width=3) 
    mac4 = Entry(layer3_Frame, width=3)
    mac5 = Entry(layer3_Frame, width=3)
    mac6 = Entry(layer3_Frame, width=3)

    # The colons seperate the label
    colon1 = Label(layer3_Frame, text = ":")
    colon2 = Label(layer3_Frame, text = ":")
    colon3 = Label(layer3_Frame, text = ":")    
    colon4 = Label(layer3_Frame, text = ":")
    colon5 = Label(layer3_Frame, text = ":")   

    #Defining the text (like literally the words that say "IP:")
    iptext = Label(layer3_Frame, text = "IP:")
    mactext = Label(layer3_Frame, text = "MAC:")

    #Ip text postioning
    iptext.place(x=2,y=4) 
    #mac text postioning
    mactext.place(x=2,y=34) #mac text postioning

    #Placing all of the previously defined labels. using .place for more accurate location (This does take a while to do tho)
    ip1.place(x=20,y=5)     
    ip2.place(x=50,y=5)
    ip3.place(x=80,y=5)
    ip4.place(x=110,y=5)

    dot1.place(x=40,y=5)
    dot2.place(x=70,y=5)
    dot3.place(x=100,y=5)

    mac1.place(x=40,y=35)   
    mac2.place(x=70,y=35)
    mac3.place(x=100,y=35)
    mac4.place(x=130,y=35)
    mac5.place(x=160,y=35)
    mac6.place(x=190,y=35)

    colon1.place(x=60,y=35)
    colon2.place(x=90,y=35)
    colon3.place(x=120,y=35)
    colon4.place(x=150,y=35)
    colon5.place(x=180,y=35)
    # Done function. This concatenates all of the octects into 2 strings and then loads into the class mentioned earlier.
    def icmpdone():
        icmpConfig.ip = ""
        icmpConfig.mac = ""
        ipa = ip1.get() #a = string 1 = entry
        ipb = ip2.get()
        ipc = ip3.get()
        ipd = ip4.get()

        maca = mac1.get()
        macb = mac2.get()
        macc = mac3.get()
        macd = mac4.get()
        mace = mac5.get()
        macf = mac6.get()
        colon = ":"
        dot = "."
        ip = ipa + dot + ipb + dot + ipc + dot + ipd # concatating all of the octects
        mac = maca + colon + macb + colon + macc + colon + macd + colon + mace + colon + macf
        icmpConfig.ip = ip
        icmpConfig.mac = mac
        Config.ICMP[1] = 1
        History_Displayer()
        
        
    #Button that links the previous function. 
    if l == "ICMP":
        icmpb = Button(layer3_Frame, text = "✓", command=icmpdone,)
        icmpb.place(x=220, y=30) # postioning on the button


    def arpdone():
        arpConfig.ip = ""
        arpConfig.mac = ""
        ipa = ip1.get() #a = string 1 = entry
        ipb = ip2.get()
        ipc = ip3.get()
        ipd = ip4.get()

        maca = mac1.get()
        macb = mac2.get()
        macc = mac3.get()
        macd = mac4.get()
        mace = mac5.get()
        macf = mac6.get()
        colon = ":"
        dot = "."
        ip = ipa + dot + ipb + dot + ipc + dot + ipd # concatating all of the octects
        mac = maca + colon + macb + colon + macc + colon + macd + colon + mace + colon + macf
        arpConfig.ip = ip
        arpConfig.mac = mac
        Config.ARP[1] = 1
     
    if l == "ARP":
        arpb = Button(layer3_Frame, text = "✓", command=arpdone,)
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
    layer4_Frame.grid(row = (4), column = 3, sticky = E)
    udp_Ip = Entry(layer4_Frame)
    tcp_Ip = Entry(layer4_Frame)

    if l == layersArray[3][0]:
        udp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)  

    if l == layersArray[3][1]:
        tcp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

def layer5_Displayer(l):
    layer5_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration")
    layer5_Frame.grid(row = (5), column = 3, sticky = E)

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
    layer6_Frame.grid(row = (6), column = 3, sticky = E)

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
    layer7_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration")
    layer7_Frame.grid(row = (7), column = 3, sticky = E)

    soap_Ip = Entry(layer7_Frame)
    dhcp_Ip = Entry(layer7_Frame)
    telnet_Ip = Entry(layer7_Frame)
    irc_Ip = Entry(layer7_Frame)
    ftp_Ip = Entry(layer7_Frame)
    http_Ip = Entry(layer7_Frame)
    https_Ip = Entry(layer7_Frame)
    dns_Ip = Entry(layer7_Frame)

    if l == layersArray[6][0]:
        soap_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[6][1]:
        dhcp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)
    
    if l == layersArray[6][2]:
        telnet_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[6][3]:
        irc_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[6][4]:
        ftp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[6][5]:
        http_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[6][6]:
        https_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[6][7]:
        dns_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

# Sets the History and the Size Configuration
def History_Displayer():
    icmpSpinbox = Spinbox(TrafficConfigFrame, from_=0, to= TrafficSize.size,width=4)

    #Loads the specific Sizes. (Has to be within this function otherwise TrafficSize won't load)
    def TrafficSize_Loader():
        if Config.ICMP[1] == 1:
            icmpConfig.size = icmpSpinbox.get()
           

    TrafficSizeButton = Button(TrafficConfigFrame, text = "✓", command=TrafficSize_Loader)
    TrafficSizeButton.place(x=127,y=140)

    #Displays ICMP configuration
    if Config.ICMP[1] == 1:
        icmpHistory = LabelFrame(cConfigLabel, text="", width=262,height=30, borderwidth=1, relief=SOLID)
        icmpHistory.place(x=0, y=0)

        icmpHistoryLabel = Label(icmpHistory, text = "ICMP", font=("Arial", 16), borderwidth=1,  relief="solid",)
        icmpHistoryLabel.place(x=0, y=0)

        icmpHistoryButton = Button(icmpHistory, text = "INFO", width=3, height=0)
        icmpHistoryButton.place(x=227, y=1)

    
        icmpSpinbox.place(x=40, y=3) #Code needs to be added to make this modular in the future (atm the location is static, I can change this around with some class stuff tho)

        icmpSpinboxLabel = Label(TrafficConfigFrame, text="ICMP:")
        icmpSpinboxLabel.place(x=0, y=3)
        

#Function on the "create Pcap button", checks for errors, then calls the main writing function (PcapWrite())
def createPcap():
    ErrorReset()   # clears all previous error checks from previous creations
    #Checker functions (This will be ran on pretty much every protocol, (Don't know how to make this more effective))
    # As tkinter doesn't like values being returned we have to use a place holder class to hold errors. This gets reset after each compare. (This allows for multiple protocols to use the error checking functions)
    print(icmpConfig.ip)
    print(icmpConfig.mac)
    print(arpConfig.ip)
    print(arpConfig.mac)


    if Config.ICMP[1] == 1:
        IP_checker(icmpConfig.ip) #calls the ip parse function
        icmpConfig.iperror[0] = IPErrors.error[0]
        icmpConfig.iperror[1] = IPErrors.error[1]
        MAC_checker(icmpConfig.mac) #calls the mac parse function
        icmpConfig.macerror[0] = MACErrors.error[0]
        icmpConfig.macerror[1] = MACErrors.error[1]
        icmpConfig.macerror[2] = MACErrors.error[2]
        icmpConfig.macerror[3] = MACErrors.error[3]
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
    if (int(icmpConfig.macerror[0]) > 0 or int(icmpConfig.macerror[1]) > 0 or  int(icmpConfig.macerror[2]) > 0 or int(icmpConfig.macerror[3]) > 0 or int(icmpConfig.iperror[0]) > 0 or int(icmpConfig.iperror[1]) > 0):
        Config.ICMP[0] = 1 #This sets the error 
    #Place holder error follow the same syntax
    
    if (int(arpConfig.macerror[0]) > 0 or int(arpConfig.macerror[1]) > 0 or  int(arpConfig.macerror[2]) > 0 or int(arpConfig.macerror[3]) > 0 or int(arpConfig.iperror[0]) > 0 or int(arpConfig.iperror[1]) > 0):
        Config.ARP[0] = 1 #This sets the error 


    if Config.ICMP[0] != 0:
        IcmpErrorLabel = Label(error_Popup, text="ICMP ERROR: There was an error in your ICMP Configuration.")
        IcmpErrorLabel.pack()

    if Config.ARP[0] != 0:
        arpErrorLabel = Label(error_Popup, text="ARP ERROR: There was an error in your ARP Configuration.")
        arpErrorLabel.pack()


    else:
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
