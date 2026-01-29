from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.models import ProdutoCompraModel

class ProductoCompra(Resource):
    def get (self):
        productoCompras = db.session.query(ProdutoCompraModel).all()
        return jsonify({
            "productoCompra":[productoCompra.to_json() for productoCompra in productoCompras ]
        })

class ProductosCompras(Resource):
        def post(self):
        productocompra= ProdutoCompraModel.from_json(request.get_json())
        db.session.add(productocompra)        db.session.commit()
        return compra.to_json(),201    