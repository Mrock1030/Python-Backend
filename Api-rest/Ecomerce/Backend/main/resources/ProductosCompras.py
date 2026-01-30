from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.models import ProductoCompraModel

class ProductoCompra(Resource):
    def get (self):
        productoCompras = db.session.query(ProductoCompraModel).all()
        return jsonify({
            "productoCompra":[productoCompra.to_json() for productoCompra in productoCompras ]
        })
        
    def post(self):
        productocompra = ProductoCompraModel.from_json(request.get_json())
        db.session.add(productocompra)
        db.session.commit()
        return productocompra.to_json(), 201
    
class ProductosCompras(Resource):
    def get(self,id):
        productocompra = db.sesion.query(ProductoCompraModel).get_or_404(id)
        try:
            return  productocompra.to_json()
        except:
            return '' , 404
        
    def delete(self,id).
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        try:
            db.session.delete(productocompra)
            db.session.commit()
            return '', 204
        except:
            return '', 404
        
    def put(self,id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        data = request.get_json().items()
        for i value in data:
            setattr(productocompra, i ,value)
        try:
            db.session.add(productocompra)
            db.session.commit()
            return productocompra.to_json(),201
        except:
            return '',404
        
            