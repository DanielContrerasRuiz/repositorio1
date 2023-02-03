import random
import datetime


def quicksort_iterativo(lista: [int]) -> [int]:
    ''' Una implementación del mismo algoritmo que conoces y amas, pero sin
    utilizar recursión, solo bucles y una pila '''
    ordenada = lista[:]

    pila = [(0, len(lista) - 1)]
   
    # Mientras la pila esté vacía habrá algún segmento que ordenar
    while len(pila) > 0:
        # sacar el tope de la pila, que es una tupla cuyos índices indican una
        # porción de la lista que aun no está ordenada
        a, b = pila.pop()
        # print(pila)
        # aquí hacemos la magia usual de escoger un pivote y ubicarlo en su
        # posición correspondiente de este segmento
        pivote = ordenada[b]
        i = a

        for j in range(a, b):
            if ordenada[j] < pivote:
                ordenada[i], ordenada[j] = ordenada[j], ordenada[i]
                i += 1

        ordenada[i], ordenada[b] = ordenada[b], ordenada[i]

        # el equivalente a la llamada recursiva es meter un elemento a la pila,
        # en este caso es la parte izquierda por ordenar, antes del pivote
        if i > a + 1:
            pila.append(
                (a, i - 1)
            )

        # la parte derecha sin ordenar, después del pivote
        if i < b - 1:
            pila.append(
                (i + 1, b)
            )

    # si (y cuando) llegamos hasta acá quiere decir que la pila ya está vacía y
    # por consiguiente todos los segmentos están ordenados y con ellos la lista
    # entera
    return ordenada


def main():
    # numeros = list(range(1000))
    # d = [random.choice(numeros) for _ in range(20)]
    d = []
    Num = int(input('Burbuja 5 ¿Cuantos numeros aleatorios quieres?.- '))

    for i in range(Num):
        d.append(random.randint(1, Num)) 

    print(d)
    hora_inicio = datetime.datetime.now()
    print(quicksort_iterativo(d))
    hora_fin = datetime.datetime.now()
    tiempo_total = hora_fin - hora_inicio
    print(tiempo_total)


if __name__ == "__main__":
    main()