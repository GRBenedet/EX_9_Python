#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

f = str(input('digite uma frase: ')).strip().upper()
r = ''
for c in range (len(f) , 0 , -1):
    r += f[c - 1]


if r == f:
    print('A frase {} {} {} é um palídromo'.format('\033[34m' , f , '\033[37m'))


else:
    print('A frase {} {} {} não é um palídromo'.format('\033[34m' , f , '\033[37m'))


