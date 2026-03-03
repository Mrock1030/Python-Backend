from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db 
from main.help.Helper import Helper as HelperResource
from main.models import ProductoModel


class Producto(Resource):
    def get (self,id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        try:
            return producto.to_json()
        except:
            return 'Resource not found',404   
    
    def put (self,id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        data = request.get_json(force=True).items()
        for i, value in data:
            setattr(producto,i,value)
            
        try:
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(),201
        except:
            return '',404
        
    def delete(self, id):
        producto=db.session.query(ProductoModel).get_or_404(id)
        try:
            db.session.delete(producto)
            db.session.commit()
        except:
            return '',404
            

class Productos(Resource):
    
    def get(self):
        page =1
        per_page = 2
        productos = db.session.query(ProductoModel)
        if request.get_json(silent=True):
            filters = request.get_json().items()
            for i , value in filters:
                if i =='page':
                    page = int(value)
                elif i == 'per_page':
                    per_page = int(value)
        productos =productos.paginate(page,per_page,True,3)             
        return jsonify({
            'productos':[producto.to_json() for producto in productos.items],
            'total':productos.total,
            'pages':productos.pages,
            'page':page })
    
    def post(self):
        producto = ProductoModel.from_json(request.get_json(force=True))
        try:
            HelperResource.validar_sting(producto.nombre)
            HelperResource.validar_sting(producto.descripcion)
            HelperResource.validar_int(producto.precio)
            HelperResource.validar_int(producto.stock)
            if db.session.query(ProductoModel).filter(ProductoModel.nombre == producto.nombre).scalar():
                raise ValueError('Product already registered', 409)
        except ValueError as e:
            return e.args[0], e.args[1]
            
           
        db.session.add(producto)
        db.session.commit()
        return producto.to_json(),201