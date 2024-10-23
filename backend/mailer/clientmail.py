from flask_mail import Mail, Message # type: ignore
from dotenv import load_dotenv # type: ignore
import os
from flask import current_app

def send_mail(nom, email):
    msg = Message(f"bonjour {nom}", 
                sender= os.getenv("MAIL_USERNAME"),
                  recipients=[email])
    msg.body = f"votre demande a ete enregistrer notre service de communication vous conctacteras via whatsapp"
    
    with current_app.app_context():
        current_app.extensions['mail'].send(msg)
