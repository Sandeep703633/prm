import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('bandikatlasandeep6@gmail.com','prqcvfoehurpyxpz')
    msg=EmailMessage()
    msg['From']='bandikatlasandeep6@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()