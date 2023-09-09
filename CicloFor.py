print("Introduce el rango del ciclo:")
inferior = int(input("Limite Inferior: "))
superior = int(input("Limite Superior: "))

for i in range(inferior, superior, 2):
    print("El Valor de i es: {}".format(i))
