from model.model import *
from config.db import *
from flask import request,jsonify
from helpers.file import save_image
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity # type: ignore
import bcrypt


def CreatCertif():
    response={}
    try :
        name= request.form.get("name")
        description =request.form.get("description")
        image_filename =request.form.get("image_filename")

        new_certif = Certif()
        new_certif.name=name
        new_certif.description=description
        if 'image_filename' in request.files:
            image_file = request.files['image_filename']
            print("mon image depuis",image_file)
           
            if image_file.filename == '':
                response["statut"] = "erreur"
                response["info"] = "Aucun fichier d'image sélectionné"
                return jsonify(response)
            
            # Enregistrer l'image
            image_filename = save_image(image_file)
            new_certif.image_filename = image_filename 

        db.session.add(new_certif)
        db.session.commit()
        certif_info ={
            "name":new_certif.name,
            "description":new_certif.description,
            "image_filename":new_certif.image_filename
        }
        response["statut"]="succes"
        response["info"]=certif_info
        return response
    except Exception as e :
        response["statut"]="error"
        response["errorDescript"]=str(e)
    return response

def GetAllCertif():
    response={}
    try :
        data =[]
        all_certif = Certif.query.all()

        for certif in all_certif :
            info_certif ={
                "name":certif.name,
                "description":certif.description,
                "image_filename":certif.image_filename,
            }
            data.append(info_certif)
        response["statut"]="success"
        response["info"]=data
       
        return response
    except Exception as e :
        response["statut"]="error"
        response["errordescript"]=str(e)
    return response

def SingulCertif(certif_id):
    response={}
    try :

        singul_certif = Certif.query.filter_by(certif_id=certif_id).first()
        if not singul_certif :
            response["statut"]="error"
            response["info"]="Certif pas trouver"
            return response
        
        info_certif={
            "name":singul_certif.name,
            "description":singul_certif.description,
            "image_filename":singul_certif.image_filename,
        }
        response["statut"]="success"
        response["info"]=info_certif
        return response
    except Exception as e :
        response["statut"]="error"
        response["descriperror"]=str(e)  
    return response   


def DeleteCertif():
    response={}
    try :
        certif_id = request.json.get("certif_id")
        certif = Certif.query.filter_by(certif_id=certif_id).first()
        if not certif :
            response['statut']="error"
            response["info"]="certif nexiste pas"
            return response
        db.session.delete(certif)
        db.session.commit()
        response["statut"]="success"
        response["info"]="suppression reussit"
        return response
    except Exception as e :
        response["statut"]="error"
        response["errordescript"]=str(e)
    return response


def Updatecertif():
    response ={}
    try :
        certif_id = request.json.get("certif_id")
        certif_update = Certif.query.filter_by(certif_id=certif_id).first()
        if not certif_update :
            response["statut"]="error"
            response["info"]="certif non existant"
            return response
        
        certif_update.name = request.json.get("name",certif_update.name)
        certif_update.decription = request.json.get("decription",certif_update.decription)
      

        if 'image_filename' in request.files:
            image_file = request.files['image_filename']
            print("mon image depuis",image_file)
           
            if image_file.filename == '':
                response["statut"] = "erreur"
                response["info"] = "Aucun fichier d'image sélectionné"
                return jsonify(response)
            
            # Enregistrer l'image
            image_filename = save_image(image_file)

        certif_update.image_filename = image_filename or certif_update.image_filename

        info_certif ={
            "name":certif_update.name,
            "description":certif_update.description,
            "image_filename":certif_update.image_filename,
        }

        response["statut"]="succes"
        response["info"]=info_certif
        return response
    except Exception as e :
        response["statut"]="error"
        response["errordescrip"]= str(e)
    return response

           
            



    

