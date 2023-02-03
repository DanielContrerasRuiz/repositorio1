#if 5 > 3: # esto es para recordar que al
#    print('5 es mayor a 3')

"""palabra = 'hola mundo'
oracion = "hola mundo comillas dobles"

var_entero = 20
var_float =  20.2
var_complejo = 7j
print (palabra)
print (oracion)
print (var_entero)

print (palabra, oracion, var_entero, var_float, var_complejo)


VarLista = [1, 2, 3, 'Ana', 'Javier', 'Lucas']

#print (VarLista)
#print (VarLista[3])
#VarLista2 = VarLista.copy()
#VarLista.append('Magda')
print (VarLista)
print (VarLista2)
VarLista.reverse()
print (VarLista)
print (VarLista.count('Ana'))
#VarLista.clear()"""

Tupla = ('hola', 4, 'somos', 'tupla')
#print(Tupla.count('somos'))
#print(Tupla.index('somos'))
#print(Tupla[0])
ListaDeTupla = list(Tupla)
ListaDeTupla.append('chanchito')
#print(ListaDeTupla)

rango = range(6)
#print (rango)

Diccio = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}
print(Diccio)
print(Diccio['nombre'])
#print(Diccio['raza'])
#print(Diccio.get('raza'))
Diccio['nombre'] = 'Fluffy'
print(Diccio['nombre'])
print(Diccio)
print(len(Diccio))
Diccio['ronronea'] ='Si'
print(Diccio)
Diccio.pop('ronronea')
print(Diccio)
Diccio.popitem()
print(Diccio)


