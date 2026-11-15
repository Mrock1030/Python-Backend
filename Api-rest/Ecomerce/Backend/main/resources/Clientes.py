from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request
from main import db, mailsender
from main.models import UsuarioModel
from main.help.Helper import Helper as HelperResource
from main.auth.decorators import role_required
from flask_jwt_extended import get_jwt
from flask_mail import Message
from flask import jsonify, request, current_app
from sqlalchemy.exc import SQLAlchemyError


        
class Cliente(Resource):
    @role_required(roles=['admin','cliente'])
    def get (self,id):
        # Obtenemos los datos del usuario que hace la petición (del token)
        claims = get_jwt()
        # Buscamos al usuario objetivo en la base de datos por su ID
        cliente = db.session.query(UsuarioModel).filter(UsuarioModel.id == id).first()
        
        # Si no existe el usuario, devolvemos 404
        if cliente is None:
            return 'Cliente no existe', 404
        # Verificamos que el usuario buscado sea efectivamente un 'cliente'
        elif cliente.rol=='cliente' and claims['id'] == cliente.id:
            # Solo permitimos ver los datos si el usuario se busca a sí mismo O si quien busca es admin
           return cliente.to_json()

        elif claims['id']==cliente.id  and  cliente.rol=='admin':
            return cliente.to_json()
        else:
            # Si el usuario existe pero no es 'cliente' ni'admin' devolvemos 404 para ocultarlo
            return 'No tienes permisos para acceder a este recurso',404
   
    CAMPOS_PERMITIDOS = {"nombre", "apellido", "telefono"}

    @role_required(roles=['admin','cliente'])    
    def put (self, id):
        claims = get_jwt()
        es_admin = claims.get("rol") =="admin"
        es_dueno = int(claims.get("id",-1)) ==id

        cliente = db.session.get(UsuarioModel).get_or_404(id)
        if cliente is None
            return {"error:Cliente no encontrado"},404
        
        data = request.get_json(silent=True)
        if not isintance (data,dict):
            return {"error": "Debes enviar un objeto JSON"}, 400
        campos_invalidos = set(data)-CAMPOS_PERMITIDOS
        if campos_invalidos :
            return {
            "error": "Campos no permitidos",
            "campos": sorted(campos_invalidos), }, 422

        for campo, valor, in data.items():
            setattr (cliente,campo,valor):
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Error actualizando cliente")
            return {"error": "No se pudo actualizar el cliente"}, 500

        return cliente.to_json(), 200
    

    @role_required(roles=['admin','cliente'])
    def delete(self,id):
        claims = get_jwt()
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        
        if cliente is None:
            return 'El cliente no existe o ya fue eliminado', 404
        
        elif cliente.rol=='cliente' and claims['id'] == cliente.id:
                try:
                    db.session.delete(cliente)
                    db.session.commit()
                    return 'Se elimino el cliente', 201
                except:
                    return 'No se pudo eliminar el cliente', 404
                
        elif claims['id']==cliente.id  and  cliente.rol=='admin':
                try:
                    db.session.delete(cliente)
                    db.session.commit()
                    return 'Se elimino el cliente', 201
                except:
                    return 'No se pudo eliminar el cliente', 404
        else:
            return '',404
            
class Clientes(Resource):
    @role_required(roles=['admin'])
    def get(self):
        page =1
        per_page=5 
        clientes= db.session.query(UsuarioModel).filter(UsuarioModel.rol=='cliente')
        if request.get_json(silent=True):
            filters=request.get_json().items()
            for i, value in filters:
                if i =='page':
                    page = int(value)
                elif i =='per_page':
                    per_page=int(value)
        clientes=clientes.paginate(page,per_page,True,10)
        
        return jsonify({
            'pages':clientes.pages,
            'page':page,   
            'usuario':[cliente.to_json() for cliente in clientes.items],
            'total':clientes.total
        })
        
    @role_required(roles=['admin'])
    def post(self):
        cliente = UsuarioModel.from_json(request.get_json(force=True))
        try:
            HelperResource.validar_sting(cliente.nombre)
            HelperResource.validar_sting(cliente.apellido)
            HelperResource.validar_int(cliente.telefono)
            HelperResource.how_many_number(cliente.telefono)
            
            if db.session.query(UsuarioModel).filter(UsuarioModel.email == cliente.email).scalar():
                raise ValueError('Email already registered', 409)
            elif db.session.query(UsuarioModel).filter(UsuarioModel.nombre == cliente.nombre, UsuarioModel.apellido == cliente.apellido).scalar() :
                 raise ValueError('User already registered', 409)

        except ValueError as e:
            return e.args[0], e.args[1]
        cliente.rol='cliente'
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(),201