#Uso de asterisco para asignar mas elementos sin variables en la tupla
tupla = (1,2,3,4,5,6)
#uno, dos, tres, *cuatro = tupla
#uno, *dos, cinco, seis = tupla

lista = [10,20,30,40]

tupla_dos = (100, 200, 300, 400)
#comprimir
resultado = zip(tupla,lista)
#Tupla la cual contiene los elementos de la tupla y la lista
resultado = tuple(resultado)

#obtiene los elementos tupla y lista em list
resultado = list(resultado)
print(resultado)

#Obtiene los elementos de 3 tuplas 
resultado = zip(tupla,lista, tupla_dos)
resultado = list(resultado)
print(resultado)
"""
print(uno)
print(dos)
print(tres)
print(cuatro)
print (cinco)
print (seis)
"""