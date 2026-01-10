#import modulos
#print(modulos.saludar('Gaston'))
#user = modulos.Usuario('Juan Camilo','jkmilo1030@gmail.com')
#print(user.nombre)


## Para importar una sola clase o función##

from modulos import Usuario

user = Usuario('Pedro','jkmil1030@gmail.com')

## para importar de dos carpetas##

from ..import POO7

persona = POO7.Persona('Juan',27,'jkmilo1030@gmail.com')
