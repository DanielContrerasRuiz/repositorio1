# Burbuja6.py
#
# Algoritmo Burbuja Ver 6.0
# programa de ordenación de numeros introducidos mediante una lista de Python de forma 
# aleatoria con función swap, control de fin de ordenación y decremento del ultimo elemnto para no realizarlo

# Importar librerias accesorias
import random       # Se utilizara la función randint() de esta libreria para el calculo de numero aleatorio enteros de un intervalo
import datetime     # Se utilizarán la funcione datetime.now() para extraer el tiempo en el instante de uso

#Definición de funciones
def Swap(a, b):     # Función que intercambia los valores de dos elemento de una lista
    Var_Lista[i] = b
    Var_Lista[i + 1] = a
    return

#Definición de variables
Num = 0             # Cantidad de números aleatorios a generar
Var_Lista = []      # Variable que contendrá la lista de números a ordenar
Cambio = True       # Variable de control para saber si se produce un cambio
i = 0               # Variable de control del bucle For
j = 0               # Variable de control del bucle For
LongLista = 0       # Variable para almacenar la longitud de la lista = Num

Num = int(input('Burbuja 6 ¿Cuantos numeros aleatorios quieres?.- '))

for i in range(Num):
   Var_Lista.append(random.randint(1, Num)) 

LongLista = len(Var_Lista)
# print(Var_Lista)
# print(range(len(Var_Lista)))
hora_inicio = datetime.datetime.now()
for j in range(LongLista - 1):
    for i in range(LongLista - 1):
        if Var_Lista[i] > Var_Lista[i + 1]:
            Swap(Var_Lista[i], Var_Lista[i + 1])
            
    LongLista = LongLista - 1

hora_fin = datetime.datetime.now()
tiempo_total = hora_fin - hora_inicio
# print(Var_Lista)
print(tiempo_total)