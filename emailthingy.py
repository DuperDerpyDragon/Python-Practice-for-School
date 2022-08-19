from email.message import EmailMessage
import ssl
import smtplib
import random


def verified():
    v1 = input('Enter your Verification Code: ')
    if v1 == f'{letter}{number}':
        print("Correct Verification Code!")
    else:
        print("Wrong Code!")


name = input("Enter your name: ")
list = ['a', 'b', 'c', 'd']
number = random.randint(0, 100)
letter = random.choice(list)

email_sender = 'antixblox@gmail.com'
email_password = 'cjhuptxusagjeogy'
email_reciever = input("Enter your email: ")


subject = f'Welcome {name}!'
body = f"Your verification Code is {letter}{number}"


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

verified()