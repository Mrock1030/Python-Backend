#importamos la librerira os
import os 
from flask import Flask
##importamos el dotenv para tomar las variables de entorno
from dotenv import load_dotenv



##importamos el modulo para crear la api-rest
from flask_restful import  Api
##definimos lo importado
api = Api()

## para levantar nuetra aplicación
def create_app():
    app = Flask(__name__)
    ##llamamos a las variables de entorno
    load_dotenv()
    #definimos la ruta
    import main.resources as resources
    ##agregamos la url que va tener para ser obtenido
    api.add_resource(resources.ClientesResource,'/Clientes')
    api.add_resource(resources.ClienteResource,'/Cliente/<id>')
    api.init_app(app)
    return app