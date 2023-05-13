"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga 
como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

# Creamos la clase Almuno
class Alumno:

    # Metódo para inicializar los atributos 
    def inicializar(self, _nombre, _nota):
        self._nombre = _nombre
        self._nota = _nota
    
    def imprimir(self):
        print("Nombre:", self._nombre)
        print("Nota:", self._nota)

    def resultado(self):
        if self._nota < 3:
            print(f"El alumno {self._nombre}, ha suspendido con una nota de {self._nota}.")
        else:
            print(f"El alumno {self._nombre}, ha aprobado con una nota de {self._nota}.")
    
# -------------------------------Programa principal-----------------------------------------------------#

# Creamos los objetos
alumno1 = Alumno()
alumno2 = Alumno()

# Inicializamos sus atributos
alumno1.inicializar("Mateo", 3)
alumno2.inicializar("Daniela", 2.3)

# Imprimimos los atributos de cada objeto
alumno1.imprimir()
alumno2.imprimir()

# Motramos si cada alumno aprueba o reprueba
alumno1.resultado()
alumno2.resultado()