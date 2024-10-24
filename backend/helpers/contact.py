from model.model import *
from config.db import *
from flask import request,jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity # type: ignore
import bcrypt
from mailer.clientmail import * 
from mailer.contactmailer import * 


def Contacts():
    response = {}
    try :
       
        name = request.json.get("name")
        email = request.json.get("email")
        whatsapp =request.json.get("whatsapp")
        message = request.json.get("message")

        new_contact= Contact()
        new_contact.name=name
        new_contact.email=email
        new_contact.whatsapp=whatsapp
        new_contact.message=message

        response["statut"]="success"
        response["info"]="envois de message reuissit"

        if response["statut"]=="success":
            send_mail1(name,email)
            send_mail2(name,email,message)
            return response
    except Exception as e :
        response["statut"]="error"
        response["errordescrip"]= str(e)
    return response