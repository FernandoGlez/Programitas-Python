mensaje = "Este mensaje de texto puede ser un poco grande"

#Busca la palabra texto y mos dice cuantas veces lo encontro
resultado = mensaje.count("texto")
print(resultado)
#Cuenta el total de letras e 
resultado = mensaje.count("e")
print(resultado)
#Cuenta el total de letras z , en este caso no existe en el parrafo de textos 
resultado = mensaje.count("z")
print(resultado)

#Nos regresa un Verdadero o false si existe la frase en el mensaje.
resultado = "texto" in mensaje
print(resultado)

#Negamos que existe dicha palabra
#resultado = "texto" not in mensaje
#print(resultado)

#Hace referencia en enteros a el #de parrafo  contando la primer letra  T de texto
resultado = mensaje.find("texto")
print(resultado)

#Posicion inicio :resultado , posicion final len ("texto")
resultado = mensaje[resultado: resultado + len("texto")]
print(resultado)

#nos regresa -1 si una palabra o frase  no fue encontrada
resultado = mensaje.find("codigo")
print(resultado)

#True o False si la palabra se encuentra igual escrita y al principio del mensaje
resultado = mensaje.startswith("Este")
print(resultado)