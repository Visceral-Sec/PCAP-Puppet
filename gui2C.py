from ctypes import *

#This program requires the puppet-backend.so folder
#Change the value of so_file accordingly
#This program only runs functions with included variables
#I see no point intialising the functions that don't output from python
#Everytime the puppet_backend.c function is edited, it will need to be recompiled
#cc -fPIC -shared -o puppet-backend.so puppet-backend.c


#so_file = "/home/csc/SEProject/puppet-backend.so"
puppet_backend = CDLL(so_file)

#Insert variables from GUI below

#insertVariable vars
arrIn =
bytesToWrite =

#condenseChar vars
currentParam = 
paramSize =

#dataParse vars
sMac =
dMac =
target =
source =
data =

insertVar_val = puppet_backend.insertVariable(arrIn, bytesToWrite)
condenseChar_val = puppet_backend.condenseChar(currentParam, paramSize)
dataParse_val = puppet_backend.dataParse(sMac, dMac, target, source, data)
