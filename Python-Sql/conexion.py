#agregamos el conector de acuerdo a bd

import sqlite3 

#creamos la variable de conexión
conexion = sqlite3.connect("/home/jk/Documentos/Python/bases-sql/basespruebacurso.db")
cursor = conexion.cursor()

#creamos funcion obtener clientes
def obtener_clientes():
    sql = 'SELECT * from clientes;'
    cursor.execute(sql)
    print(cursor)
    clientes=cursor.fetchall()
    print(clientes)


def add_clientes(nombre, apellido, email,fecha_registro,role=None, telefono=None):
    clientes = (
        nombre,
        apellido,
        email,
        fecha_registro,
        telefono,
        role )
    sql = f"INSERT INTO CLIENTES(nombre,apellido,email,fecha_registro,telefono) VALUES{clientes};"
    cursor.execute(sql)


def update_clientes(nombre,id):
    sql = f"UPDATE CLIENTES SET nombre='{nombre}' WHERE id ={id};"
    cursor.execute(sql)

def drop_usuario(id):
    sql= f"DELETE  FROM CLIENTES WHERE id = {id};"
    cursor.execute(sql)




#obtener_clientes()
#add_clientes("Luisa","Anaya","luisanaya@prueba.com","2025-01-03 9:56:00.552583","3014182691")
update_clientes('Monda Parada',13)
#drop_usuario()
obtener_clientes()


conexion.commit()
conexion.close()

