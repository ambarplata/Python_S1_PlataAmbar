## Enteros Positivos hasta 680
print ("Los numeros que satisfacen la expresion dada son: ")
for p in range (0,680): 
    for q in range (0,680):
        expresionmatematica= p**3+q**4-2*p**2
        if (expresionmatematica<680):
            print ("p:",p)
            print ("q:",q)
            print ("sumatoria" , expresionmatematica)
## Desarollado por Ambar Isabella Plata Lopez / T.I 1102635296 