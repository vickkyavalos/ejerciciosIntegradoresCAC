#Escribir una función que calcule el máximo común divisor entre dos números

def mcd(x, y):
    while y:
        x, y = y, x % y
        return x

    
num1 = 48
num2 = 18
resultado = mcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es { resultado}")