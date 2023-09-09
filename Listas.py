lista = [1,2,3,4]
"""Cambiar un elemento de la Lista"""
print(lista)
lista[0] = 9
print(lista)

"""Listas con diferentes tipos de dato"""
lista2 = ["Hola", "Como", "Estas"]
lista3 = ['Hola', 3, True, 4.3]
print(lista2)
print(lista3)

"""Imprimir cada elemento de la lista"""
for elemento in lista:
    print(elemento)

"""Agregar un elemento a la lista"""
lista.append(5)
print(lista)

"""Cambiar tipos de datos en una lista"""
lista[3] = "Hola"
print(lista)

"""Quitar un elemento de la lista"""
lista.pop(1)
print(lista)
"""Otra Forma de eliminar un elemeto"""
del lista[2]
print(lista)
"""Quitar el elemeto dando su valor"""
lista.remove(9)
print(lista)

"""Concatenacion de Listas"""
lista.extend(lista2+lista3)
print(lista)

"""Contar cuantas veces existe un elemento en la lista"""
print(lista.count("Hola"))

"""Ordenar una lista"""
lista4 = [5, 7, 9, 2, 6, 1, 7]
lista4.sort()
print(lista4)
lista4.sort(reverse=True)
print(lista4)
