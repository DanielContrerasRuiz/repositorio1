'''def high_and_low(numbers):
    low = int(numbers[0])
    high = int(numbers[0])
    numero = 0
    signo = ''
    for i in range(len(numbers)):
        signo = ''
        # print(i)
        # print(numero[1])
        if numbers[i] != ' ':
            if numbers[i] == '-':
                signo = numbers[i]
                i += 1
            
            numero = int(signo + numbers[i])
            # print(signo)
            # print(signo+numbers[i])
            print(numero)
            if numero < low:
                low = numero
            elif numero > high:
                high = numero
    
    print(low, ' ', high)'''

def high_and_low(numbers):
    # Definición variables integer
    low = 0
    high = 0
    num = 0
    i = 0
    # Definición variables string
    numstr = '' 
    
    # Se añade una marca de final a la cadena para control de fin
    numbers = numbers + 'X'
    while numbers[i] != 'X':
     
        espacio = numbers[i] == ' '
        numero = numbers[i] == '-' or (numbers[i]>='0' and numbers[i]<='9')
        
        while espacio:
            i +=1
            
        while numero:
            numstr = numstr + numbers[i]
            i += 1

        if not espacio and not numero:
            i +=1
        elif espacio or numero:
            num = int(numstr)
            if num < low:
                low = num
            elif num > high:
                high = num
        numstr = ''
        num = 0

    print('El mas bajo es: ', low)
    print('El mas alto es: ', high)


high_and_low('3 5 a 7 -2 4 8 -7')
