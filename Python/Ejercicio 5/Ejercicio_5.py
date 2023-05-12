"Escribe una función que pueda decirte si un año (número entero) es bisiesto o no."

def biciesto(año):

    # Verificamos si el año es divisible por 4, secular  y divisible entre 400
    if año % 4 == 0 and (año % 100 !=0 or año %400 ==0):        

        return "Año biciesto (366 días)"
    return "Año no biciesto (365 días)"
    
for i in range(1,11):
    a = int(input("Por favor ingrese un año: \n"))
    print(biciesto(a))

