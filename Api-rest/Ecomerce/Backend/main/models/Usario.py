from .. import db
import datetime as dt


class Usuario(db.Model):
    ##creamos las tablas para nuestra base de datos 
    id= db.Column(db.Integer,primary_key=True)
    nombre= db.Column(db.String(45),nullable=False)
    apellido=db.Column(db.String(45),nullable=False)
    email=db.Column(db.String(80),nullable=False,unique=True,index=True)
    rol=db.Column(db.String(45),nullable=False,default="cliente")
    telefono= db.Column(db.Integer,nullable=False)
    fecha_registro = db.Column(db.DateTime,default=dt.datetime.now(), nullable=False)
    compras = db.relationship('Compra',back_populates="usuario", cascade="all,delete-orphan")
    
    ##añadimos esta función para debuguiar
    def __repr___(self):
        return f'{self.nombre},{self.apellido},{self.email},{self.rol}'
    
    ##añadimos esto para convertirlo en json 
    ##para convertit un objeto en json
    def to_json(self):
        #creamos el diccionario donde vamos a mostrar las variables
        usuario_json ={
            "id":self.id,
            "Nombre":self.nombre,
            "Apellido":self.apellido,
            "Email":self.email,
            "Rol":self.rol,
            "Telefono":self.telefono,
            "Fecha":str(self.fecha_registro)
        }
        return usuario_json
    ##ahora de json a  objeto
    
    @staticmethod
    def from_jon(usuario_json):
        id = usuario_json.get("id"),
        nombre= usuario_json.get("Nombre") ,
        email=usuario_json.get("Email"),
        rol=usuario_json.get("Rol"),
        telefono=usuario_json.get("telefono"),
        fecha_registro= usuario_json.get("fecha")
        
        #instanciamos esto como un objeto
        return Usuario(
            nombre= nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            fecha_registro=fecha_registro
            
        )
                
        
    
    
    

        