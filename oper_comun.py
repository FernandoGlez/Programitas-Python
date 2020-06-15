lista = [8.17, 90, 1 , 5, 44, 1.32]
#Longitud de lista
longitud = len(lista)
print(longitud)

#Busqueda de un numero en la lista
resultado = 8.17 in lista
print(resultado)

#el numero de la lista se encuentra dentro del indice
indice = lista.index(8.17)
print(indice)

#Ordenar la lista de forma ascendente
lista.sort()
print(lista)

#cuenta las veces un elemento en nuestra lista
contador = lista.count(5)
print(contador)


#Ordenar la lista de forma descendente
lista.sort(reverse=True)
print(lista)
#Obtener el numero mayor de una  lista
lista.sort(reverse=True)
mayor = lista[0]
print(mayor)
#Obtener el numero menor de una lista
lista.sort()
menor = lista[0]
print(menor)

menor = min(lista)
print(menor)

mayor = min(lista)
print(mayor)