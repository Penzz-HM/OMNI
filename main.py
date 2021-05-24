#take calls from an added environmental variable
#chron once every 15 min to run a status check of the routes. run a heartbeat first before doing any of the status items.

import sys, os, datetime
from heartbeat.omniPing import omniPing

configFile = open('config.conf' , 'r')
configLines = configFile.readlines()
configFile.close()
#args = sys.argv[1]
up = 'false'
traceList = '' #a list of args to run tracerts to, formatted 'dest hop' per line

if len(sys.argv)==1:
    print('Use main.py -h for list of commands')
    args = 'null'

else:
    args = sys.argv[1]

########################################################
#if '-h' in args:
    #write help doc

if '-status' in args:
    up = omniPing('8.8.8.8')
    if up:
        for trace in traceList:
            os.system('python /home/pi/OMNI/trace/omniTrace.py ' + trace[0] + ' ' + trace[1])


elif '-trace' in args:
    os.system('python /home/pi/OMNI/trace/omniTrace.py ' + sys.argv[2] + ' ' + sys.argv[3])


elif '-addTrace' in args:
    #add IP to monitor trace to, format 'OMNI -addTrace dest hop'
    configFile = open('config.conf' , 'w')
    for line in configLines:
        if 'TRACE=' in line.strip():
            if len(sys.argv) == 4:
                configFile.write(line.strip() + sys.argv[2] + ' ' + sys.argv[3] + ',')
        else:
            configFile.write(line)
    configFile.close()
