import time

hora_actual = time.strftime("%H:%M:%S %p")
lista = hora_actual.split(":")
hora = int(lista[0])

if hora >= 20: # 20:00 = 08:00 de la noche
    print("Es hora de irse a casa")
    
elif hora < 20 and hora >= 8:
    print("Sigue trabajando") 
    
elif hora < 8:
    print("sigue durmiendo")

