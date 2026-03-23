
from main.repositorio import CompraRepository

compra_repositorio = CompraRepository()


class CompraService:
    
    def obtener_compra_con_descuento(self,id):
        compra = compra_repositorio.find_one(id)
        #Aca se pdoria agregar el descuento 
        #tipo de logica a la compra para calcular el descuento
        #compra.total = compra.total -(compra.total* descuento)
        return compra
    
    def agregar_compra(self,compra):
        return compra_repositorio.create(compra)
    
    def actualizar_compra(self,compra):
        return compra_repositorio.update(compra)