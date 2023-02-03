# Burbuja puro.py
#
# Algoritmo Burbuja puro
# programa de ordenación de numeros introducidos mediante una lista de Python

import random
import datetime

Num = int(input('Burbuja Puro ¿Cuantos numeros aleatorios quieres?.- '))
Var_Lista = []

for i in range(Num):
   Var_Lista.append(random.randint(1, Num)) 

# print(Var_Lista)
Hora_Inicio = datetime.datetime.now()
for veces in range(len(Var_Lista)-1):
    for i in range(len(Var_Lista) - 1):
        if Var_Lista[i] > Var_Lista[i + 1]:
            Temp = Var_Lista[i]
            Var_Lista[i] = Var_Lista[i + 1]
            Var_Lista[i + 1] = Temp
Hora_Fin = datetime.datetime.now()
Tiempo_total = Hora_Fin - Hora_Inicio
# print(Var_Lista)
print(Tiempo_total)
