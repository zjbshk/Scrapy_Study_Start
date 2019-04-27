# from selenium import webdriver

# from time import sleep
# #1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
# browser = webdriver.Chrome("F:/brower_driver/chromedriver")
# #2.通过浏览器向服务器发送URL请求
# browser.get("https://wenku.baidu.com/view/a2eaa1273069a45177232f60ddccda38376be193.html")
# browser.set_window_size(1400,800)
# div = browser.find_element_by_id("view-like-recom")
# print(div.text)
# sleep(3)
# browser.quit()

from scrapy.mail import MailSender
import smtplib

MAIL_HOST = "smtp.163.com"
MAIL_FORM = "zjb592466695@163.com"
MAIL_USER = "zjb592466695@163.com"
MAIL_PASSWORD = "yjnzjb123"
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = MAIL_HOST
mail_user = MAIL_USER
mail_pass = MAIL_PASSWORD

sender = MAIL_FORM
receivers = ['592466695@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('空指针', 'plain', 'utf-8')
message['From'] = Header(MAIL_FORM, 'utf-8')
message['To'] = Header('592466695@qq.com', 'utf-8')

subject = '数据出现异常'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.set_debuglevel(1)
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(e)