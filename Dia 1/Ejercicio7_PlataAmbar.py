## numeros amigos 
n1=int(input("ingresa n1: ")) 
n2=int(input("ingrese n2: "))
suma1=0
suma2=0  
for i in range (1,n1-1):
    if (n1%i == 0):
        suma1+=i
for i in range (1,n2-1):
    if(n2%i == 0): 
        suma2+=i 

if suma1== n2 and suma2==n1: 
    print (n1, "y" , n2, "son numeros befos")
else:
    print (n1, "y" , n2, " no son befos" )
## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 

