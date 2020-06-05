nombre = input("Cual es tu nombre?\n")

edad = int(input("Cual es tu edad?\n"))

peso = float(input("Cual es tu peso?\n"))

autorizado = input("Estas Autorizado?(Si/no)\n") == "si"

print("Hola", nombre)
print("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)