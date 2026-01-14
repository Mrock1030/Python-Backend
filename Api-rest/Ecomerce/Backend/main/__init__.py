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
##definimos lo importado
api = Api()
#instanciamos lo anteriormente importado SQLAlchemy
db=SQLAlchemy()

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
    api.add_resource(resources.ClientesResource,'/Clientes')
    api.add_resource(resources.ClienteResource,'/Cliente/<id>')
    api.add_resource(resources.UsuariosResource,'/Usuarios')
    api.add_resource(resources.UsuarioResource,'/Usuario/<id>') 
    
    
    api.init_app(app)
    
    return app