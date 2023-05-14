import sys
import pprint
pprint.pprint(sys.path)

sys.path.append('Python\Pruebas de codigo\mismodulos')

import operaciones
import math

import saluda

def main():
    #op = operaciones.Operador()
    #print(op.multiplicacion(4, 2))
    #print(operaciones.PI)
    pprint.pprint(sys.path)
    saluda.saluda('Teo')

if __name__ == '__main__':
    main()  