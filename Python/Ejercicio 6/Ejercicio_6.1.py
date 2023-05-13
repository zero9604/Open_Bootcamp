"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
* Color
* Ruedas
* Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

* Velocidad

* Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""


class vehiculo:
    color = ''
    ruedas = 0
    puertas = ''

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    

class coche(vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

deportivo = coche('negro',4,3,50,125)
print(deportivo.color)
print(deportivo.ruedas)
print(deportivo.puertas)
print(deportivo.velocidad)
print(deportivo.cilindrada)





