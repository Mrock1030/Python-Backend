
class Usuario:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido= apellido
        self.edad = edad
        self.sexo= sexo
        self.premiun= False
    ## similar a str sirve para imprimir las variables por pantalla.    
    def __repr__(self):
        return f"{self.nombre},{self.apellido},{self.edad},{self.sexo},{self.premiun}"
    
    def convertir_premium(self):
        self.premiun = True
    def mirar_peliculas(self):
        if self.premiun:
            print("El usuario puede ver las peliculas ")
        else:
            print("El usuario no es premium")
            
            
    ##metodos estaticos 
    #no ncesitas llamar mediante el objeto
    @staticmethod
    def usuario_mayor(edad):
        return edad >= 18        
        
usuario = Usuario("Gaston","Fenske",21,True)
print(usuario)
print(usuario.premiun)
usuario.mirar_peliculas()
usuario.convertir_premium()
print(usuario)
print(Usuario.usuario_mayor(20))
          
        