from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    from_email = "13191099631@163.com"
    from_password = 'MURCDIOKRHQATKQA'
    to_email = email

    subject = "Height data"
    message = '您好，您的身高是<strong>%s</strong>cm, 共有<strong>%s</strong>人提交，提交的人的平均身高是<strong>%s</strong>cm。' % (height,count,average_height)

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    # 由于gmail邮箱由于网络问题发不出去 改成用国内的邮箱发送
    mail163 = smtplib.SMTP_SSL('smtp.163.com',994) # 实例化smtp 可以用SSL连接 也可以不用
    # gmail.ehlo()
    # gmail.starttls()
    mail163.login(from_email,from_password)
    mail163.sendmail(from_email,to_email,msg.as_string())
    mail163.close()
