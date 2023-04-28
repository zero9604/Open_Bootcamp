"""Para practicar la encapsulación:
* Crear clase Persona.
* Crear variables las privadas edad, nombre y telefono de la clase Persona.
* Crear gets y sets de cada propiedad.
* Crear un objeto persona en el main.
* Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola."""

class Persona:
  

    def __init__(self, _edad, _nombre, _telefono):
        self._edad = _edad
        self._nombre = _nombre
        self._telefono = _telefono

    def setEdad(self, _edad):
        self._edad = _edad

    def getEdad(self):
        return self._edad
    
    def setNombre(self, _nombre):
        self._nombre = _nombre

    def getNombre(self):
        return self._nombre
    
    def setTelefono(self, _telefono):
        self._telefono = _telefono

    def getTelefono(self):
        return self._telefono



# Programa principal.

# Creamos el objeto persona_1
persona_1 = Persona(12,'Roberto', 4756988)

print(persona_1.getEdad())
print(persona_1.getNombre())
print(persona_1.getTelefono())

# Cambiamos atributos del objeto
persona_1.setEdad(27)
persona_1.setNombre('Mateo')
persona_1.setTelefono(3014948366)

print('-----------------')

# Imprimimos los nuevos atributos
print(persona_1.getEdad())
print(persona_1.getNombre())
print(persona_1.getTelefono())

"""NOTA: En Python, los atributos y metodos privados no existen pues todos se tratan como publicos,
sin embargo por convención se utiliza "_" para "tratar" estos elementos como privados (no es que se vuelvan
 privados con esto, si no que los desarrolladores los tratan como atributos privados)"""