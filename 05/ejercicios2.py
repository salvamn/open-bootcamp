class Alumno:
    nombre = None
    nota = None
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def aprobado(self):
        if self.nota >= 4:
            return True
        return False
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}\nNota: {self.nota}")
        

a1 = Alumno("Salvador", 6)
a1.imprimir()
print(f"Aprobo: {a1.aprobado()}")

a2 = Alumno("Tomas", 2)
a2.imprimir()
print(f"Aprobo: {a2.aprobado()}")