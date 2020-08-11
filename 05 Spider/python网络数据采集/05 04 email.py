import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def pythonSendEmail():
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "yangzong5@163.com"  # 用户名
    mail_pass = "yangzongwu1987"  # 口令

    sender = "yangzong5@163.com"
    receivers = "yangzong5@163.com"

    message = MIMEText('Python 邮件发送测试...', )
    message['subject'] = 'An Email Alert'
    message['From'] = "yangzong5@163.com"
    message['To'] = "yangzong5@163.com"

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def sendMail(subject,body):
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "yangzong5@163.com"  # 用户名
    mail_pass = "yangzongwu1987"  # 口令

    sender = "yangzong5@163.com"
    receivers = "yangzong5@163.com"

    message = MIMEText(body)
    message['subject'] = subject
    message['From'] = "yangzong5@163.com"
    message['To'] = "yangzong5@163.com"

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

bsObj=BeautifulSoup(urlopen("http://isitchristmas.com/"))
while(bsObj.find('a',{"id":"answer"}).attrs["title"]=="NO"):
    print("It is not Christmas yet")
    time.sleep(3600)
sendMail("It's Christmas","hello, christmas")
