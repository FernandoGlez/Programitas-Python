#print("¿Cual es tu nombre?\n")
nombre = input("¿Cual es tu nombre?\n")

#print("¿Cual es tu edad?\n")
edad = int(input("¿Cual es tu edad?\n"))

#print("¿Cual es tu peso\n"))
peso = float(input("¿Cual es tu peso\n"))

#print("¿Estas autorizado (si/no)\n")
#autorizado = input() == "si"
autorizado = input("¿Estas autorizado (si/no)\n") == "si"

print("Hola", nombre)
print("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)