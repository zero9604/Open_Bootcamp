"Escribe una función que pueda decirte si un año (número entero) es bisiesto o no."

def bisiesto(año):

    # Verificamos si el año es divisible por 4, secular  y divisible entre 400
    if año % 4 == 0 and (año % 100 !=0 or año %400 ==0):        

        return "Año bisiesto (366 días)"
    return "Año no bisiesto (365 días)"
    
a = int(input("Por favor ingrese un año: \n"))
print(bisiesto(a))

