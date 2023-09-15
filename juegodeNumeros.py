import random

intentos = 0
numMaximo = input("¿Cual es el numero maximo que puede ser generado? ")

if numMaximo.isdigit():
    numMaximo = int(numMaximo)
    if numMaximo <= 0:
        print("Intenta con otro numero")
        quit()
else:
    print("Solamente puedes introducir numeros")
    quit()

numerogenerado = random.randint(1,numMaximo)

"""print(numerogenerado)"""
print("Intenta adivinar el numero generado: ")

while True:
    intentos+=1
    posibleNumero = input("Numero: ")
    if posibleNumero.isdigit():
        posibleNumero = int(posibleNumero)
    else:
        print("Solo puedes introducir Numeros")
        continue
    if posibleNumero == numerogenerado:
        print("Felicidades, Acertaste")
        break
    else:
        print("Intentalo de Nuevo")
        if posibleNumero > numerogenerado:
            print("Intenta con un numero menor al ",posibleNumero)
        else:
            print("Intenta con un numero mayor al ", posibleNumero)


print("Realizaste", intentos, "intentos para adivinar")

