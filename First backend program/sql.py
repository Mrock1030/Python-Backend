## importamos la  libreria
import sqlite3
## importamos los datos de variables de entorno. 
from constantes import *

## creamos la funcion para conectarnos

def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
# retornamos la variable para que podamos  hacer llamado en otra función.
    return conexion, cursor

def desconectar_db():
    conexion, cursor = conectar_db()
    guardar_data = conexion.commit
    desconexion = conexion.close()
    return guardar_data, desconexion

def agregar_peliculas(pelicula):
    ##llamamos los conectores de la pelicula
    conexion, cursor = conectar_db()
    pelicula = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero )
    sql= f"INSERT INTO pelicula (nombre,duracion,genero)VALUES {pelicula};"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()


def obtener_peliculas():
    conexion, cursor = conectar_db()
    sql = "SELECT * FROM PELICULA"
    cursor.execute(sql)
    pelicula = cursor.fetchall()
    guardar_data , desconexion = desconectar_db()
    guardar_data
    return  pelicula





#para crear la base de datos
#conectar_db() 

