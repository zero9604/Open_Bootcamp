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

# Creamos la clase padre
class vehiculo:
    
    # Inicializamos los atributos
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
# Creamos la clase hija
class coche(vehiculo):

    # inicializamos los atributos
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    # Creamos el siguiente metodo para la visualización de la clase por medio de un print
    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, 
                                                                        self.velocidad, 
                                                                        self.ruedas, self.puertas, 
                                                                        self.cilindrada )

#--------------------------------------------Programa principal-----------------------------------------#

# Instanciamos e imprimimos el objeto "deportivo"
deportivo = coche('negro',4,3,200,125)
print(deportivo)





