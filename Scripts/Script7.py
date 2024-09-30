#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('defina o numero: '))
t = 0

for c in range(1 , num + 1):

    if num % c == 0 :
        print('\033[33m' , end=' ')
        t += 1
        if t > 2:
            s = 'não é'
            
        else:
            s = 'é'

    else:
        print('\033[31m' , end=' ')
    print( c , end=' ')

print('\033[37m', '\nO numero {}, foi divido {} vezes, portanto {} primo.'.format(num , t , s))
