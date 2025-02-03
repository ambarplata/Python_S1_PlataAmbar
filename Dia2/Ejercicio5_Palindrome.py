## escribe y mira si es un palindrome 
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

# Solicitar la palabra al usuario
palabra_ingresada = input("Ingresa una palabra: ")

# Verificar si es palíndromo y mostrar el resultado
if es_palindromo(palabra_ingresada):
    print(f"'{palabra_ingresada}' es un palíndromo.")
else:
    print(f"'{palabra_ingresada}' no es un palíndromo.")

## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296  