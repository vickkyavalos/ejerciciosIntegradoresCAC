#Escribir una función que calcule el mínimo común múltiplo entre dos números
num1= 48
num2= 18


def mcm(x, y): 
    def mcd(x, y):  #primero calculamos el mcd
        while y:
            x, y = y, x % y
        return x
    return (x * y) // mcd(x, y) #formula

resultado= mcm(num1, num2)
print(f"El mínimo común múltiplo de {num1} y {num2} es { resultado}")