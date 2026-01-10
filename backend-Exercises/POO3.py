class Catalogo:
    def __init__ (self,nombre):
        self.nombre = nombre
        self.peliculas = []
        
        
class Pelicula:
    def __init__(self,nombre,duracion,genero):
         self.nombre = nombre
         self.duracion = duracion
         self. genero = genero
         
    def __repr__(self):
        return f"{self.nombre},{self.duracion},{self.genero}"
    
    
catalago1= Catalogo("Catalago de terror")
pelicula = Pelicula ("Actividad paranormal",120,"Terror")
print(catalago1.peliculas)
catalago1.peliculas.append(pelicula)
print(catalago1.peliculas)
         
        
     