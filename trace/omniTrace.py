def omniTrace():
    import os, re

    # TRACE = ['8.8.8.8 192.168.74.2']
    TRACE = os.environ['TRACE']
    traceDir = os.listdir('/home/pi/OMNI/trace')
    result = dict()
    if 'tmp' not in traceDir:
        os.system('mkdir /home/pi/OMNI/trace/tmp')
    tracerouteOut = open('/home/pi/OMNI/trace/tmp/tracerouteOut.txt', 'w')
    tracerouteOut.close()
    for ind, addressPair in enumerate(TRACE):
        destIP, testIP = str(addressPair).split(' ')
        addressPair = addressPair.replace(' ', '_')
        os.system('traceroute {} >> /home/pi/OMNI/trace/tmp/tracerouteOut_{}.txt'.format(addressPair, ind))


        with open('/home/pi/OMNI/trace/tmp/tracerouteOut_{}.txt'.format(addressPair), 'r') as traceData:
            traceLines = traceData.readlines()
        for ind2, tLine in enumerate(traceLines):
            s = re.compile(str(testIP))
            isMatch = bool(s.search(tLine))
            if isMatch:
                print('Found matching IP Address at hop {}'.format(ind2))
                result[addressPair] = {'lineText': tLine,
                                       'hopNum': ind2}
            else:
                result[addressPair] = None

    os.system('rm -rf /home/pi/OMNI/trace/tmp/*')

    # Returns a dictionary with info about the traceroute results.
    # Example: result[8.8.8.8_192.168.74.2]['hopNum'] will return the value of
    # the hop at which the address 192.168.74.2 was matched for traceroute to
    # 8.8.8.8. If no match is found for that route, the value will be null (None)
    if result:
        return result

