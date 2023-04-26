
# Parte 1.

"""Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
Pista: Los números inferiores a 0 son negativos y los superiores, positivos."""

numeroIf = float(input("Por favor ingrese un número para  comparar si es positivo, negativo o cero: \n"))

if (numeroIf == 0 ):
    print("la variable numeroIf es igual a cero. \n")

elif(numeroIf > 0):
    print("la variable numeroIf es un número positivo. \n")

elif(numeroIf < 0):
    print("la variable numeroIf es un número negativo. \n")

# Parte 2.

"""Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
Incrementar el valor de la variable en uno cada vez que se ejecute.
Mostrarlo por pantalla cada vez que se ejecute."""

numeroWhile = int(input("Por favor ingrese un número entero para el valor de \"numeroWhile\" \n"))

while(numeroWhile<3):
    print(numeroWhile)
    numeroWhile = numeroWhile + 1



