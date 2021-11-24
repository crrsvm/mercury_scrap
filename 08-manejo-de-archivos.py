#MODOS DE APERTURA DE UNA ARCHIVO

# 'r' => LEER
# 'a' => AGREGAR
# 'w' => ESCRIBIR DESDE 0

f = open('/Users/cristobalsilvamanzo/Documents/repositorios/python/durazno.txt', 'r')

#print( f.readlines()) #LEE EL ARCHIVO DE UNA VEZ

#PARA ITERAR ARCHIVO:

for line in f:
    line = line.strip() # SE ELIMINAN LOS SALTOS DE LINEA 
    print(line)

    line = line.split(',') #SE LE DA FORMATO LISTA CONSIDERANDO EL PARAMETRO ','
    print(line)

    print(line[0])   #SE SELECCIONA EL ELEMENTO CON ÍNDICE 0.

#PARA AGREGAR INFO A UN ARCHIVO

f = open('/Users/cristobalsilvamanzo/Documents/repositorios/python/durazno.txt', 'a')

f.write('Melón,4,10\n') #SE AGREGA EL SALTO DE LÍNEA PARA QUE LOS ELEMENTOS APAREZCAN EN LA FILA SIGUIENTE


#CONSIDERAR QUE AL MOMENTO DE UTILIZAR 'w' SE REESCRIBE EL ARCHIVO, POR LO TANTO, SE SUGIERE 
#CAMBIAR EL NOMBRE PARA QUE NO SE REEMPLACE.

f = open('/Users/cristobalsilvamanzo/Documents/repositorios/python/durazno-nuevo.txt', 'w')

f.write('Hola mundo')



