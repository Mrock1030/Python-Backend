from main import db


class ProductoCompra(db.Model):
    
    productoId=db.Column(db.Integer, db.ForeignKey('producto.id'),primary_key=True, nullable=False)
    producto= db.relationship('Producto',back_populates="productoscompras", uselist=False, single_parent=True)
    compraId= db.Column(db.Integer,db.ForeignKey("compra.id"),nullable=False)
    compra = db.relationship('Compra',back_populates="productoscompras", uselist=False, single_parent=True)
    
    def __repr__(self):
        return f"Producto-Compras:{self.producto.to_json()}"
    
    def to_json(self):
        productocompra_json={
            "id":self.id,
            "Producto":self.producto.to_json(),
            "Compra":self.compra.to_json()
        }
        return productocompra_json
    
    @staticmethod
    def from_json(productocompra_json):
        id = productocompra_json.get ("id"),
        productoId = productocompra_json.get("productoId")
        compraId = productocompra_json.get("compraId")
        
        return ProductoCompra (
            productoId=productoId,
            compraId=compraId)
        