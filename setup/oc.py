import os.path
bootTest = open('/boot/config.txt.test', 'w')
bootFile = open('/boot/config.txt', 'r')
bootLines = bootFile.readlines()
bootFile.close()

for line in bootLines:
    if line.strip() == '#arm_freq=800':
        print 'true'
        bootTest.write('over_voltage=6 \n' + 'arm_freq=2000 \n')
    else:
        bootTest.write(line)


bootTest.close()
bootTest = open('/boot/config.txt.test' , 'r')
bootTestLines = bootTest.readlines()
for line in bootTestLines:
    print line


bootTest.close()
