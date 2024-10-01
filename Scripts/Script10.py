#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1 , 6):
    peso = float(input('digite o peso da {}° pessoa: '.format(c)))
    if peso > maior:
        maior = peso
        if c == 1:
            menor = peso
    elif peso < menor:
        menor = peso
print('o menor peso foi {}{:.2f}kg {} e o maior peso foi {}{:.2f}kg{}'.format('\033[32m' , menor  , '\033[37m', '\033[32m', maior , '\033[37m'))