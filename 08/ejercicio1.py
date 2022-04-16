paises = []

print("¿ Cuantos paises deseas agregar ?")

numero_paises = int(input(">>> "))

while numero_paises > 0:
    print("Ingresa el pais")
    pais = input(">>> ")
    paises.append(pais)
    numero_paises -= 1
    
eliminar_repetidos = set(paises)
paises = list(eliminar_repetidos)
paises.sort()
print(paises)