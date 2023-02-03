# Burbuja1.py
#
# Algoritmo Burbuja Ver 1.0
# programa de ordenación de numeros introducidos mediante una lista de Python

Var_Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Cambio = True
print(Var_Lista)
for veces in range(len(Var_Lista)-1):
    Cambio = False
    for i in range(len(Var_Lista) - 1):
        if Var_Lista[i] > Var_Lista[i + 1]:
            Temp = Var_Lista[i]
            Var_Lista[i] = Var_Lista[i + 1]
            Var_Lista[i + 1] = Temp
            Cambio = True
    print(Var_Lista)
