##interes simple 

def calcular_interes_simple(capital, tasa, tiempo):
    interes=capital*tasa*tiempo
    return interes 

capital=float(input("ingresa el capital inicial "))
tasa=float(input("ingresa la tasa de interes anual,en decimas "))
tiempo=int(input("ingresa el tiempo en años "))

interes_generado= calcular_interes_simple(capital,tasa,tiempo)

print(f"El interes simple generado es:{interes_generado}" )

def calcular_interes_compuesto(capital, tasa, tiempo ):
    capital_final=capital*(1+tasa)** tiempo 
    return capital_final 

print("Ahora ingrese los datos para su interes compuesto")

capital = float(input("Ingresa el capital inicial: "))
tasa = float(input("Ingresa la tasa de interés anual (en decimal): "))
tiempo = float(input("Ingresa el tiempo en años: "))

capital_con_interes_compuesto = calcular_interes_compuesto(capital, tasa, tiempo)
print(f"El capital final con interés compuesto es: {capital_con_interes_compuesto}")

## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 