import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail():
    email_sender = 'email@gmail.com'
    email_receiver = 'email@gmail.com'
    subject = 'Today\'s Hijacking'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    body = ''
    with open('person.csv', 'r', newline='\n') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            body = body + row[0] + '\n'

    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(email_sender, 'password')
    connection.sendmail(email_sender, email_receiver, text)
    connection.quit()

