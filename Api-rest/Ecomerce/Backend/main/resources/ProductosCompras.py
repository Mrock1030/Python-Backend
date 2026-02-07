from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.models import ProductoCompraModel

class ProductosCompras(Resource):
    def get (self):
        page=1
        per_page=5
        productocompras = db.session.query(ProductoCompraModel)
        if request.get_json(silent=True):
            filters = request.get_json().items()
            for i , value in filters:
                if i =='page':
                    page = int(value)
                elif i == 'per_page':
                    per_page = int(value)
        productoscompras=productocompras.paginate(page,per_page,True,10)             
        return jsonify({
                'total':productoscompras.total,
                'pages':productoscompras.pages,
                'page':page,           
                'productos':[productoscompras.to_json() for productocompras in productoscompras.items]})
                  
    def post(self):
        productocompra = ProductoCompraModel.from_json(request.get_json(force=True))
        db.session.add(productocompra)
        db.session.commit()
        return productocompra.to_json(), 201
    
class ProductoCompra(Resource):
    def get(self,id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        try:
            return  productocompra.to_json()
        except:
            return '' , 404
        
    def delete(self,id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        try:
            db.session.delete(productocompra)
            db.session.commit()
            return '', 204
        except:
            return '', 404
        
    def put(self,id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        data = request.get_json(force=True).items()
        for i, value in data:
            setattr(productocompra, i ,value)
        try:
            db.session.add(productocompra)
            db.session.commit()
            return productocompra.to_json(),201
        except:
            return '',404
        
            