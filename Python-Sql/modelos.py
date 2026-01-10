

###creamos una pelicula###

class Pelicula:

    def __init__(self,nombre,duracion,genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

class Genero:
    def __init__(self, nombre):
        self.nombre=nombre


class Catalago:
    def __init__(self,nombre):
        self.nombre= nombre
        self.peliculas =[]
