lenguajes = "Python; Java; Ruby; Php; Swift; Js; C#; C; C++";

separador = "; "

resultado = lenguajes.split(separador) #Resultado es una lista

#nuevo_string = "curso".join(resultado)
nuevo_string = separador.join(resultado)
print(resultado)
print(nuevo_string)

texto = """Este es un texto
con 
saltos
de 

linea """

resultado = texto.splitlines()
print(resultado)