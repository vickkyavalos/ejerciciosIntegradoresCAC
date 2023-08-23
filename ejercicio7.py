
class Cuenta():
    def __init__(self,titular,cantidad = 0):
        self.__titular = titular
        self.__cantidad = cantidad
        
        
    def get_titular(self):
        return self.__titular
        
    def set_titular(self,titular):
        self.__titular = titular
        
    def get_cantidad(self):
        return self.__cantidad
        
    def set_cantidad(self, cantidad):
        self.__cantidad = titular
        
    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad



#ejemplo 
titular1 = Cuenta("Valeria Diaz", 2000)
titular1.mostrar()

titular1.ingresar(1200)
titular1.retirar(500)
titular1.mostrar()