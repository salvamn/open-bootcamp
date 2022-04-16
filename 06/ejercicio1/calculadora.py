from operaciones import suma
from operaciones import resta
from operaciones import multiplicacion
from operaciones import division

def main():
    operaciones = ["suma", "resta", "multiplicacion", "division"]
    resultado = None
    
    print("Que operacion deseas realizar ?\n1. sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    
    opcion = int(input(">>> "))
    
    numero1 = int(input("Ingresa el primer numero:\n>>> "))
    numero2 = int(input("Ingresa el segundo numero:\n>>> "))
    
    if opcion == 1:
        resultado = suma(numero1, numero2)
    
    elif opcion == 2:
        resultado = resta(numero1, numero2)
        
    elif opcion == 3:
        resultado = multiplicacion(numero1, numero2)
        
    elif opcion == 4:
        resultado = division(numero1, numero2)
        
    elif opcion == 5:
        print("Adios.")
        exit()
        
    print(f"El resultado de la {operaciones[opcion - 1]} es: {resultado}")


if __name__ == "__main__":
    main()