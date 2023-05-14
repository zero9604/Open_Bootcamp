"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
haréis una operación para calcular el tiempo que queda de trabajo.
"""
# Importamos el modulo time
import time

# time.time nos retorna la fecha y hora actual en segundos
# time.ctime le da un formato de dia mes hora minutos segundos y año
print(f"Fecha y tiempo actual: {time.ctime(time.time())}")

tiempo = time.localtime(time.time())

# time funciona en horario militar osea desde las 0 horas hasta las 23:59
if tiempo.tm_hour >=19:
    print("Es hora de ir a casa")
else:
    print(f"Faltan {18-tiempo.tm_hour} horas con {59-tiempo.tm_min} minutos para ir a casa")


#------------------------------------------Otra opción--------------------------------------------------#

"""
# Importamos el módulo time para poder coger la hora.
import time

# Inicializamos las variables y formateamos el tiempo para que solo se vean las horas y minutos
hora = time.strftime('%H') 
minutos = time.strftime('%M') 

# Comprobamos si la hora es mayor o igual a 19. Si es mayor, mostrará un mensaje y en el caso de que sea menor mostrará un mensaje informando de las horas y minutos que faltan para ir a casa.
if int(hora) >= 19:
	print ("Es hora de irse a casa") 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))
"""