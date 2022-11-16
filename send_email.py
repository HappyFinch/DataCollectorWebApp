from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    from_email = "happyfinch7788@gmail.com"
    from_password = 'pomwpbtqxcbvgvwm'
    to_email = email

    subject = "Height data"
    message = '您好，您的身高是<strong>%s</strong>cm, 共有<strong>%s</strong>人提交，提交的人的平均身高是<strong>%s</strong>cm。' % (height,count,average_height)

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
