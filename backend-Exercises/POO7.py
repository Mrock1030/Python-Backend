## Encapsulamiento 2.0

class Persona:
    
    def __init__(self,name:str, age:int, mail:str) ->None:
        self.__name=name
        self.__age = age
        self.__mail = mail

    @property
    def name(slef)->str:
        return self.__name

    @name.setter
    def name(self,name:str)->None:
        self.__name = name
        
    @name.deleter
    def name(self)->None:
        del self.__name

    def main () ->None:
        person = Person(name = "Gaston",age=22, mail ="jkmilo1030@gmail.com")
        print(person.name)
        person.name = "Gastonceto"
        print(person.name)
        del person.name
        print(person.name)
        
if __name__== "__main__":
    main()
        
        
    