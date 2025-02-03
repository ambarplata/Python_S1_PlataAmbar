## crear la secuencia fibonacci y despues imprementarla con nuevos numeros

def analizar_fibonacci(n):

    num1 = 0
    num2 = 1
    pares = []  
    suma_fibonacci = 0  

    print("Serie de Fibonacci:")
    for i in range(n):
        print(num1)
        if num1 % 2 == 0:
            pares.append(num1)  # Añadimos el número par a la lista
        suma_fibonacci += num1  # Sumamos el número actual a la suma
        num3 = num1 + num2
        num1 = num2
        num2 = num3

    print("Números pares en la serie:")  # Imprimimos los números pares al final
    for par in pares:
        print(par)

    print("Suma de la serie de Fibonacci:", suma_fibonacci)  # Imprimimos la suma

# Ejemplo de uso:
n = int(input("Ingresa el largo de la serie: "))
analizar_fibonacci(n)

## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296  c