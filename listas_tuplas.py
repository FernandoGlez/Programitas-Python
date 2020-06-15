lista = ["Curso", "Python", "Cf"]
tupla = ["Introduccion", "Basic", "lista", "Tuplas"]

mensaje = "Este es el curso de Python"
#obtenemos una tupla a una nueva lista
nueva_lista = list(mensaje)
nueva_tupla = tuple(mensaje)

"""
nueva_lista = list(tupla)
#obtenemos una lista a una nueva Tupla
nueva_tupla = tuple(lista)
"""
print(nueva_lista)
print(nueva_tupla)