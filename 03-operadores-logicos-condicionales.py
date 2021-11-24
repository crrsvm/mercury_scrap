import random
##OPERADORES LÓGICOS Y CONDICIONALES

# <  
# >
# >=
# =<
# == IGUAL
# != NO ES IGUAL

#LAS 3 CONDICIONALES EN PYTHON:

#if(condicion1):
    #código

# elif(condicion2):
    #código en secuencia a la primera condición)
# else:
    #código se ejecuta si no se cumplen las cond. anteriores.


#EJEMPLO

x = 5
y = 4

#print(x>=5 and y<=4)

x = random.randint(1,5)

if x == 1:
    print('Soy igual a 1')
elif x == 2:
    print('Soy el número 2')
else:
    print('Soy algún otro número')
print(x)
