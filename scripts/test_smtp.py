import smtplib
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

today = datetime.today()
# 发送邮件服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户名和密码
user = 'test_admin_001@163.com'
password = 'TONIWEDMWCZBNDJB'
# 发送邮箱
sender = 'test_admin_001@163.com'
# 接受邮箱
receiver = ['512839753@qq.com']

# 创建一个带附件的实例
message = MIMEMultipart()
subject = str(today) + ': ' + 'HiFiNi - 音乐磁场自动化签到结果'
message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
message.attach(MIMEText("一般来说如果发出了这条邮件基本上都是签到成功的,唯一出现问题的就是GitHub网络连接不稳定", 'plain', 'utf-8'))

file = open(R'C:\iamge\压轴.docx', 'rb').read()
file1 = open(R'C:\iamge\image.png', 'rb').read()
# 构造附件1，传送当前目录下的test.txt文件
att1 = MIMEText(file, 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
attIamge = MIMEImage(file1)
att1.add_header('Content-Disposition', 'attachment', filename='压轴.docx')
attIamge.add_header('Content-Disposition', 'attachment', filename='签到结果.png')
message.attach(att1)
message.attach(attIamge)

smtp = smtplib.SMTP()
smtp.connect(smtpserver, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, message.as_string())
smtp.quit()
