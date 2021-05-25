import os, re, subprocess

TRACE = ['8.8.8.8 192.168.74.2']
# TRACE = os.environ['TRACE']
for addressPair in TRACE:
    destIP, testIP = addressPair.split(' ')
    tracerouteOut = subprocess.run('traceroute', destIP, stdout=subprocess.PIPE)
    print(tracerouteOut.stdout)