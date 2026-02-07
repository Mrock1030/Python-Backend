
class Helper():
    
    @staticmethod
    def validar_sting(value_string):
        #asi quedan mejor instanciadas 
        if not isinstance(value_string, str):
            raise ValueError('El valor para este campo nombre  debe ser una cadena de texto.', 409)
        return value_string
    
    @staticmethod
    def validar_int(value_int):
        if not isinstance(value_int, int):
            raise ValueError('El valor para este campo debe ser un número entero.', 409)
        return value_int

    @staticmethod
    def how_many_number(value):
        if len(str(value)) > 10:
            raise ValueError('No ha ingresado digitos de mas', 409)
        elif len(str(value)) < 10:
            raise ValueError('No ha ingresado digitos suficientes', 409)
        return value
