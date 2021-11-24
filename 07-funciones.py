#PARA DEFINIFIR UNA FUNCIÓN UTILIZO LA PALABRA RESERVADA DEF.

def suma(lista):
    x = 0
    for elem in lista:
        x += elem       #ES IGUAL QUE DECIR 'x + elem'
    return x            #ESTA PALABRA SE UTILIZA PARA DEVOLVER VALORES

sumatoria = suma([1,2,3,4,5])

print(sumatoria)