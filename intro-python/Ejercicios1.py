# Ejercicio 1
# Multiplicar dos numeros sumando el primero tantas veces como sea el segundo
'''def multiplica(a, b):
    resultado = 0
    for n in range(b):
        resultado = resultado + a
    
    return(resultado)

a = 5
b = 8
print(multiplica(a, b))'''

# Ejercicio 2
# Ingresa nombre y apellido e imprimelo al reves
'''nombre =''
apellido = ''
nombre = input('Introduce nombre: ')
apellido = input('Introduce apellido: ')
todo = nombre + ' ' + apellido

# Variante 1
#for i in range(len(todo) - 1, -1, -1):
#    print(todo[i], end = "")

# Variante 2
#for i in reversed(range(len(todo))):
#    print(todo[i], end = '')

# Variante 3
print(todo[::-1])'''

# Ejercicio 3
# Encontrar el menor valor de una lista
'''lista = [1, 5, 3, 8, 2, 9, -24, -13]
menor = lista[0]
for i in lista:
    if i < menor:
        menor = i

print('Menor: ', menor)'''

# Ejercicio 4
# Escribir función que devuelva el volumen de una esfera por su radio
# 4/3 * Pi * r**3

'''def CalculaVolumen(r):
    volumen = (4/3 * 3.14159 * (radio**3))
    return(volumen)

radio = int(input('Introduce el radio de la esfera: '))
print('El volumen es: ', CalculaVolumen(radio))'''

# Ejercicio 5
# Funcion que indique si el usuario es mayor de edad

'''def esMayor(usuario):
    return(usuario.edad > 17)

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario1 = Usuario(15)
usuario2 = Usuario(21)

print(esMayor(usuario1), esMayor(usuario2))'''

# Ejercicio 6
# escribir funcion que indique si un numero es par o impar

'''def esPar(num):
    return num % 2 == 0

num = int(input('Introduce un numero: '))
print('El numero ', num, ' es par ', esPar(num))'''

# Ejercicio 7
# escribir funcion que indique cuantas vocales tiene una palabra

'''def contarVocales(palabra):
    vocales = 0
    for i in palabra:
        if i in ListaVocales:
            vocales += 1
    return vocales

ListaVocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
palabra = 'En un lugar de La Mancha'
print(contarVocales(palabra))'''

# Ejercicio 7
# escribir programa que reciba cantidad infinita de numeros hasta decir basta, finalmente que devuelva la suma de los números

'''Lista = []
valor = ''
resultado = 0
while valor != 'S' and valor != 's':
    valor = input('Introduzca valor o pulse S para salir: ')
    try:
        valor = int(valor)
        Lista.append(valor)
    except:
        if valor =='S' or valor == 's':
            print('Ha pulsado salir')
        else:
            print('Dato no válido')

for i in Lista:
    resultado += i

print(resultado)'''

# Ejercicio 8
# escribir funcion que reciba nombre y apellido y los agregue a un archivo

def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

nombre = input('Introduce el nombre: ')
apellido = input('Introduce el apellido: ')
agregaNombreAArchivo(nombre, apellido)