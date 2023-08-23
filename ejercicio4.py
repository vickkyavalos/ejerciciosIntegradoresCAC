def palabrasRepetidas(words):
    palabras = words.split()
    repetidas = {}

    for palabra in palabras:
        if palabra in repetidas:
            repetidas[palabra] +- 1
        else:
            repetidas[palabra] = 1
    
    return repetidas

#def palabraMasRepetida()