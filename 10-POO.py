#CLASES Y OBJETOS. 
#RECORDAR QUE LAS CLASES SON LOS MOLDES Y LOS OBJETOS SON LAS INSTANCIAS DE LAS CLASES.
#LAS CLASES TIENE  MÉTODOS(FUNCIONES) Y ATRIBUTOS(CARACTERÍSTICAS).


class Casa:

#EL MÉTODO CONSTRUCTOR O FUNCIÓN CONSTRUCTORA SE ENCARGA DE CONSTRUIR
#LA VARIABLE self SE UTILIZA PARA CAMBIAR EL VALOR DE ALGUNA PROPIEDAD DLE OBJETO

    def __init__(self, color): 
        self.color = color
        self.consumo_de_luz = 0
        self.consumo_de_agua = 0
    
    def pintar(self, color):
        self.color = color

    def prender_luz(self):
        self.consumo_de_luz += 10

    def abrir_ducha(self):
        self.consumo_de_agua += 10

    def tocar_timbre(self):
        print('RIIIIINNNGG!!!')
        self.consumo_de_luz += 2
        
#PARA CREAR UN OBJETO SE EJECUTA LO SIGUIENTE:
mi_casa = Casa('rojo') 

#PARA ACCEDER A LAS PROPIEDADES DE NUESTRO OBJETO LA SINTAXIS ES LA SIGUIENTE:
print(mi_casa.color)

mi_casa.tocar_timbre() #AL EJECUTAR EL MÉTODO TOCAR TIMBRE, AUMENTA EL CONSUMO DE LUZ EN 2.
print(mi_casa.consumo_de_luz)

mi_casa.pintar('verde')     #LA FUNCIÓN PINTAR CAMBIA LA PROPIEDAD QUE TIENE EL BOJETO MI CASA.
print(mi_casa.color)


#HERENCIA. SE EXTIENDEN LAS PROPIEDADES DE LA CASA. SE EJECUTA UTILIZANDO 
# LA CLASE PADRE DENTRO DE LOS PARÉNTESIS

class Mansion(Casa):

    def prender_luz(self):
        self.consumo_de_luz += 50

    def abrir_ducha(self):
        self.consumo_de_agua += 50

    def tocar_timbre(self):
        print('DING-DONG')
        self.consumo_de_luz +=3

mi_mansion = Mansion('blanco')
print(mi_mansion.color)

mi_mansion.tocar_timbre()

mi_mansion.pintar('verde')
print(mi_mansion.color)
    