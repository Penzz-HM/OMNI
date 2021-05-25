import os

TRACE = ['8.8.8.8 192.168.74.2']
# TRACE = os.environ['TRACE']
traceDir = os.listdir('/home/pi/OMNI/trace')
if 'tmp' not in traceDir:
    os.system('mkdir /home/pi/OMNI/trace/tmp')
tracerouteOut = open('/home/pi/OMNI/trace/tmp/tracerouteOut.txt', 'w')
tracerouteOut.close()
for addressPair in TRACE:
    destIP, testIP = addressPair.split(' ')
    os.system('traceroute {} >> /home/pi/OMNI/trace/tmp/tracerouteOut.txt'.format(destIP))