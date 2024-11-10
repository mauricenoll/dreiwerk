from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart('alternative')

message['Subject'] = "Deine Anfrage bei DreiWerk Solutions"


def get_contact_mail_template(name):
    html = f"""
        <!DOCTYPE html>
        <html lang="de">
        <head>
            <meta charset="UTF-8">
            <title>Deine Anfrage bei DreiWerk Solutions</title>
        </head>
        <body style="background-color: rgb(240, 248, 255); padding: 0; margin: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <div style="width: 100%; height: 25vh; background-color: rgb(0, 204, 153); display: flex;justify-content: center;align-items: center;">
            <div style="color: rgb(240,240,240); font-size: 5em; min-font-size: 35px; font-weight: bold;text-align: center;">Hi!</div>
        </div>
        <div style="min-width: 350px; width: 100%; background-color: rgb(240,240,240); box-shadow: 0 0 .25vw .15vw rgba(80, 80, 80, .65);border-radius: .3vw;padding: 2vh 2vw;translate: 0 -6vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div style="color: rgb(45, 45, 45); font-size: 2em; width: 100%; text-align: center; min-font-size: 25px; font-weight: bolder;">Hallo {name},</div>
            <div style="color: rgb(45, 45, 45); width: 100%; margin-top: 2vh; min-font-size: 16px;font-size: 1.25em; text-align: center;">
                Wir haben Ihre Anfrage erhalten und melden uns so bald wie möglich bei Ihnen.
                <br><br>
                In der Regel antworten wir innerhalb der nächsten 24 Stunden.
            </div>
            
        </div>
            <div style="margin-top: 5vh;color: rgb(45, 45, 45); width: 100%; font-size: 1.25em; text-align: left;">
                Wir freuen uns darauf, Ihre Fragen zu beantworten und Ihnen weiterzuhelfen.
            </div>
            <div style="color: rgb(45, 45, 45); width: 60%; font-size: 1.25em; text-align: left; margin: 2.5vh 0 .5vh 0;">
                Mit freundlichen Grüßen
            </div>
            <div style="color: rgb(45, 45, 45); width: 60%; font-size: 1.25em; text-align: left; font-weight: bolder;">
                Ihr DreiWerk Team
            </div>
            <img style="width: 50%; min-width: 320px" alt="DreiWerk Logo" src="https://dreiwerk-solutions.de/assets/images/dreiwerk_short.svg">
    
        </body>
        </html>
"""
    plain_text = f"""
    Hallo {name},\n
    Wir haben Ihre Anfrage erhalten und melden uns so bald wie möglich bei Ihnen.\n
    In der Regel antworten wir innerhalb der nächsten 24 Stunden.\n
    Wir freuen uns darauf, Ihre Fragen zu beantworten und Ihnen weiterzuhelfen.\n\n
    Mit freundlichen Grüßen\n
    Ihr DreiWerk Team
    """
    message.attach(MIMEText(html, "html"))
    message.attach(MIMEText(plain_text, "plain"))
    return message
