# Import smtplib for the actual sending function
import smtplib
import os
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    import auth
except ModuleNotFoundError:
    print("No auth module, no email pw")
# TODO: create email handler, .env file, import keys/pw from there

msg = MIMEMultipart('alternative')

me = 'basic@dreiwerk-solutions.de'
you = 'info@dreiwerk-solutions.de'
msg['Subject'] = "Testing email sending via python"
msg['From'] = me
msg['To'] = you

text = """
This is a test email
"""

html = """
<html>
  <body>
    <h1> This is test email </h1>
  </body>
</html>
"""

p1 = MIMEText(text, "plain")
p2 = MIMEText(html, "html")

msg.attach(p1)
msg.attach(p2)

mailserver = smtplib.SMTP('smtp.strato.de', 587)

mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()

mailserver.login(me, os.getenv("INFO_PASSWORD"))

mailserver.sendmail(me, [you], msg.as_string())

mailserver.quit()