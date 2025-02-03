##convierte celsius a farenheit y contrario
def CelsiusToFarenheit(c):
    #Esta funcion convierte los grados Celcius a grados Farenheit#
    conversion = (c * 9/5) + 32
    return conversion

def FarenheitToCelcius(f):
    #Esta funcion convierte los grados Farenheit a grados Celcius#
    conversion = 5/9*(f - 32)
    return conversion

pregunta = input("Ingrese c para convertir a grados Celcius y f para convertir a grados Farenheit ")
print(pregunta)
if (pregunta == "f"):
    solicitarTemperatura = float(input("Ingrese la temperatura en grados Celcius: "))
    print(solicitarTemperatura)
    resultado = CelsiusToFarenheit(solicitarTemperatura)
    print("La temperatura en grados Farenheit es: ", resultado)
elif (pregunta == "c"):
    solicitarTemperatura = float(input("Ingrese la temperatura en grados Farenheit: "))
    print(solicitarTemperatura)
    resultado = FarenheitToCelcius(solicitarTemperatura)
    print("La temperatura en grados Celcius es: ", resultado)
else:
    print("Has ingresado mal la letra")
    
    ## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 