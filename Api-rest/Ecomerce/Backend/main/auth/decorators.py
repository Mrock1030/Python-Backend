from .. import jwt 
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def role_required(roles):
    def decorator(function):
        def wrapper(*args, **kwargs):
            #verificar que el jwt es correcto
            verify_jwt_in_request()
            #obtenemos los calims (peticiones), que estan dentro del JWT
            claims = get_jwt()
            if claims.get('rol') in roles:
                return function(*args, **kwargs)
            else:   
                return 'rol not allowed', 403
        return wrapper
    return decorator

@jwt.user_identity_loader
def user_identity_loader(usuario):
    return {
        'usuario.Id':usuario.id,
        'rol':usuario.rol }

@jwt.additional_claims_loader
def additional_claims_to_access_token(usuario):
    claims ={
        'id':usuario.id,
        'rol':usuario.rol,
        'email':usuario.email
    }
    return claims
    


















    

        
             