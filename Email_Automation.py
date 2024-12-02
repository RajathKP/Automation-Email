import smtplib
from email.mime import message
from email.mime.text import MIMEText

my_email = "<EMAIL>"
password_key = "<PASSWORD>"

#SMTP Server and part no for Gmail.com

gmail_server="smtp.gmail.com"
gmail_port=587

#Starting Connection

my_server = smtplib.SMTP(gmail_server,gmail_port)
my_server.ehlo()
my_server.starttls()

# login with your email and password

my_server.login(my_email,password_key)

text_content = "Hello, I am a computer science student. I’m interested in Internship at your organization"
message.attach(MIMEText(text))