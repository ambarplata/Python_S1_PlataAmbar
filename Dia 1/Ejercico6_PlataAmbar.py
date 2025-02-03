##Empresa ACME
n = int(input("ingrese la cantidad de empleados: "))
totalBruto = 0
totalEPS = 0
totalPension = 0
totalNeto = 0
mayorSueldo = 0
nombreMayor = ""

print(f"\nIngrese el nombre del empleado 1:")
nombre = input()
print("Ingrese las horas trabajadas: ")
horas = int(input())

bruto = horas * 20000
eps = bruto * 0.04
pension = bruto * 0.04
neto = bruto - eps - pension

menorsueldo = neto 
nombreMenor = nombre

totalBruto += bruto
totalEPS += eps
totalPension += pension
totalNeto += neto

print(f"Empleado: {nombre}")
print(f"Sueldo Bruto: ${bruto}")
print(f"EPS: ${eps}")
print(f"Pensión: ${pension}")
print(f"Sueldo Neto: ${neto}")

for i in range(2, n + 1): 
    print(f"\nIngrese el nombre del empleado {i}:")
    nombre = input()
    print("Ingrese las horas trabajadas: ")
    horas = int(input())

    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension

    totalBruto += bruto
    totalEPS += eps
    totalPension += pension
    totalNeto += neto

    if neto > mayorSueldo:
        mayorSueldo = neto
        nombreMayor = nombre
    if neto < menorsueldo:
        menorsueldo = neto
        nombreMenor = nombre

    print(f"Empleado: {nombre}")
    print(f"Sueldo Bruto: ${bruto}")
    print(f"EPS: ${eps}")
    print(f"Pensión: ${pension}")
    print(f"Sueldo Neto: ${neto}")

promedioBruto = totalBruto / n
promedioNeto = totalNeto / n

print("\nResultados finales:")
print(f"Total Salarios Brutos: ${totalBruto}")
print(f"Total EPS: ${totalEPS}")
print(f"Total Pensión: ${totalPension}")
print(f"Total Salarios Netos: ${totalNeto}")
print(f"Empleado que más gana: {nombreMayor}, con un sueldo neto de ${mayorSueldo}")
print(f"Empleado que menos gana: {nombreMenor}, con un sueldo neto de ${menorsueldo}")
print(f"Promedio Salarios Brutos: ${promedioBruto}")
print(f"Promedio Salarios Netos: ${promedioNeto}")

## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 