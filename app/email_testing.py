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

import mail_handler
from mail_templates import contact_template

handler = mail_handler.EmailHandler(myEmail=os.getenv("INFO_EMAIL"), password=os.getenv("INFO_PASSWORD"), mailHost=os.getenv("MAIL_HOST"), port=int(os.getenv("MAIL_PORT")))

handler.send_mail('maurice-noll@mail.de', contact_template.get_contact_mail_template("Maurice Noll"), {
        "anrede": "Herr",
        "name": "maurice",
        "email": "maurice-noll@mail.de",
        "tel-num": "",
        "msg": "Hallo ich interesiere mich für dinge",
        "data_protection": True
    })





