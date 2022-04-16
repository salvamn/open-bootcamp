class Vehiculo:
    color = None
    ruedas = None
    puertas = None
    
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
class Coche(Vehiculo):
    velocidad = None 
    cilindrada = None
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada  = cilindrada
        
    def __str__(self) -> str:
        return f"Color: {self.color}\nRuedad: {self.ruedas}\nPuertas: {self.puertas}\nVelocidad: {self.velocidad}\nCilindrada: {self.cilindrada}"
        
c = Coche("Azul", 4, 4, 100, 12)
print(c)
        