def area_triangulo(altura, base):
    area = (altura * base) / 2
    return area

def area_circulo(radio):
    area = 3.1416 * (radio * radio)
    return area

print(area_triangulo(10, 20))
print(area_circulo(5))