def mensaje():
    print("Funcion simple sin parametros\n")


mensaje()


def edadpersona(edad):
    print("Tu edad es: ", edad)


edad1 = int(input("Escribe tu edad: "))

edadpersona(edad1)


def cuadrado(numero):
    print("El cuadrado del numero es: ", numero * numero)


cuadrado(9)


def rango(num1, num2):
    for i in range(num1, num2, 2):
        print("El Valor de i es: {}".format(i))


inferior = int(input("Ingresa el Rango Inferior: "))
superior = int(input("Ingresa el Rango Superior: "))

print("El rango de numero que elegiste fue: {} y {}".format(inferior, superior))

rango(inferior, superior)
