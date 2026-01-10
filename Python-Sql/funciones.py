from modelos import *
import sql

def agregar_peliculas():
    nombre = str(input("Ingrese el nombre de la pelicula que desea agregar"))
    duracion = int(input("Ingrese la duración de la pelicula"))
    genero = int(input("Ingrese el genero de la pelicula")) 

    pelicula = Pelicula(nombre,duracion,genero)
    sql.agregar_peliculas(pelicula)


catalago = Catalago("Peliculas de Ciencia Fitcion")

def obtener_peliculas():
    peliculas = sql.obtener_peliculas()
    ## hacemois la busqueda
    for pelicula in peliculas:
        guardar_pelicula = Pelicula(pelicula[1], pelicula[2],pelicula[3])
        catalago.peliculas.append(guardar_pelicula)
    
    for pelicula in catalago.peliculas:
        print(f"""\
            Nombre de la pelicula:{pelicula.nombre}
            Duración de la pelicula:{pelicula.duracion} Horas
            Genero de la poelicula:{pelicula.genero}
            """)

        
