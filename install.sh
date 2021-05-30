#!/bin/sh
#install depedencies
#add anything to chron it needs to
#overclock to 2ghz
#change hostname

echo "applying overclock"
sudo python3 /home/pi/OMNI/setup/oc.py
sudo python3 /home/pi/OMNI/setup/hostname.py
echo "updating hostname"
echo "adding OMNI to system path"
sudo python3 /home/pi/OMNI/setup/omniToPath.py
echo "adding reboot email to cron"
sudo crontab -l | { cat; echo "@reboot sleep 15 && sudo python3 /home/pi/OMNI/smtp/rebootEmail.py &"; } | sudo crontab -


read -p 'Press any key to reboot to apply changes'
sudo reboot
