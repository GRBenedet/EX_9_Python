#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
menor = 0
maior = 0

for c in range(1 , 8):
    data = int(input('digite o ano de nascimento da {}° pessoa: '.format(c)))
    
    if date.today().year - data < 21:
        menor += 1

    else:
        maior += 1

print('no total são {} menores de idade e {} maiores de idade.'.format(menor ,  maior))