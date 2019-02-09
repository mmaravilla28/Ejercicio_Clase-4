#Ejemplo de creación de clases y herencia
#creación de la clase animal y pato
class Animal:
    numero_de_animales = 0

    def __init__(self,):
        print('Creando un animal')
        self.estoy_vivo = True
        Animal.numero_de_animales += 1

    def crecer(self):
        print('Soy un animal y estoy creciendo')

    def respirar(selg):
        print('Soy un animal y estoy respirando')

    def estoy_vivo(self):
        print('Soy un animal y estoy respirando')

    def reproducir(self):
        print('Soy un animal y me estoy reproduciendo')

    def morir(self):
        self.estoy_vivo = False
        print('Fuí un animal')

    def vivir_o_morir(self):
        self.estoy_vivo = not self.estoy_vivo

class Pato(Animal):
    def __init__(self, nombre_pato='pato', ala_color='blanca', pico_color='cafe'):
        self.nombre_pato = nombre_pato
        self.ala_color = ala_color
        self.pico_color = pico_color
        super().__init__() #hereda de la clase principal Animal
        print('Creando un pato...y me llamo: {}'.format(self.nombre_pato))


    def __str__(self):
        #Para soportar el print de una clase pato
        return 'Soy un pato, me llamo: {} ' \
               'y tengo el ala de color {} y el pico de ' \
               'color {}'.format(self.nombre_pato, self.ala_color, self.pico_color)

    def __repr__(self):
        return self.nombre_pato

    def __add__(self, other): #método especial para sumar instancias de tipo pato
        #Pato 1 + Pato 2 -> self + other
        return Pato(ala_color=self.ala_color, pico_color=other.pico_color)


# Este método hereda de la clase principal Animal
#    def respirar(self):
#        print('Hola soy un Pato pero ...')
#        super().respirar()

Donal = Pato('Donal', pico_color='verde', ala_color='negro')   #Donal.respirar()
Daisy = Pato('Daisy', pico_color='azul', ala_color='rojo')
#Hugo = Pato('Hugo')
#Luis = Pato('Luis')
#animalito = Animal()

print('Sumando 2 patos:', Donal + Daisy)

#print('soy un pato --->', Daisy)

#Para saber cuántos animales han sido creados
#print('Numero de animales ', Animal.numero_de_animales)

#animalito = Animal()
#print('¿Estoy vivo?', animalito.estoy_vivo)
#print('Crezca', animalito.crecer())

#estatus = 'inicial'
#estatus = animalito.respirar()

#if estatus is None:
#    print('que salvada, el animal respiró')
#else:
#    print('Más noticias a las 6...')


