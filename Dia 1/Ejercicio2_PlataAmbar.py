## Serie con numero entero N
CantidadD = int(input("ingresa el numero de la sucesion"))
if CantidadD<= 0: 
    print ("0")

sum=0 
for i in range (1,CantidadD):
    if (i%2==0):
       sum=sum-(1/i)
    else:
       sum=sum+(1/i)

print ("la sumatoria dio: ", sum)

## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 

 
