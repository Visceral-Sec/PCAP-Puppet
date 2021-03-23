from tkinter import * #Importing tkinter


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    PCAP_PUPPET GUI    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frames/Master ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#https://www.youtube.com/watch?v=YXPyB4XeYLA
#Tkinter works a bit like HTML, but instead of objects etc we have widgets

master = Tk() #This is the root of the entire gui
master.geometry('779x580') # sets default size
#master.resizable(width=False, height=False) # prevents the size from being adjusted

#Frame for layer configuraiton
lconfig_Frame = Frame(master)
lconfig_Frame.grid(row = (1), column = 0, sticky = W)

#Frame for Titles "Protocols"/"Configuration"/"PCAP Settings"
tConfig_Frame = Frame(master)
tConfig_Frame.grid(row = (0), column = 0, sticky = N)

#Frame for Protocol Configuraiton Settings

pConfig_Frame = Frame(master)
pConfig_Frame.grid(row = (0), column = 1, sticky = W)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Dictionaries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Layer 2 is fully commented, all other layer functions use the exact same formatting and configuration. Follow commenting and apply the good old common sense  to the rest

def layer2_Displayer(l): # The purpose of this functions is that every layer menu option will call one of this funcitons followed with the selection option. In this case that is L.
    layer2_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration") # This then prints the label heading as the name of the chosen protocol + the option
    layer2_Frame.grid(row = (2), column = 3, sticky = E,) # Postioning

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
       
    # current issues:
    # Currently each option doesn't actually remove the previous it jsut over-writes on top of it. It's impossbile for the user to notice but may be an issue in the future. (.forget() doesn't work for some reason I hate tkinter)
    # Currently no testing has got into how this is going to withdraw data so that's an important thing to note
    # Potentially not the best way of approaching this but this but that's why we have prototypes.

    # to do
    # add more options 
    # flesh out a better way of appraoch
    # get data out of these inputs
    # think about how to connect to this to the actual python program


def layer3_Displayer(l):
    layer3_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration")
    layer3_Frame.grid(row = (3), column = 3, sticky = E)

    nat_Ip = Entry(layer3_Frame)
    icmp_Ip = Entry(layer3_Frame, text="IP")
    rip_Ip = Entry(layer3_Frame, text="IP") 
    arp_Ip = Entry(layer3_Frame, text="IP")
    ospf_Ip = Entry(layer3_Frame, text="IP")
    ip_Ip = Entry(layer3_Frame, text="IP")

    if l == layersArray[2][0]:
        nat_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)  

    if l == layersArray[2][1]:
        icmp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[2][2]:
        
        rip_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[2][3]:
        
        arp_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[2][4]:
        ospf_Ip.grid(row = (1), column = 3, sticky = E, pady=25, padx=82)

    if l == layersArray[2][5]:
        ip_Ip.grid(row = (1), column = 3, sticky = E,pady=25, padx=82)

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

   
# agony this was coded nicely with modular programming but unfornutely you can't do anything with the .get function if it's in a localised for statemnent therefore I need to hard code it all
# Adding variables with common protocols at each level

#for i in range(1,7):
 #   layerTitle = StringVar()  # sets the dropbox as a string variable 
  #  layerTitle.set("Layer " + str(i + 1))
   # Layerdrop = OptionMenu(lconfig_Frame, layerTitle, *layersArray[i], command=mynameisjeff() # Sets it as a drop down
    #Layerdrop.config(width=5, padx=68, pady=5, height=4, font=("Arial", 12)) # configures the size of the drop box
    #Layerdrop.grid(row = (i+1), column = 0, sticky = W)

# ^ this code does that entire ugly block in one simple for statement but it's difficult to get it to work with the function commands

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


# end of program so far

master.mainloop()