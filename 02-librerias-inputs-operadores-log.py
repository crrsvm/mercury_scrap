#BIBLIOTECAS O LIBRERÍAS
#TIENEN FUNCIONES O TROZOS DE CÓDIGO QUE EJECUTAN ACCIONES 
#Y SÓLO NECESITAMOS IMPORTARLAS UTILIZANDO LOS SIGUIENTE: 

#HAY 3 FORMAS DE IMPORTAR


#A) IMPORTACIÓN POR EL NOMBRE DE LA LIBRERÍA

import random
random.randint(1,5)


#B) IMPORTACIÓN DE FUNCIÓN ESPECÍFICA DE LA LIBRERÍA

from random import randint
randint(1,5)

#C) IMPORTACIÓN TODAS LAS FUNCIONES DE UNA LIBRERÍA

from random import *

randint(1,5)
random()


x = input('Ingresa un valor numérico ' )

print('El valor ingresado es ' + (x))

