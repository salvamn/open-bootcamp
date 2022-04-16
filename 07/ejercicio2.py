import pickle

class Vehiculo:
    color = None
    marca = None
    modelo = None
    
    def __init__(self, color, marca, modelo) -> None:
        self.color = color
        self.marca = marca
        self.modelo = modelo
        
    
        
archivo = "vehiculo.bin"

v1 = Vehiculo("rojo", "Ford", "Fiesta")


def escribir_bin(archivo, dato):
    with open(archivo, "ab") as f:
        f.write(dato)
        
        
def mostrar_contenido_archivo(archivo):
    with open(archivo, "rb") as f:
        dato = pickle.load(f)
        print(dato.color, dato.marca, dato.modelo)
        
        
escribir_bin(archivo, pickle.dumps(v1))
mostrar_contenido_archivo(archivo)