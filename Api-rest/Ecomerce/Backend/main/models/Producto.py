from .. import db
import datetime as dt


class Producto(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     nombre= db.Column(db.String(100),nullable=False)
     precio = db.Column(db.Integer,nullable=False)
     imagen = db.Column(db.String(200),nullable=False)
     descripcion = db.Column(db.String(200),nullable=False)
     productoscompras=db.relationship("ProductoCompra",back_populates="producto",cascade="all,delete-orphan")
     stock = db.Column(db.Integer,nullable=False)
     
def __repr___(self):
    return f'{self.nombre},{self.precio},{self.descripcio},{self.stock}'


##añadimos esto para convertirlo en json 
 ##para convertit un objeto en json
def to_json(self):
        #creamos el diccionario donde vamos a mostrar las variables
        producto_json ={
            "id":self.id,
            "Nombre":self.nombre,
            "Precio":self.precio,
            "Imagen":self.imagen,
            "Descripcion":self.descripcion,
            "Stock":self.stock,
        }
        return producto_json
    
@staticmethod   
def from_json(producto_json):
    id = producto_json.get("id"),
    nombre= producto_json.get("Nombre"), 
    precio=producto_json.get("Precio"),
    imagen=producto_json.get("Imagen"),
    descripcion=producto_json.get("Descripcion"),
    stock= producto_json.get("Stock")
            
    return Producto (
    id=id,
    nombre=nombre,
    precio=precio,
    imagen=imagen,
    descripcion=descripcion,
    stock=stock  )
    