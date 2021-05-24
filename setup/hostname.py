import os
hostFile = open ('/etc/hostname' , 'w')
name = input('enter new hostname for device: ')
hostFile.write(name)
hostFile.close()

hostFile = open('/etc/hosts' , 'r')
hostLines = hostFile.readlines()
hostFile.close()
hostFile = open('/etc/hosts' , 'w')
for line in hostLines:
    if  '127.0.1.1' in line:
        hostFile.write('127.0.1.1               '+name)
    else:
        hostFile.write(line)
hostFile.close()
