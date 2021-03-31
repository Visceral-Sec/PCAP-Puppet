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
master.title("PCAP PUPPET")
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

#Pcap Button Frame

pCreate_Frame = Frame(master)
pCreate_Frame.place(x=515, y = 445)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class icmpConfig:
    icmptext = ""
    ip = ""
    mac = ""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Layer 2 is fully commented, all other layer functions use the exact same formatting and configuration. Follow commenting and apply the good old common sense  to the rest
# UPDATE ^ Layer 3 is now the prefered method. Issues with layer 2 were only solved using a new geometry manage (.place()) which allows for more precise placement.
# As layer 2 contains ICMP which is required for the first prototype. Most work has been done on that layer

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
    layer3_Frame = LabelFrame(lconfig_Frame, text = l + " Configuration", width=294, height=90)    # Using .place geomotry manager under the label frame in order to position correctly
    layer3_Frame.grid(row = (3), column = 3,)
    
    # defining entries
    ip1 = Entry(layer3_Frame, width=2) 
    ip2 = Entry(layer3_Frame, width=2)
    ip3 = Entry(layer3_Frame, width=2)
    ip4 = Entry(layer3_Frame, width=2)
    dot1 = Label(layer3_Frame, text = ".")
    dot2 = Label(layer3_Frame, text = ".")
    dot3 = Label(layer3_Frame, text = ".")

    mac1 = Entry(layer3_Frame, width=3)
    mac2 = Entry(layer3_Frame, width=3)
    mac3 = Entry(layer3_Frame, width=3) 
    mac4 = Entry(layer3_Frame, width=3)
    mac5 = Entry(layer3_Frame, width=3)
    mac6 = Entry(layer3_Frame, width=3)


    colon1 = Label(layer3_Frame, text = ":")
    colon2 = Label(layer3_Frame, text = ":")
    colon3 = Label(layer3_Frame, text = ":")    
    colon4 = Label(layer3_Frame, text = ":")
    colon5 = Label(layer3_Frame, text = ":")   

    iptext = Label(layer3_Frame, text = "IP:")
    mactext = Label(layer3_Frame, text = "MAC:")

    iptext.place(x=2,y=4) #Ip text postioning
    mactext.place(x=2,y=34) #mac text postioning

    ip1.place(x=20,y=5)     #ip entry boxes
    ip2.place(x=50,y=5)
    ip3.place(x=80,y=5)
    ip4.place(x=110,y=5)

    dot1.place(x=40,y=5)
    dot2.place(x=70,y=5)
    dot3.place(x=100,y=5)

    mac1.place(x=40,y=35)   # mac entry boxes
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
    

    def done():
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

        ip = ipa + ipb + ipc + ipd # concatating all of the octects
        mac = maca + macb + macc + macd + mace + macf
        icmpConfig.ip = ip
        icmpConfig.mac = mac
        print(mac)
        print(ip)

    b = Button(layer3_Frame, text = "completed", command=done, )

    b.place(x=220, y=30) # postioning on the button
    
    if l == layersArray[2][0]: #nat
        nat_ip = Entry(layer3_Frame)
        
    if l == layersArray[2][1]: #icmp
        icmp_ip = Entry(layer3_Frame)
        #icmpwindow = Toplevel(master)
        #icmpwindowbutton = Button(icmpwindow, text="Finished", command=icmptextcomplete())
        #finishedbox = Label(icmpwindow, text="Text Saved. You can now close this interface")
    
        
        #def icmptext():
            #icmptxtwindow = Text(icmpwindow)
            #icmptxtwindow.insert(INSERT, "Input ICMP Text Here")
            #icmptxtwindow.pack()
            #icmpwindow.title("ICMP Text input")
            #icmpwindow.geometry("400x400")

    
           # icmpwindowbutton = Button(icmpwindow, text="Finished", command=icmptextcomplete())
          #  icmpwindowbutton.place()
         #   icmpwindowbutton.pack()
        #def icmptextcomplete():
         #   print(icmptxtwindow.get(1.0,END)) # 1.0 is needed cus this library is beyond awful this holds the inputted values 
        #    finishedbox.pack()
      #  icmpbutton = Button(layer3_Frame, text = "ICMP TEXT", command=icmptext)   
       # icmpbutton.place(x=220, y=0)

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

def createPcap():
    print(icmpConfig.ip)
    print(icmpConfig.mac)

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


# setting the buttons

pcapCbutton = Button(pCreate_Frame, text = "Create Pcap", command=createPcap, height=8, width=36)
pcapCbutton.grid
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

pcapCbutton.grid(row = (0), column = 0, sticky = W)




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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    PCAP_PUPPET PYTHON       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~













master.mainloop()