from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.models import ProductoModel

class Producto(Resource):
    pass

class Productos(Resource):
    pass 