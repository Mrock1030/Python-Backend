from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db
from main.models import UsuarioModel

class Usuario(Resource):
    def get (self,id):
        Usuario=db.session.query(UsuarioModel).get_or_404(id)
        if cliente.rol=='cliente':
            return cliente.to_json()
        else:
            return '',404
        
  

class Usuarios(Resource):
    
     def get(self):
        usuarios= db.session.query(UsuarioModel).all()
        return jsonify({
            'usuario':[usuario.to_json() for compra in usuarios]
        })