print("Hola mundo")

#DECLARACIÓN DE VARIABLES

#PUEDEN SER:
# A) ASIGNADAS DE FORMA INDIVIDUAL

x = 5

# B) ASIGNADAS DE FORMA MULTIPLE

y,z = 3,4

suma = y+z
#print(suma)

#TIPOS DE DATOS PRIMITIVOS

# x = 3                        --> enteros
# y = 3.5                      --> decimales (float) flotantes
# varible = "cadena de txt"    --> strings 
# varible = 'cadena de txt'    --> strings
# z = True                     --> boolean
# z = False                    --> boolean

#CASTING

#SE DENOMINA AL CAMBIO DE VARIABLE. OBSERVAR SGTE. EJEMPLO:

# x = '3'
# x = int(x) EN ESTE CASO LA VARIBLE SE CONVIRTIÓ DE STRING A ENTERO CON INT
# x = str(x) EN ESTE CASO DE VOLVIÓ A CONVERTIR LA VARIBLE X EN STRING

#OPERACIONES ENTRE VARIABLES

#ENTEROS Y FLOTANTES SOPORTAN OPERACIONES ARITMÉTICAS

# 22/4      --> DIVISIÓN CONVENCIONAL, ENTREGA ENTERO Y FLOTANTES
# 22//4     --> DIVISIÓN ENTERA. ENTREGA SÓLO EL NÚMERO ENTERO
# 22%4      --> DIVISIÓN MÓDULO. ENTREGA EL RESTO

a = 22/4      
b = 22//4     
c = 22%4      

print(c)

#OPEREACIONES CON STRINGS
#EL SÍMBOLO + ENTRE STRINGS CONCATENA
#EL SÍMBOLO * LUEGO DE UNA CADENA, REPITE LA CANTIDAD DE VECES INDICADA

string1 ='cadena'
repeticion = string1*4
print(repeticion)

#REASIGNACIÓN Y OPERACIÓN AL MISMO TIEMPO

x = 5
x = x+1
x += 1  # AMBAS SINTAXIS SON EQUIVALENTES E IMPLICAN REASIGNACIÓN Y OPERACIÓN AL
        # MISMO TIEMPO

print(x)

# SALIDAS POR PANTALLA

print(2, 4, 'Hola mundo')



