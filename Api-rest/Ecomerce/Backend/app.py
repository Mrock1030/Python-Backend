#importamos de main la función create_app
from main import create_app,db
import os

# Importamos los modelos para que SQLAlchemy los reconozca antes de inicializar la DB
from main.models import ProductoModel, UsuarioModel, ProductoCompraModel, CompraModel

#llamamos nuevamnete a la aplicación app
app = create_app()

##llamamos app .context
"""para acceder a la aplicación en cualquier 
del sistema"""
app.app_context().push()

#para saber si al app se esta ejecutando
##el debug tru hace que se actulice a cada rato
if __name__=='__main__':
    db.create_all()
    app.run(port=os.getenv("PORT"),debug=True)
