#Send an email informing of the intrusion
#Author: Joshua Roberts
import smtplib
import os
import Constants
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(timeStamp):
    "This function sends an email with the current timestamp"
    print("Sending email")

    sender = Constants.SENDER_EMAIL
    receiver = Constants.RECIPIENT_EMAIL

    message = MIMEMultipart()
    
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "INTRUSION"

    message.attach(MIMEText("There was an intrusion at " + str(timeStamp)))

    smtpObject.sendmail(sender, receiver, message.as_string())
    print("Email sent...")
    print("Intrusion recorded and uploaded to internet")
    

print("Connecting to SMTP Server...")
smtpObject = smtplib.SMTP(Constants.SMTP_PORT)
smtpObject.starttls()
smtpObject.login(Constants.SENDER_EMAIL, Constants.SENDER_PASSWORD)
print("Connection made")
