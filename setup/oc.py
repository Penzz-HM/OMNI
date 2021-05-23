import os.path

bootFile = open('/boot/config.txt', 'r')
bootLines = bootFile.readlines()
bootFile.close()
bootFile = open('/boot/config.txt' , 'w')
for line in bootLines:
    if line.strip() == '#arm_freq=800':
        print 'Applying Overclock to 2ghz'
        bootFile.write('over_voltage=6 \n' + 'arm_freq=2000 \n')
    else:
        bootFile.write(line)
bootFile.close()
