"""Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable, 
 e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de 
 masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en 
 una carpeta comprimida zip."""

peso = float(input("Por favor ingrese su peso en Kilo gramos (Kg): \n"))
altura = float(input("Por favor ingrese su altura en metros (m): \n"))

imc = peso/(altura**2)
print(f"su IMC es: {imc}")
# NOTA: El IMC se calcula con el peso en kilogramos dividido la altura en metros elevada al cuadrados 