# lista (array) unidimencional - numeros enteros
listaNumeros= [1,2,3,4,5,6,7,8,9,10]
# varible
suma = 0
mayorNumero = listaNumeros[0]

# Buclw FOR -Para conntar el mayor numero
for varNumero in listaNumeros:
    if varNumero > mayorNumero:
      mayorNumero = varNumero
    
#print("El numero mayor es: ", mayorNumero)
for varNumero in listaNumeros :
    suma += varNumero
    if varNumero > mayorNumero:
        mayorNumero = varNumero
        
        
print("El numero mayor. ", mayorNumero)
print()