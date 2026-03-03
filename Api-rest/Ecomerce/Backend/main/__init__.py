#importamos la librerira os
import os 
from flask import Flask
import sqlite3
##importamos el dotenv para tomar las variables de entorno
from dotenv import load_dotenv
##importamos el modulo para crear la api-rest
from flask_restful import  Api
##Importamos el modulo para conectarme euna base de datos sql
from flask_sqlalchemy import SQLAlchemy
#importamos el json webtokenn
from flask_jwt_extended import JWTManager
#importo el modulo para  trabajar con email.
from flask_mail import Mail




##definimos lo importado
api = Api()
#instanciamos lo anteriormente importado SQLAlchemy
db=SQLAlchemy()
jwt = JWTManager()
#instanciamos mail sender
mailsender= Mail()



## para levantar nuetra aplicación
def create_app():
    app = Flask(__name__)
    ##llamamos a las variables de entorno
    #cargamos las variables de entorno
    load_dotenv()
    #configuración de la base de datos.db
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    #comprobamos si existe la base de datos
    if not os.path.exists(os.path.join(PATH,DB_NAME)):
        os.makedirs(PATH, exist_ok=True)
        connect_db =sqlite3.connect(os.path.join(PATH,DB_NAME))
        
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{os.path.join(PATH,DB_NAME)}"
    db.init_app(app)
    
    #definimos la ruta
    import main.resources as resources
    ##agregamos la url que va tener para ser obtenido
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource,'/cliente/<int:id>')
    api.add_resource(resources.UsuariosResource,'/usuarios')
    api.add_resource(resources.UsuarioResource,'/usuario/<int:id>')
    api.add_resource(resources.ProductoResource,'/producto/<id>')
    api.add_resource(resources.ProductosResource,'/productos')
    api.add_resource(resources.ComprasResource,'/compras')
    api.add_resource(resources.CompraResource,'/compra/<id>')
    api.add_resource(resources.ProductosComprasResource,'/productos/compras')
    api.add_resource(resources.ProductoCompraResource,'/producto/compra/<id>')
    
    api.init_app(app)
    
    #congigurar jwt
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'fallback_secret_key')
    app.config['JWT_ACCESS_TOKEN_EXPIRE'] = os.getenv('JWT_ACCESS_TOKEN_EXPIRE')
    
    #instanciamos la jwt para  que que acorde a la función
    jwt.init_app (app)
    from main.auth import routes
    # Importamos los decoradores para que se registren los callbacks de JWT (identity_loader, etc.)
    from main.auth import decorators
    app.register_blueprint(routes.auth)
    from main.mail import functions
    app.register_blueprint(functions.mail)
    
    #configurar mail
    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') 
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
    
    mailsender.init_app(app)
    

    return app