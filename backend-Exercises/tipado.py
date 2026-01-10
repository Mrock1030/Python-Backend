##ejercicio de tipado

nombre :str = 'juanka'
edad :int = 22
familia : list = [ 'Mama','Papa','Hermanos']
atributos : dict = {'Genero':"masculino", "Altura":180}

programador : bool = True

#Persona :object = Pérsona()
def imprimir_nombre (nombre:str)-> None:
    print(nombre)

def calcular_potencia(num:int) -> int:
    return num**num
def ordenar_numeros() -> list:
    numeros : list(int) = [1,6,7,3,4,9,10,2]
    return sorted [numeros]

def main()->None:
    print(orendar_numeros())
    
if __name__=='__main__':
    main()