from .. import mailsender
from flask import current_app, render_template, Blueprint
from  flask_mail import Message
from  smtplib import SMTPException
from main.models import UsuarioModel, ProductoModel
from main import db
from main.auth.decorators import role_required




def send_email(to, subject, template, **kwargs):
    
    # Esto soluciona el error "please run connect() first" sin tocar __init__.py
    if isinstance(current_app.config['MAIL_PORT'], str):
        current_app.config['MAIL_PORT'] = int(current_app.config['MAIL_PORT'])
    if isinstance(current_app.config['MAIL_USE_TLS'], str):
        current_app.config['MAIL_USE_TLS'] = current_app.config['MAIL_USE_TLS'].lower() == 'true'

    # Asegurar que 'to' sea una lista, si llega como texto
    if isinstance(to, str):
        to = [to]

    msg = Message(subject, sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=to)
    
    try:
        msg.body = render_template(f'{template}.txt', **kwargs)
        mailsender.send(msg)
        
        
    except SMTPException as error:
        return 'Mail deliver failed'
    
    return 'Mail deliver success', True

mail = Blueprint('mail', __name__, url_prefix='/mail')

@mail.route('/newsletter', methods=['POST'])
@role_required(roles=['admin'])

def newsletter():
    usuarios= db.session.query(UsuarioModel).filter(UsuarioModel.rol=='cliente').all()
    productos=db.session.query(ProductoModel).all()
    
    try:
        for usuario in usuarios:
            send_email([usuario.email],"Producto en venta", "newsletter",usuario=usuario, productos=[producto.nombre for producto in productos])
    
    except SMTPException as error:
        return 'Mail deliver failed'
    
    return 'Mail sent',200
             




