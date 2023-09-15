print("Hola, Bienvenido a tu Examne")

nombre = input("¿Cual es tu nombre? ")
acierto=0

print("Tu nombre es: ", nombre)

pregunta1 = input("¿Estas seguro de realizar el Examen? (Si/No) ")

if pregunta1.lower() != "si":
    quit();

print("Perfecto, Preparate!")

pregunta2 = input("¿Como se llaman los animales que nacen de un huevo? ")
if pregunta2.lower() == "oviparos":
    print("Correcto")
    acierto+=1
else:
    print("Incorrecto")

pregunta3 = input("¿Cual es el unico mamifero que vuela? ")
if pregunta3.lower() == "murcielago":
    print("Correcto")
    acierto += 1
else:
    print("Incorrecto")

pregunta4 = input("¿Cual es el rio mas grande del mundo? ")
if pregunta4.lower() == "amazonas":
    print("Correcto")
    acierto += 1
else:
    print("Incorrecto")

print("Tu numero de Acierto fue: ", acierto)
