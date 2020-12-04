import smtplib
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Email, Mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings


USERNAME = settings.USERNAME
PASSWORD = settings.PASSWORD
port = 587
host = 'smtp.gmail.com'
from_email = "KU Oracle Club <kosamdjango@gmail.com>"
subject="Thank You For Subscribing To Our Newsletter"
text = "Hello thank you for becoming part of our community. You will receive updates when new events are uploaded to site"
html = """
<!Doctype html>
<html>
<head>
<title>Kenyatta University Oracle Club</title>
</head>
<body>
<p>Hello thank you for becoming part of our community. You will receive updates when new events are uploaded to site</p>
<a href="https://oracleku-club.herokuapp.com" target="_blank">View Site</a>
</body>
</html>
"""



def send_mail(from_email=from_email, subject=subject , text=text, to_emails=None, html=html):
  assert isinstance(to_emails, list)
  did_send = False

  msg = MIMEMultipart('alternative')
  msg['Subject'] = subject
  msg['From'] = from_email
  msg['To'] = ", ".join(to_emails)

  text_part = MIMEText(text, 'plain')
  msg.attach(text_part)

  if html != None:
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

  msg_str = msg.as_string()

  with smtplib.SMTP(host, port) as server:
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)
    try:
      server.sendmail(from_email, to_emails, msg_str)
      did_send = True
    except:
      did_send = False
  return did_send


def send_mail_sg(from_email=from_email, to_emails=None, subject=subject, html=html):
  assert isinstance(to_emails, list)
  did_send = False

  message = Mail(
    from_email=from_email,
    to_emails=", ".join(to_emails),
    subject=subject,
    html_content=html
  )

  try:
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    did_send = True
  except Exception as e:
    print(e)
    did_send = False
  return did_send