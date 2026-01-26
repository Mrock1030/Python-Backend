from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.models import CompraModel

class Compra(Resource):
    pass

class Compras(Resource):
    
    def get(self):
        compras = db.session.query(CompraModel).all()
        return jsonify({
            'compras':[compra.to_json() for compra in compras]
        })
    
    def post(self):
        compra = CompraModel.from_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(),201    