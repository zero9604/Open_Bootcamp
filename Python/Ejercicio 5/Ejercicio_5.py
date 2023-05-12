"Escribe una función que pueda decirte si un año (número entero) es bisiesto o no."

def biciesto(año):
    a = False
    if año % 4 == 0:        
        if año % 100 == 0 and año % 400 ==0:          # Verificamos si el año es secular
            return "Año biciesto (366 días)"
        
        elif año % 100 !=0:
            return "Año biciesto (366 días)"

    return "Año no biciesto (365 días)"
    
print(biciesto(1992))
print(biciesto(2000))
print(biciesto(1900))
