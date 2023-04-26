
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

# Parte 3.

"""Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez."""

# python no posee el ciclo do while, sin embargo una forma para emularlo es la siguiente
# Repetimos lo anterior mente realizado.

numeroWhile = int(input("Por favor ingrese un número entero para el valor de \"numeroWhile\" \n"))

print(numeroWhile)
numeroWhile = numeroWhile + 1

while(numeroWhile<3):
    print(numeroWhile)
    numeroWhile = numeroWhile + 1

# De esta forma imprimimos antes de entrar al ciclo while, lo cual en sintesis es lo qu erealiza el
# ciclo do while

# Parte 4.

""" Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición 
será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla."""

# Creamos la variable numeroFor

for numeroFor in range(0, 4):
    print(numeroFor)

# El ciclo for en python es algo distinto, sin embargo cumple las condiciones solicitadas.

# Parte 5.

"""Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor 
de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación."""

estacion = input(" Por favor ingrese la estación del año \n").lower() # Guarda el texto escrito en minusculas

if estacion == "primavera":
    print("Nos encontramos en la estación \"primavera\" \n")

elif estacion == "verano":
    print("Nos encontramos en la estación \"verano\" \n")

elif estacion == "otoño":
    print("Nos encontramos en la estación \"otoño\" \n")

elif estacion == "invierno":
    print("Nos encontramos en la estación \"invierno\" \n")

else:
    print("Se introdujo un aestación no valida: \n")



