from model.model import *
from config.db import *
from flask import request,jsonify
from helpers.file import save_image
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity # type: ignore
import bcrypt



def CreatAdmin():
    response={}
    admin_id  = request.form.get("admin_id")
    password=request.form.get("password")
   
    email=request.form.get("email")
    print("mon pass",admin_id,password ,email)
    admin = Admin.query.filter_by(email=email).first()

    if admin :
        response["statut"]="error"
        response["info"]="utilisateur existe"
        return response
    
    firstname = request.form.get("firstname")
    
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_admin = Admin()
    new_admin.firstname=firstname
    new_admin.email=email
    new_admin.password=password_hash
    new_admin.admin_id=admin_id


    if 'image_filename' in request.files:
            image_file = request.files['image_filename']
            print("mon image depuis",image_file)
           
            if image_file.filename == '':
                response["statut"] = "erreur"
                response["info"] = "Aucun fichier d'image sélectionné"
                return jsonify(response)
            
            # Enregistrer l'image
            image_filename = save_image(image_file)
            new_admin.image_filename = image_filename 

    db.session.add(new_admin) 
    db.session.commit()      

    data = {}
    data["admin_id"]=new_admin.admin_id
    data["email"]=new_admin.email
    data["password"]=new_admin.password
    data["firstname"]=new_admin.firstname
    response["statut"]="success"
    response["info"]=data

    if response["statut"]=="success" :
         return data
         
    
def GetAllAdmin():
    response={}
    try :
            data = []
            all_admin = Admin.query.all()

            if all_admin :
                 for admin in all_admin:
                      liste_admin={
                           "admin_id":admin.admin_id,
                           "email":admin.email,
                           "firstname":admin.firstname,
                           "image_filename":admin.image_filename,
                      }
                      data.append(liste_admin)
            response["statut"]="succes"
            response["info"]=data   
            return response       

                 
          
    except Exception as e:
        response["statut"]="error"
        response["descriperror"]= str(e)
    return response


def GetSingulAdmin(admin_id):
     response={}
     
     try :
          admin = Admin.query.filter_by(admin_id=admin_id).first()

          if not admin :
               response["statut"]="error"
               response["info"]="admin existe pas"
               return response
          data = {
          "admin_id": admin.admin_id,
          "email": admin.email,
          "firstname": admin.firstname,
          "image_filename": admin.image_filename,
          }

          response["statut"]="succes"
          response["info"]=data
          return response
    
     except Exception as e :
          response["statut"]="error"
          response["erorDescrip"]=str(e)

     return response



def DeleteAdmin():
     response={}
     try :
          admin_id = request.json.get("admin_id")
          admin = Admin.query.filter_by(admin_id=admin_id).first()
          if not admin :
               response["statut"]="error"
               response["info"]="utilisateur n'existe pas"
               return response
          db.session.delete(admin)
          db.session.commit()
          response["statut"]="succes"
          response["info"]="utilisateur supprimer"
          return response
     except Exception as e :
          response["statut"]="error"
          response["errorDescrip"]=str(e)
     return response
               

def UpdateAdmin() :
     response={}
     try :
          admin_id= request.form.get("admin_id")
          admin_update = Admin.query.filter_by(admin_id=admin_id).first()
          if not admin_update :
               response["statut"]="error"
               response["info"]="utilisateur nexiste pas"
               return response
          admin_update.admin_id = request.form.get("admin_id", admin_update.admin_id)
          admin_update.email = request.form.get("email", admin_update.email)
          admin_update.password = request.form.get("password", admin_update.password)
          admin_update.firstname = request.form.get("firstname", admin_update.firstname)
          password = bcrypt.hashpw(request.form.get("password").encode('utf-8'), bcrypt.gensalt())
          admin_update.password = request.form.get(password,admin_update.password)

          if 'image_filename' in request.files:
            image_file = request.files['image_filename']
            print("mon image depuis",image_file)
           
            if image_file.filename == '':
                response["statut"] = "erreur"
                response["info"] = "Aucun fichier d'image sélectionné"
                return jsonify(response)
            
            # Enregistrer l'image
            image_filename = save_image(image_file)
            admin_update.image_filename = request.json.get(image_filename,admin_update.image_filename)

          db.session.commit()
          info_admin = {
               "firstname":admin_update.firstname,
               "email":admin_update.email,
               "password":admin_update.password,
               "image_filename":admin_update.image_filename,
               "admin_id":admin_update.admin_id,
          }
          response["statut"]="success"
          response["info"]= info_admin
          return response
     except Exception as e :
          response["statut"]="error"
          response["errorDecrip"]=str(e)

            
def LoginAdmin() :
     response={}
     try :
          admin_id = request.json.get("admin_id")
          email = request.json.get("email")
          password = request.json.get("password")
          admin = Admin.query.filter_by(email=email).first()
          if not admin :
               response["statut"]="error"
               response["info"]="utilisateur n'existe pas"
               return response
          admin_info={
               "email":admin.email,
               "firstname":admin.firstname,
               "password":admin.password,
               "admin_id":admin.admin_id,
               "image_filename":admin.image_filename,
          }

          if admin and bcrypt.checkpw(password.encode("utf8"),admin.password.encode("utf8")) :
               response["statut"]="succes"
               response["info"]=admin_info
               return response
     except Exception as e :
          response["statut"]="error"
          response["erorrDescription"]=str(e)
          