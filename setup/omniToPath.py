import os
path = open('/usr/local/bin/omni' , 'w')
path.write('#!/bin/sh \n')
path.write('/usr/bin/python3 /home/pi/OMNI/main.py $@')
path.close()
os.system('sudo chmod +x /usr/local/bin/omni')
