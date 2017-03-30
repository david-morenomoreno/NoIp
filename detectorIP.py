import re, smtplib, time, random, parametersConfig, ipgetter
from json import load
from urllib.request import urlopen


"""
def GetIpPublica(opcion):
    try:
        if opcion == 0:
            msg = urlopen('http://cual-es-mi-ip-publica.com/').read()
            ip_publica = re.compile('[0-9]+(?:\.[0-9]+){3}').findall(str(msg))
            return ip_publica[0]
        elif opcion == 1:
            ip_publica = urlopen('http://ip.42.pl/raw').read()
            return ip_publica
        elif opcion == 2:
            ip_publica = load(urlopen('http://jsonip.com'))['ip']
            return ip_publica
        elif opcion == 3:
            ip_publica = urlopen("http://whatismyip.com/automation/n09230945.asp").read()
            return ip_publica
        elif opcion == 4:
            ip_publica = load(urlopen('http://httpbin.org/ip'))['origin']
            return ip_publica

        elif opcion == 5:
            ip_publica = load(urlopen('https://api.ipify.org/?format=json'))['ip']
            return ip_publica
        elif opcion == 6:
            ip_publica = ipgetter.myip()
            print(ip_publica)
            return ip_publica

    except Exception as e:
        print(e)
"""

def SendEmail(ip):
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(parametersConfig.gmail_user, parametersConfig.gmail_pwd)
        header = 'To:' + parametersConfig.to + '\n' + 'From: ' + parametersConfig.gmail_user + '\n' + 'Subject:Ip privada \n'
        msg = header + '\n Ip privada: '+str(ip)
        smtpserver.sendmail(parametersConfig.gmail_user, parametersConfig.to, msg)
        print('Enviado')
        smtpserver.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':

    ip_aux = 0

    while True:
        if ipgetter.myip() != ip_aux:
            SendEmail(ipgetter.myip())
            ip_aux = ipgetter.myip()
        time.sleep(random.randint(0, 60))
