#take calls from an added environmental variable
#chron once an hours to run a status check of itself? -status flag?

import sys, os, datetime

args = sys.argv[1]

if '-trace' in args:
    os.system('python /home/pi/OMNI/trace/omniTrace.py ' + sys.argv[2] + ' ' + sys.argv[3])

