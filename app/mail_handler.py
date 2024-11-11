import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    import auth
except ModuleNotFoundError:
    print("No auth module, no email pw")


class EmailHandler:

    def __init__(self, myEmail: str, password: str, mailHost: str, port: int):
        self.email = myEmail
        self.password = password
        self.host = mailHost
        self.port = port
        self.mailserver = smtplib.SMTP(self.host, self.port)

    def login(self):
        self.mailserver.ehlo()
        self.mailserver.starttls()
        self.mailserver.ehlo()

        self.mailserver.login(self.email, self.password)

    def send_inquiry_to_myself(self, inquiry_form: dict):
        msg = MIMEMultipart('alternative')
        msg['To'] = self.email
        msg['From'] = self.email
        msg['Subject'] = "Anfrage an DreiWerk solutions"

        text = """ """
        for key in inquiry_form:
            text = f"{text}\n{key}: {inquiry_form.get(key)}"

        msg.attach(MIMEText(text, "plain"))
        print(msg)
        self.mailserver.sendmail(self.email, self.email, msg.as_string())

    def send_mail(self, recipient: str, message: MIMEMultipart, form_data: dict):
        self.login()
        message['To'] = recipient
        message['From'] = self.email
        self.mailserver.sendmail(self.email, recipient, message.as_string())
        self.send_inquiry_to_myself(form_data)
        self.mailserver.quit()

