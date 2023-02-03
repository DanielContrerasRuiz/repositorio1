# Burbuja2.py
#
# Algoritmo Burbuja Ver 2.0
# programa de ordenación de numeros introducidos mediante una lista de Python

Var_Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Cambio = True
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