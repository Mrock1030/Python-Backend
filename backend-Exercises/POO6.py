###Nuevo Tema Encapsulamiento##

class Curso:
    __titulo ="Backend Python"
    __duracion = 20
    ##los __ hacen que los metodos o atributos queden
    ##privados
    def __adquirir_curso(self):
        print("has adquirido este curso")
    #se crea la función para adquir el curso
    
    def get_adquirir_curso(self):
        return self.__adquirir_curso()
    
     #se crea la función para adquir el titulo
    
    def get_titulo(self):
        return self.__titulo
    
    ##creamos esta función para modificar
    def set_titulo(self,titulo):
        self.__titulo= titulo
        
##asi no se pueden adquir los atributos porque
## estan privados        
curso = Curso()
#curso.titulo
##
curso.get_adquirir_curso()
print(curso.get_titulo())
##
curso.set_titulo("Ya no aguanto mas")
print(curso.get_titulo())
