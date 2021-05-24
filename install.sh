#!/bin/sh
#install depedencies
#add anything to chron it needs to
#overclock to 2ghz
#change hostname

sudo python3 /home/pi/OMNI/setup/oc.py
sudo python3 /home/pi/OMNI/setup/hostname.py
sudo python3 /home/pi/OMNI/setup/omniToPath.py


read -p 'Press any key to reboot to apply changes'
sudo reboot
