# Burbuja3.py
#
# Algoritmo Burbuja Ver 3.0
# programa de ordenación de numeros introducidos mediante una lista de Python de forma aleatoria

# Importar librerias accesorias
import random

#Definición de variables

Num = 0         # Cantidad de números aleatorios a generar
Var_Lista = []  # Variable que contendra la lista de números a ordenar
Cambio = True   # Variable de control para saber si se produce un cambio
i = 0           # Variable de control del bucle for

Num = int(input('¿Cuantos numeros aleatorios quieres?.- '))

for i in range(Num):
    Var_Lista.append(random.randint(1, Num)) 

# Var_Lista = [9, 1, 2, 3, 4, 5, 6, 7 ,8]
print(Var_Lista)
print(range(len(Var_Lista)))
while Cambio:
    Cambio = False
    for i in range(len(Var_Lista) - 1):
        if Var_Lista[i] > Var_Lista[i + 1]:
            Temp = Var_Lista[i]
            Var_Lista[i] = Var_Lista[i + 1]
            Var_Lista[i + 1] = Temp
            Cambio = True

print(Var_Lista)