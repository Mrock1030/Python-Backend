###Nuevo Tema###
####Herencias###


class Animal:
    
    def __init__(self,edad,patas,alimentacion,estado):
        self.edad = edad
        self.patas = patas
        self.alimentacion = alimentacion 
        self.estado=estado
        
    def caminar(self):
        print("El animal camina")
    
    def nadar(self):
        print("El animal nada")

#creamos una clase con herencia.
class Perro(Animal):
    raza = None
    ladrido =None
    pelaje =  None 
    
    def ladrar(self):
        print("El perro ladra")
    
    def morder(self):
        print("El perro muerde")
        
class Gato(Animal):
    
    def saltar(self):
        print("El gato salta")
        
        
    def maulla(self):
        print("El gato maulla")
        
        

Zeus = Perro(5,4,"onnivoro","vivo")
Zeus.raza ="Chandoso"
Zeus.ladrido = "Intenso"
Zeus.pelaje = "Negro Aspero" 

#imprimimos atributos
print(Zeus.edad)   
    
    
    
    
        
        