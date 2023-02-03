# Burbuja4.py
#
# Algoritmo Burbuja Ver 4.0
# Programa de ordenación de numeros introducidos mediante una lista de Python de forma aleatoria con funcion swap y toma de tiempo

# Importar librerias accesorias
import random
import datetime

#Definición de funciones
def Swap(a, b): # Función que intercambia los valores de una lista
    Var_Lista[i] = b
    Var_Lista[i + 1] = a
    return

#Definición de variables
Num = 0         # Cantidad de números aleatorios a generar
Var_Lista = []  # Variable que contendrá la lista de números a ordenar
Cambio = True   # Variable de control para saber si se produce un cambio
i = 0           # Variable de control del bucle For

Num = int(input('Burbuja 4 ¿Cuantos numeros aleatorios quieres?.- '))

for i in range(Num):
   Var_Lista.append(random.randint(1, Num)) 

# Var_Lista = [9, 1, 7, 8, 4, 5, 6]
# print(Var_Lista)
# print(range(len(Var_Lista)))
hora_inicio = datetime.datetime.now()
while Cambio:
    Cambio = False
    for i in range(len(Var_Lista) - 1):
        if Var_Lista[i] > Var_Lista[i + 1]:
            Swap(Var_Lista[i], Var_Lista[i + 1])
            Cambio = True

hora_fin = datetime.datetime.now()
tiempo_total = hora_fin - hora_inicio
# print(Var_Lista)
print(tiempo_total)