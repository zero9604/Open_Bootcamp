"""
Crea una clase Persona con las siguientes variables:

* La edad
* El nombre
* El teléfono

Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.
Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador."""

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



class Cliente (Persona):
    
    def __init__(self, _edad, _nombre, _telefono, _credito):
        super().__init__(_edad, _nombre, _telefono)
        self._credito = _credito

    def setCredito(self, _credito):
        self._credito = _credito

    def getCredito(self):
        return self._credito


class Trabajador (Persona):
    
    def __init__(self, _edad, _nombre, _telefono, _salario):
        super().__init__(_edad, _nombre, _telefono)
        self._salario = _salario

    def setSalario(self, _salario):
        self._salario = _salario

    def getSalario(self):
        return self._salario
    
# Programa principal.

cliente_1 = Cliente(12, 'Roberto', 4756988, 100)
trabajador_1 = Trabajador(30, 'Ricardo', 3015764656, 300)

print("Información del cliente: ")
print(f"Edad:     {cliente_1.getEdad()} \n"
    f"Nombre:   {cliente_1.getNombre()} \n" 
    f"Telefono: {cliente_1.getTelefono()} \n"
    f"Credito:  {cliente_1.getCredito()}  \n")

print("--------------------------- \n")
print("Información del trabajador: ")
print(f"Edad:     {trabajador_1.getEdad()} \n"
    f"Nombre:   {trabajador_1.getNombre()} \n" 
    f"Telefono: {trabajador_1.getTelefono()} \n"
    f"Salario:  {trabajador_1.getSalario()}  \n")

