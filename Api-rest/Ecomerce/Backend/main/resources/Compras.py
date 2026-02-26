mfrom flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.models import CompraModel
from main.help.Helper import Helper as HelperResource

class Compra(Resource):
    
    def get(self, id):
        compra=db.session.query(CompraModel).get_or_404(id)
        try:
            return compra.to_json()
        
        except:
            return '',404
        
    def put (self,id):
        compra = db.session.query(CompraModel).get_or_404(id)
        data = request.get_json(force=True).items()
        for i , value in data:
            setattr(compra,i,value)
        try:
            db.session.add(compra)
            db.session.commit()
            return compra.to_json(),201
        except:
            return 'No se pudo actualizar ', 404
        
    def delete(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        try:
            db.session.delete (compra)
            db.session.commit()
            return '', 204
        except:
            return 'No se pudo eliminar', 404
            
class Compras(Resource):
    
    def get(self):
        page=1
        per_page=5
        compras = db.session.query(CompraModel)
        if request.get_json(silent=True):
            filters = request.get_json().items()
            for key, value in filters:
                if key =='page':
                    page=int(value)
                if key =='per_page':
                    per_page = int(value)
        compras =compras.paginate(page,per_page,True,10)
        return jsonify({
            'compras':[compra.to_json() for compra in compras.items],
            'total':compras.total,
            'pages':compras.pages,
            'page':page})
    
    def post(self):
        compra = CompraModel.from_json(request.get_json(force=True))
        try:
            HelperResource.validar_int(compra.usuarioId)        
        except ValueError as e:
            return e.args[0], e.args[1]
        
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(),201    