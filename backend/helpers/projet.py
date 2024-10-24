from model.model import *
from config.db import *
from flask import request,jsonify
from helpers.file import save_image
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity # type: ignore
import bcrypt


def CreatProjet():
    response={}
    try :
        name= request.form.get("name")
        description =request.form.get("description")
        lien =request.form.get("lien")
        image_filename =request.form.get("image_filename")


        new_projet = Projet()
        new_projet.name=name
        new_projet.description=description
        new_projet.lien=lien
        if 'image_filename' in request.files:
            image_file = request.files['image_filename']
            print("mon image depuis",image_file)
           
            if image_file.filename == '':
                response["statut"] = "erreur"
                response["info"] = "Aucun fichier d'image sélectionné"
                return jsonify(response)
            
            # Enregistrer l'image
            image_filename = save_image(image_file)
            new_projet.image_filename = image_filename 

        db.session.add(new_projet)
        db.session.commit()
        projet_info ={
            "name":new_projet.name,
            "description":new_projet.description,
            "lien":new_projet.lien,
            "image_filename":new_projet.image_filename
        }
        response["statut"]="succes"
        response["info"]=projet_info
        return response
    except Exception as e :
        response["statut"]="error"
        response["errorDescript"]=str(e)
    return response

def GetAllProjet():
    response={}
    try :
        data =[]
        all_projet = Projet.query.all()

        for projet in all_projet :
            info_projet ={
                "name":projet.name,
                "description":projet.description,
                "lien":projet.lien,
                "image_filename":projet.image_filename,
            }
            data.append(info_projet)
        response["statut"]="success"
        response["info"]=data
        return response
    except Exception as e :
        response["statut"]="error"
        response["errordescript"]=str(e)
    return response

def SingulProjet(projet_id):
    response={}
    try :

        singul_projet = Projet.query.filter_by(projet_id=projet_id).first()
        if not singul_projet :
            response["statut"]="error"
            response["info"]="projet pas trouver"
            return response
        
        info_projet={
            "name":singul_projet.name,
            "description":singul_projet.description,
            "lien":singul_projet.lien,
            "image_filename":singul_projet.image_filename,
        }
        response["statut"]="success"
        response["info"]=info_projet
        return response
    except Exception as e :
        response["statut"]="error"
        response["descriperror"]=str(e)  
    return response   


def DeleteProjet():
    response={}
    try :
        projet_id = request.json.get("projet_id")
        projet = Projet.query.filter_by(projet_id=projet_id).first()
        if not projet :
            response['statut']="error"
            response["info"]="projet nexiste pas"
            return response
        db.session.delete(projet)
        db.session.commit()
        response["statut"]="success"
        response["info"]="suppression reussit"
        return response
    except Exception as e :
        response["statut"]="error"
        response["errordescript"]=str(e)
    return response


def UpdateProjet():
    response ={}
    try :
        projet_id = request.json.get("projet_id")
        projet_update = Projet.query.filter_by(projet_id=projet_id).first()
        if not projet_update :
            response["statut"]="error"
            response["info"]="projet non existant"
            return response
        
        projet_update.name = request.json.get("name",projet_update.name)
        projet_update.decription = request.json.get("decription",projet_update.decription)
        projet_update.lien = request.json.get("lien",projet_update.lien)

        if 'image_filename' in request.files:
            image_file = request.files['image_filename']
            print("mon image depuis",image_file)
           
            if image_file.filename == '':
                response["statut"] = "erreur"
                response["info"] = "Aucun fichier d'image sélectionné"
                return jsonify(response)
            
            # Enregistrer l'image
            image_filename = save_image(image_file)

        projet_update.image_filename = image_filename or projet_update.image_filename

        info_projet ={
            "name":projet_update.name,
            "description":projet_update.description,
            "lien":projet_update.lien,
            "image_filename":projet_update.image_filename,
        }

        response["statut"]="succes"
        response["info"]=info_projet
        return response
    except Exception as e :
        response["statut"]="error"
        response["errordescrip"]= str(e)
    return response

           
            



    

