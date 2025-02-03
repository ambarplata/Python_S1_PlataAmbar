import random
import string

def generar_contraseña(longitud, caracteres_excluidos):
    """Genera una contraseña aleatoria de la longitud especificada, excluyendo los caracteres indicados."""

    # Verifica que la longitud ingresada sea válida
    while True:
        try:
            longitud = int(longitud)
            if longitud > 0:
                break
            else:
                print("La longitud debe ser un número entero positivo.")
                longitud = input("Ingrese la longitud de la contraseña: ")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
            longitud = input("Ingrese la longitud de la contraseña: ")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    caracteres_filtrados = ''.join(caracter for caracter in caracteres if caracter not in caracteres_excluidos)

    if not caracteres_filtrados:
        return "No hay caracteres disponibles para generar la contraseña con las restricciones especificadas."

    contraseña = ''.join(random.choice(caracteres_filtrados) for i in range(longitud))
    return contraseña

# Solicita al usuario la longitud de la contraseña
longitud = input("Ingrese la longitud de la contraseña: ")

# Solicita al usuario los caracteres a excluir
caracteres_excluidos = input("Ingrese los caracteres que no desea incluir en la contraseña (ej: aeiou123): ")

# Genera la contraseña y la muestra
contraseña_generada = generar_contraseña(longitud, caracteres_excluidos)
print("Contraseña generada:", contraseña_generada)

## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 