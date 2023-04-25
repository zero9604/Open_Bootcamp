def funcionSuma(a,b,c):
    return a+b+c

class coche:
    puertas = 4

    def __init__(self, puertas):
        self.puertas = puertas

    def agregarPuerta(self):
        self.puertas = self.puertas + 1

    def quitarPuerta(self):
        self.puertas = self.puertas - 1





# Primera parte:
"""Crear una función con tres parámetros que sean números que se suman entre sí.
Llamar a la función en el main y darle valores."""

# Permitimos al usuario ingresar valores por consola que posteriormente se sumaran y devolverna el resultado
# mostrandolo por pantalla
print("Parte #1 del ejercicio: \n")
v1 = float(input("Ingrese un primer valor númerico: \n"))
v2 = float(input("Ingrese un segundo valor númerico: \n"))
v3 = float(input("Ingrese un tercer valor númerico: \n"))

resultado = funcionSuma(v1,v2,v3) # Llamamos a la función "funcionSumas" y le damos valores v1,v2,v3.
print(f"El resultado es: {resultado}\n") 
print("------------------------------------------------------------")

# Segunda parte:

print("Parte #2 del ejercicio: \n")
""" Crear una clase coche.
Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
Una función que incremente el número de puertas que tiene el coche.
Crear un objeto miCoche en el main y añadirle una puerta.
Mostrar el número de puertas que tiene el objeto. """

# Al iniciondel programa tenemos la clase coche, contruida con su variable númerica que define
# el número de puertas que tiene el objeto y la función que incrementea el número de puertas que tiene el coche
# como añadido, tenemos la función que decrementa las puertas del coche

# Procederemos a crear el objeto "miCoche"
p = int(input("Por favor ingrese el número de puertas que tendra el coche \n"))
miCoche = coche(p)
print (f"El coche tiene {miCoche.puertas} puertas") # Muestra "p" puertas en el coche

miCoche.agregarPuerta()
miCoche.agregarPuerta()
miCoche.agregarPuerta()

print (f"El coche tiene {miCoche.puertas} puertas") # Muestra "p+3" puertas en el coche

miCoche.quitarPuerta()
miCoche.quitarPuerta()
miCoche.quitarPuerta()

print (f"El coche tiene {miCoche.puertas} puertas") # Muestra "p" puertas en el coche

print("------------------------------------------------------------")