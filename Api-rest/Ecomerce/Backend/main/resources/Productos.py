from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.models import ProductoModel

class Producto(Resource):
    def get (self,id):
        producto = db.session.query(ProductoModedl).get_or_404(id)
        try:
            return producto.to_json()
        except:
            return 'Resource not found',404   
    
    def put (self,id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        for key, value in data:
            setattr(producto,key,value)
        try:
            db.session.add(producto)
            db.sesion.commit()
            return producto.to_json(),201
        except:
            return '',404
        
    def delete(self, id):
        producto=db.sesion.query(ProductoModel).get_or_404(id)
        try:
            db.sesion.delete(producto)
            db.session.commit()
        except:
            return '',404
            

class Productos(Resource):
    
    def get(self):
        productos = db.session.query(ProductoModel).all()
        return jsonify({
            'productos':[producto.to_json() for producto in productos]
        })
    
    def post(self):
        producto = ProductoModel.from_json(request.get_json())
        db.session.add(producto)
        db.session.commit()
        return producto.to_json(),201