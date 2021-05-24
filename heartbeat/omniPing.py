import os

def omniPing(arg1):
    response = os.system('ping -c 1 ' + arg1)
    if response == 0:
        return 'true'
    else:
        return 'false'


omniPing('8.8.8.8')
