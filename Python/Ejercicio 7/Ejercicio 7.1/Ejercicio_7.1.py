"""
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
Los resultados tenéis que mostrarlos por consola.
"""

# Importamos el modulo calculadora
import calculadora

# Solicitamos al usuario dos números flotantes
n1 = float(input("Por favor ingrese un primer valor: "))
n2 = float(input("Por favor ingrese un primer valor: "))

# Imprimimos las operaciones realizadas con ambos números
print(f"la suma de ambos números es: {calculadora.sumar(n1,n2)}")
print(f"la resta de ambos números es: {calculadora.restar(n1,n2)}")
print(f"la multiplicación de ambos números es: {calculadora.multiplicar(n1,n2)}")
print(f"la división de ambos números es: {calculadora.dividir(n1,n2)}")


