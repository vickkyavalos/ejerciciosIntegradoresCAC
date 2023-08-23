def palabrasRepetidas(cadena):
    palabras = cadena.split()
    repetidas = {}

    for palabra in palabras:
        if palabra in repetidas:
            repetidas[palabra] +- 1
        else:
            repetidas[palabra] = 1
    
    return repetidas

#ejemplo
print(palabrasRepetidas("buenas tardes, buenas tardes como estan"))