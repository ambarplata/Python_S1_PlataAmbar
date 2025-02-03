## Mayor y menor de 10 numeros 
pequeño=0
grande=0
for i in range (1,10):
    n=int(input("ingrese los numeros: "))
    if i==1:
       grande=n
       pequeño=n 
    elif n> grande:
        grande=n
    elif n<pequeño:
        pequeño=n 

print("grande" , grande)
print("pequeño" , pequeño)

## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 