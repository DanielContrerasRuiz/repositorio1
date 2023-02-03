# Primer ejecicio de funciones

def mifuncion():
    print('Mi primera función')

# mifuncion()

def ImprimeDato(*nombre):
    print('Mi nomnre es:', nombre[2])

# ImprimeDato('Chanchito', 'Feliz', 'Fernandez', 'el cojo')

def NombreCompleto(apellido, nombre):
    print(nombre, apellido)

# NombreCompleto(nombre='Chanchito', apellido='Feliz')

def NombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

# NombreCompleto2(nombre='Chanchito', apellido='Feliz')

def mifuncion2(arg = 'Chanchito'):
    print(arg)

# mifuncion2('Batman')
# mifuncion2()

def MiFuncionLista(Lista):
    for el in Lista:
        print(el)

# Lista = [1, 2, 3, 4, 5]
# MiFuncionLista(Lista)

def ConcatenaNombres(Lista):
    i = ''
    for el in Lista:
        i = i + ' ' + el
    return i

# nombres = ConcatenaNombres(['Chanchito', 'Feliz'])
# print(nombres)

def recursion(i):
    if i < 1:
        return i
    print(i)
    recursion(i - 1)

recursion(5)