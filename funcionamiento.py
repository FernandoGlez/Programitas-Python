diccionario = {}

diccionario["nombre"] = "Codi" #Para agregar una llave con su valor

valor = diccionario["nombre"]

diccionario["nombre"] = 90
print(diccionario)
print(valor)
"""
el fincionamiento es muy sencillo si la llave existe dentro del diccionario ,entonces se remplaza el valor
si la llave existe entonces dentro del diccionario entonces se crea la llave
y se almacena su valor
"""
diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}
print(diccionario)

"""
Lo primero que devemos hacer es agregar su primera llave y su primer valor """

#imprimimos el valor asignado siempre y cuando existe una llave dentro del diccionario
resultado = diccionario["a"]
print(resultado)

