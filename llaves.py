diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 , 'f': 6, 'g': 7 , 'h': 8}

#Algunos metodos que nos van a ayudar cuando trabajemos con diccionarios en python
resultado = diccionario.keys()
print(resultado)
#resultado = diccionario.values()

#Visualizamos como tupla con la llave diccionario
#resultado = tuple(resultado)
resultado = list(resultado)
print(resultado)

resultado = diccionario.items()
print(resultado)