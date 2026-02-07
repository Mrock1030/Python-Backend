from flask import request, Blueprint
from main.models import UsuarioModel
from flask_jwt_extended import create_access_token
from main import db


auth = Blueprint('auth',__name__,url_prefix='/auth')

@auth.route('/login',methods=['POST'])
def login():
    usuario = db.session.query(UsuarioModel).filter(UsuarioModel.email==request.get_json().get('email')).first_or_404()
    if usuario.validate_pass(request.get_json().get('password')):
        access_token = create_access_token(identity=usuario)
        
        data = {
            'id':str(usuario.id),
            'email': usuario.email,
            'access_token':access_token,
            'rol':str(usuario.rol)   
        }
        return data, 200
    else:
        return 'Incorrect password',401
    
        
@auth.route('/register',methods=['POST'])
def register():
    usuario = UsuarioModel.from_json(request.get_json())
    exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar()
    if exists:
        return 'Duplicated email', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as error :
            db.session.rollback()
            return  str(error), 409
        return usuario.to_json(),201    
 