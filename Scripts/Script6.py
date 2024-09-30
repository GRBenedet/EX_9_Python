#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('defina um valor: '))

raz = int(input('defina a razão: '))

print('Inicio da progressão: ')
for c in range(0, 10):
    print(num + c * raz)

print('FIM')