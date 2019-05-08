import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.qq.com'

user='1301073951@qq.com'
password='dkghsefbvnyrjafc'

sender='1301073951@qq.com'
receive='340497963@qq.com'

subject='Web Selenium 自动化测试报告'

content='<html><h1 style="color:red"> Selenium1111111111</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='1301073951qq.com'
msg['To']='340497963@qq.com'

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)
print("Start send Email")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("Send Email end!")