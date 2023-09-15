autores={"Libro 1":"Kendall","Libro 2":"Perez","Libro 3":"Luis"}

print(autores.keys())
print(autores.values())
for autor in autores:
    print(autor)

"""autores.clear()"""
print(autores)

diccionario={"Libro 1":"Carro"}
autores.update(diccionario)

print(autores)

print(autores.get("Libro 1"))
