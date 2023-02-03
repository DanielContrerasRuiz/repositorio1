class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un ', self.tipo, ' y mi sonido es el', self.onomatopeya)


class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'Maullido')
gato.saludo()

perro = Perro('Tobby', 'ladrido')
perro.saludo()

canario = Canario('Piolon', 'piopio')
canario.saludo()


