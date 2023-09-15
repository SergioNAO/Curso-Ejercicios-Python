class Profesor:
    nombre=""
    edad=28
    materia="Ingles"
    def enseñar(self):
        print("Tienes tarea para mañana")
        print("De la materia",self.materia)
        
Juan=Profesor()
Juan.enseñar()

