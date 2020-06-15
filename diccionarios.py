"""
Los diccionarios en Python al igual que las tuplas o listas,
nos permite almacenar diferentes tipos de datos 
Strings, Enteros, Booleanos, Flotantes, Tuplas ,listas & otros diccionarios..


A diferencia que las tuplas o listas no se rigen por la reglas de los 
indices , si no por una llave,
Una llave puede ser Culaquier tipo de dato en Python.
"""

diccionario = {}
diccionario = dict()

# { llave: el valor el cual queremos asociar.}
diccionario = { "total": 55 }
print(diccionario)

diccionario = { "total": 55, "descuento": True, "subtotal": 15}
print(diccionario)

#Un Json en Python es un diccionario
#Definimos un diccionario de tipo usuario 
usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23,
    'curso': 'Curso de Python',
    'skills' : {
        'programacion' : True,
        'base_de_datos' : False
    },
    'medallas' : ['básico', 'intermedio']
}
print(usuario)

#Creación del diccionario
diccionario = dict()

#Agregar nueva llave valor
diccionario['usuario'] = 'Maria'

#Actualizar valor mediante una llave
diccionario['usuario'] = "Maria.gpg"

#obtener valor mediante una llave
print(diccionario['usuario'])

usuario = {
    'name' : 'Fernando Ismael',
    'age': 26,
    'job' : 'Codigo'
}
