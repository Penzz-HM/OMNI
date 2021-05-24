#take calls from an added environmental variable
#chron once an hours to run a status check of itself? -status flag?

import sys, os, datetime
from heartbeat.omniPing import omniPing

args = sys.argv[1]
up = 'false'

if '-status' in args:
    up = omniPing('8.8.8.8')
    print (up)


elif '-trace' in args:
    os.system('python /home/pi/OMNI/trace/omniTrace.py ' + sys.argv[2] + ' ' + sys.argv[3])

