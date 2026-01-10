
import funciones
while True:
    try:
            menu = int(input("""
                [1] Para agregar una nueva pelicula
                [2] Para obtener peliculas
                [0] Para salir del del programa 
                >>>: """))

            if menu ==1:
                funciones.agregar_peliculas()
            elif menu ==2:
                funciones.obtener_peliculas()
            elif menu ==0:
                print("Saliendo del programa...")
                break
            elif menu >=3:
                print("Ha ingresado una opcion invalida")


    except ValueError as error:
            print(    
            F"""             ingrese una opción invalida, 
            !POR FAVOR  ALIDE EL NUMERO
            Y VUELVA INTENTARLO,{error}""")



