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
        page =1
        per_page=5
        usuarios= db.session.query(UsuarioModel)
        if request.get_json(silent=True):
            filters = request.get_json().items()
            for key, value in filters:
                if key =='page':
                    page=int(value)
                elif key =='per_page':
                    per_page==int(value)
        usuarios=usuarios.paginate(page,per_page,True,10)
            
        return jsonify({
            'total':usuarios.total,
            'pages':usuarios.pages,
            'usuario':[usuario.to_json() for compra in usuarios.items],
            'page':page
        })
        
        