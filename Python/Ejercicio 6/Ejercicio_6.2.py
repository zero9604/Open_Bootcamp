"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga 
como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

# Creamos la clase almuno
class alumno:

    def __init__(self, _nombre, _nota):
        self._nombre = _nombre
        self._nota = _nota
    
    def setNombre(self , _nombre):
        self._nombre = _nombre

    def getNombre(self):
        return self._nombre
    
    def setNota(self , _nota):
        self._nota = _nota

    def getNota(self):
        return self._nota
    
    def aprobado(self):
        if self._nota >= 3.0:
            return "El Alumno aprobo"
        else:
            return "El Alumno reprobo"
    

estudiante = alumno("Mateo", 3)

print(estudiante.aprobado())