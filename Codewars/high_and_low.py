# Programa de calculo del mayor y menor numero de una lista de numeros de texto

###########################
# Definición de funciones #
###########################

def high_and_low(numbers):
    # Definición de variables
    # Variables integer
    num = 0
    i = 0
    low = 0
    high = 0

    # Variables string
    numero = ''
    numbers = numbers + 'X'
    
    # Inicio del proceso
    while numbers[i] != 'X':
     
        while numbers[i] == ' ':
            i +=1
            
        while numbers[i] == '-' or (numbers[i]>='0' and numbers[i]<='9'):
            numero = numero + numbers[i]
            i += 1
            
        num = int(numero)
        if num < low:
            low = num
        elif num > high:
            high = num
        numero = ''
        num = 0

    print('El mas bajo es: ', low)
    print('El mas alto es: ', high)

# Fin función hig_and_low

#################################
# Bloque principal del programa #
#################################

high_and_low('3 5 7 -2 4 8 -7 12 6 134 -1544 9')
