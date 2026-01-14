from .. import db
import datetime as dt


class Compra(db.Modelk):
    
    id = db.Column(db.Integer,primary_key=True),
    fecha_compra = db.Column(db.DateTime, default=dt.datetime.now(),nullable=False),
    usuarioId = db.Column(db.Integer,db.ForeignKey('usuario.id'),nullable=False)
    usuario = db.relationship('Usuario',back_populates="compras",uselist=False, single_parent =True)
    
    def __repr___(self):
        return f'{self.id},{self.fecha_compra},{self.usuarioId}'

    ##añadimos esto para convertirlo en json 
    ##para convertit un objeto en json
    def to_json(self):
            #creamos el diccionario donde vamos a mostrar las variables
            compra_json ={
                "id":self.id,
                "Fecha_Compra":str(self.fecha_compra),
                "Usuario":self.usuario.to_json(),
            }
            return compra_json
        
    @staticmethod   
    def from_json(compra_json):
        id = compra_json.get("id"),
        fecha_compra= compra_json.get("Fecha_Compra"), 
        usuarioId=compra_json.get("usuarioId"),
    
                
        return Compra(
        id=id,
        fecha_compra=fecha_compra,
        usuarioId=usuarioId,)
    
    