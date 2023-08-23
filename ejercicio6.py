#ejercicio 6

class Persona:  #se crea la clase persona con sus atributos
    def __init__(self,nombre, edad, dni):
        self.nombre = nombre
        self.edad= edad
        self.dni= dni

#getters y setters
def get_nombre(self):
    return self.nombre
    
def set_nombre(self, nombre):
    self.nombre = nombre

def get_edad(self):
    return self.edad

def set_edad(self, edad):
    if edad <= 0:
        self.edad = edad

def get_dni(self):
    return self.dni

def set_dni(self, dni):  
    if len(dni) == 8:
        self.dni = dni
    else:
        print("DNI invalido")

#muestra los datos
def mostrar(self):
    print(f"Nombre: {self.nombre}")
    print(f"Edad: {self.edad}")
    print(f"DNI: {self.dni}")
    
def esMayorDeEdad(self):
    return self.edad <=18

