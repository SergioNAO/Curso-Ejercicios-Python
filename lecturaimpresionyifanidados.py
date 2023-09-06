datoA = int(input("Ingresa un numero: "))
datoB = int(input("Ingresa un numero: "))
datoC = int(input("Ingresa un numero: "))

if(datoA> datoB ):
    if(datoA>datoC):
        print("El numero mayor es: ",datoA)
    else:
        print("El numero mayor es: ",datoC)

else:
    if(datoB>datoC):
        print("El numero mayor es ",datoB)
    else:
        print("El numero mayor es: ",datoC)


