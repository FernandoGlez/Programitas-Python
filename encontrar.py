diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}

resultado = "z" in diccionario
print(resultado)

#Diferentes formas para obtener elementos de nuestros diccionarios
resultado = diccionario.get("z", "la llave no exista")
resultado = diccionario.get("z", True)

resultado = diccionario.setdefault("z", {})
print(resultado)
print(diccionario)