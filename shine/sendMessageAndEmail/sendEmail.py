# 发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText

# SMTP服务器
SMTPServer = 'smtp.qq.com'
# 发邮件的地址
sender = '240272750@qq.com'
# 邮箱密码
password = 'eoywmleeedikbjjj'
# 发送内容
message = 'Shine is a good man'
# 把字符串转为邮件文本
msg = MIMEText(message)
# 标题
msg['Subject'] = '来自帅哥的问候'
# 发送者
msg['From'] = sender
# 创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)
# 登录邮箱
mailServer.login(sender,password)
# 发送邮件
mailServer.sendmail(sender,['13387565008@163.com'],msg.as_string())
# 退出邮箱
mailServer.quit()

