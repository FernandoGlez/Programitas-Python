curso = "Python"
version = "3"

#resultado = "Curso de %s %s" %(curso,version)
#sustituimos los valores de las variables dentro de los parentesis.

#resultado = "Curso de {} {}".format(curso, version)
resultado = "Curso de {a} {b}".format(b=version, a=curso)

print(resultado)