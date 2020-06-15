cursos = ["pyrhon", "django", "flask", "c", "c++", "c#", "java", "php"]

curso = cursos[1]
print(curso)
#desde indice hasta indice 
sub = cursos[0:3]
print(sub)
sub = cursos[:7]
print(sub)
sub = cursos[2:5]
print(sub)
sub = cursos[:]
print(sub)
#desde hasta con saltos de 2
sub = cursos[1:7:2]
print(sub)
# inversa desde hasta con saltos de 2
sub = cursos[::-1]
print(sub)

