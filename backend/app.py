from flask import Flask
from config.db import *
from dotenv import load_dotenv  # type: ignore
from flask_mail import Mail, Message  # type: ignore
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity 
from flask_restful import Resource, Api 
from flask_migrate import Migrate
from config.constant import *
from flask_cors import CORS
from ressources.admin import *
from ressources.contact import *
from ressources.projet import *
from ressources.certif import *
from flask_socketio import SocketIO, emit # type: ignore


from flask import send_from_directory


import os


load_dotenv()



app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

CORS(app)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),'static','uploads')

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.secret_key = os.urandom(24)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = SQL_DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)
migrate = Migrate(app,db)
api = Api(app)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # Port pour SSL
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")  # Remplacez par votre adresse e-mail
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")  # Mot de passe de l'application
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
tt =os.getenv("MAIL_USERNAME")
tt2 =os.getenv("MAIL_PASSWORD")
print(f"MAIL_USERNAME: {tt}",{tt2}) 
mail = Mail(app)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


api.add_resource(ContactApi, '/api/contact/<string:route>', endpoint='all_contact',  methods=['GET', 'POST', 'DELETE', 'PATCH'])

api.add_resource(AdminApi, '/api/admin/<string:route>', endpoint='all_admin',  methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(AdminApi, '/api/admin/<string:route>/<string:article_id>', endpoint='get_single_admin', methods=['GET'])

api.add_resource(ProjetApi, '/api/projet/<string:route>', endpoint='all_projet',  methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(ProjetApi, '/api/projet/<string:route>/<string:projet_id>', endpoint='get_single_projet', methods=['GET'])

api.add_resource(CertiftApi, '/api/certif/<string:route>', endpoint='all_certif',  methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(CertiftApi, '/api/certif/<string:route>/<string:certif_id>', endpoint='get_single_certif', methods=['GET'])


if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app, host='127.0.0.1', port=5000)

