class Auto:
    #En el metodo constructor agregamos atributos
    def __init__(self,marca,color,cantidad_ruedas,velocidad_max):
        self.marca = marca
        self.color= color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad_max= velocidad_max
        self.motor =2.0
         
    
    def __str__(self):
        return f"{self.motor},{self.marca},{self.velocidad_max},{self.cantidad_ruedas}"
    def acelerar(self):
        print(f"El auto ha acelarado,{self.velocidad_max}km")
        
 #instanciar la clase es crear un objeto.       
aventador =Auto("Lamborghini","Blanco",4,320)
        
aventador.acelerar()
        
        
    
    