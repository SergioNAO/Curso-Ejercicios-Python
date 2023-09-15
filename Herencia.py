class Producto:
    def __init__(self,nombre,precio,descripcion):
        self.nombre=nombre
        self.precio=precio
        self.descripcion=descripcion

    def __str__(self):
        return f"Nombre: {self.nombre}\n"\
            f"Precio: {self.precio}\n"\
            f"Descripcion: {self.descripcion}"
class Accesorios(Producto):
    pass

accesorios=Accesorios("Vaso",40,"Vaso de Cristal")

class Cocina(Producto):
    distribuidor=""

    def __str__(self):
        return f"Nombre: {self.nombre}\n" \
               f"Precio: {self.precio}\n" \
               f"Descripcion: {self.descripcion}\n" \
               f"Distribudor: {self.distribuidor}"\

Carne=Cocina("Carne",100,"Carne de Res")
Carne.distribuidor="Carnes S.a de C.V"

class Libro(Producto):
    autor=""
    def __str__(self):
        return f"Nombre: {self.nombre}\n" \
               f"Precio: {self.precio}\n" \
               f"Descripcion: {self.descripcion}\n" \
               f"Autor: {self.autor}\n" \

Lib1=Libro("El Principito",150,"Libro para niños pequeños")
Lib1.autor="Antoine de Saint-Exupery"

print(accesorios,"\n")
print(Carne,"\n")
print(Lib1)

