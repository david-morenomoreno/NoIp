# NoIp
Send your public IP to a register email when it change.

Install git on ubuntu:

$ sudo apt-get install git -y

# Install NoIp
$ cd /usr/local/bin/

$ sudo git clone https://github.com/dmoreno1994/NoIp.git

$ cd NoIp/

$ pip install -r requirements.txt

Go to parameterConfig.py and complete the fields. Don't forget delete {}

# Init when Ubuntu start
Make de file:

$sudo nano /etc/init.d/NoIp

Put the following lines:

#! /bin/sh

python3 nohup /usr/local/bin/NoIp

Save de file and restart

$sudo reboot now
