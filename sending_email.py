import smtplib
from config import test_email_receiver, test_email_sender, test_gmail_password, app_password

sender = test_email_sender
password = app_password
receivers = test_email_receiver
subject = 'Python Test Email'
body = 'This is a test email sent from Python'

message = f"""
From: Snoop Dogg{sender}
To: {receivers}
Subject: {subject}/n
{body}
"""


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login Success")
server.sendmail(sender, receivers, message)
print("Email has been sent to", receivers)
server.quit()
