# 发送邮件

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def send_mail(receivers, msg):
    # receivers = list(receivers)
    # 第三方 SMTP 服务
    mail_host="smtp.163.com"  #设置服务器
    mail_user="yangdianxp@163.com"    #用户名
    mail_pass="mfkdwjtj123"   #口令 

    sender = mail_user
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] =  receivers

    send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    subject = '发送通知' + send_time
    message['Subject'] = subject

    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, [receivers], message.as_string())

