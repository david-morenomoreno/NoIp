# NoIp
Send your public IP to a register email when it change.


# Ubuntu
$ sudo apt-get install git -y

# Install NoIp
$ cd /usr/local/bin/
$ sudo git clone https://github.com/threatstream/mhn.git
$ cd mhn/
$ pip install -r requirements.txt

# Init when Ubuntu start
Make de file:

$sudo nano /etc/init.d/NoIp

Put the following lines:

#! /bin/sh
python3 nohup /usr/local/bin/NoIp

Save de file and restart
$sudo reboot now
