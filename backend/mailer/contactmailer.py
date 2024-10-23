
from flask_mail import Mail, Message # type: ignore
from dotenv import load_dotenv # type: ignore
import os
from flask import current_app

def send_mail(nom, email,body):
    msg = Message(f"Monsieur {nom}", 
                sender= email,
                  recipients=[ os.getenv("MAIL_USERNAME")])
    msg.body = f"{body}"
    
    with current_app.app_context():
        current_app.extensions['mail'].send(msg)

   