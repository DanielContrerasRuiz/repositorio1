def array_diff(lista1, lista2):

     puntero = 0
     while puntero != len(lista1):
        esta = False
        for j in lista2:
            if j == lista1[puntero]:
                esta = True
        if esta:
            lista1.pop(puntero)
            puntero -=1
        puntero +=1

     print(lista1)   



#lista1 = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8]
#lista2 = [8]

array_diff([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8], [8])



