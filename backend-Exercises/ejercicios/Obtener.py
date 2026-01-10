import products

##funcion para retornar productos##
def get_all_products():
    return products.products

def get_products(productos):
    

def search_category(valor):
    lista_json = []
    for d in products.products:
        for k,v in products.products[d].items():
            if v == valor:
                lista_json.append(products.products[d])                 
    return lista_json       
            
    
        
    

##ordenar producto por nombre

#print(get_all_products())
#print(get_products(products.products))
print(search_category(130))


