import random
#PERMITEN REPETIR TROZOS DE CÓDIGO VARIAS VECES

#FOR
#SE UTILIZA PARA REPETIR UN FRAGMENTO DE CÓDIGO UN NÚMERO CONOCIDO DE VECES


# x = 0
# for i in range(10):
#     print (i)
#     x += random.randint(1,5)

#print(x)


#WHILE
#SE UTILIZA CUANDO NO SE CONOCE CUNATAS VECES HAY QUE REPETIR o MIENTRAS SE MANTIENE UNA CONDICIÓN

x = 0
while x != 5:
    x = (random.randint(1, 100))
    #break      --> ROMPE EL CICLO
    #continue   --> CONTINUA EL CICLO
print(x)