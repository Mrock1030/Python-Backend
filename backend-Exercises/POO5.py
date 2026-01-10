###Nueva clase polimorfismo###

class Arma:
    
    def __init__(self,balas,pesos):
        self.balas = balas
        self.pesos = pesos
        
    def disparar(self):
        print("El arma dispara")
        
class Pistola(Arma):
    
    def disparar(self):
       #return super().disparar()
       print("El arma dispara lento")
    
       
class Amestralladora (Arma):
    
    def disparar(self):
        print("El arma dispara rapido")
        
        
        
amestralladora = Amestralladora(50,10)
       
    