from flask_sqlalchemy import SQLAlchemy  # type: ignore
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import db
import uuid

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)  # Clé primaire
    admin_id = db.Column(db.String(128), unique=True, default=lambda: str(uuid.uuid4()))  # Identifiant unique
    firstname = db.Column(db.String(80), nullable=False)  # Prénom
    email = db.Column(db.String(128), nullable=False)  # Email
    password = db.Column(db.String(128), nullable=False)  # Mot de passe
    image_filename = db.Column(db.String(200), nullable=True)  # Nom du fichier image

   
class Contact(db.Model):
    __tablename__ = 'contact'

    # Clé primaire pour la table 'contact'
    id = db.Column(db.Integer, primary_key=True)  # Clé primaire
    article_id = db.Column(db.String(128), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))  # Identifiant unique de l'article
    name = db.Column(db.String(80), nullable=False)  # Nom de l'article
    email = db.Column(db.String(128), nullable=False)  # Email
    whatsapp = db.Column(db.String(120), nullable=False)  # Prix de l'article
    message = db.Column(db.String(120), nullable=False)  # Prix de l'article


class Projet(db.Model):
    __tablename__ = 'projet'
    id = db.Column(db.Integer, primary_key=True)  # Clé primaire
    projet_id = db.Column(db.String(128), unique=True, default=lambda: str(uuid.uuid4()))  # Identifiant unique
    name = db.Column(db.String(80), nullable=False)  # Prénom
    description = db.Column(db.String(120), nullable=False)  # Nom de famille
    lien = db.Column(db.String(120), nullable=False)  # Nom de famille
    image_filename = db.Column(db.String(200), nullable=True)  # Nom du fichier image
