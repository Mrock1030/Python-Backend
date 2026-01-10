lista = [1,2,3,4,5]

if 5 in lista:
    print("Ese numero esta en la lista")
    
menu = int(input("ingrese una opción valida:"))

try:
    print(f"Ha ingresado la opción {menu}")
except ValueError as error:
    print (f"No puede ingresar ese tipo de data {error}")
    
