import ipgetter
import parametersConfig
import random
import smtplib
import time


def SendEmail(ip):
    """
    This function send your public Ip to sender email.
    :param ip: 
    """
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo

        smtpserver.login(parametersConfig.gmail_user, parametersConfig.gmail_pwd)
        header = 'To:' + parametersConfig.to + '\n' + 'From: ' + parametersConfig.gmail_user + '\n' + 'Subject:Ip privada \n'
        msg = header + '\n Ip privada: '+str(ip)

        smtpserver.sendmail(parametersConfig.gmail_user, parametersConfig.to, msg)
        smtpserver.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    ip_aux = 0
    
    while True:
        ip_public = ipgetter.myip()
        if ip_public != ip_aux:
            SendEmail(ip_public)
            ip_aux = ip_public

        time.sleep(random.randint(0, 60))
