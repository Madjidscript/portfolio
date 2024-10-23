import os
from flask import current_app,url_for
from werkzeug.utils import secure_filename


def save_image(image_file):
    # Générer un nom de fichier sécurisé
    filename = secure_filename(image_file.filename)
    
    # Créer le dossier s'il n'existe pas
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)  # Crée le dossier s'il n'existe pas
    
    # Chemin où l'image sera enregistrée
    image_path = os.path.join(upload_folder, filename)
    
    # Enregistrer l'image
    image_file.save(image_path)
    # Construire l'URL de l'image
    image_url = url_for('static', filename='uploads/' + filename, _external=True)

    return image_url
