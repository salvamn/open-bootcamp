from functools import reduce

lista_numeros = [i for i in range(1, 51)]

obtener_impares = filter(lambda x: x % 2 != 0, lista_numeros)

suma_numeros = reduce(lambda x, y: x + y, obtener_impares)

print(suma_numeros)