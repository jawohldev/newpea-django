from companydjango import settings
username=settings.DEFAULT_FROM_EMAIL
password=settings.EMAILHOST_PASS
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_mail(html,text='Email_body',subject='Hello word', from_email='',to_emails=[]):
    assert isinstance(to_emails,list)
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=", ".join(to_emails)
    msg['Subject']=subject
    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)
    html_part = MIMETEXT(f"<p>Here is yo nigga </p><h1>{html}</h1>",'html')
    msg.attach(html_part)
    msg_str=msg.as_string()
    server=smtplib.SMTP(host='smtp.zeptomail.com',port=587)
    server.ehlo()
    server.startttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit
