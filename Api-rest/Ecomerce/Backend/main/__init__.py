#importamos la librerira os
import os 
from flask import Flask
from dotenv import load_dotenv


## para levantar nuetra aplicación

def create_app():
    app = Flask(__name__)
    ##llamamos a las variables de entorno
    load_dotenv()
    return app