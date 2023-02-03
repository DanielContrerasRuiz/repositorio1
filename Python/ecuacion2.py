def raiz(aa, bb, cc):
    return ((bb**2)-(4*aa*cc))

a = 0
b = 0
c = 0
a = int(input("Introduce A "))
b = int(input("Introduce B "))
c = int(input("Introduce C "))
if raiz(a, b, c) >= 0 and a != 0:
    r1 = ((-b)+raiz(a, b, c)**(1/2))/(a*2)
    r2 = ((-b)-raiz(a, b, c)**(1/2))/(a*2)
    print(r1)
    print(r2)
else:
    if raiz(a, b, c) < 0:
        print('La ecuación no tiene solución porque la raiz es negativa')
    if a == 0:
        print('La ecuación no tiene solución porque el termino A es igual a 0')