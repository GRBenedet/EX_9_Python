#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

contM = 0
media = 0
maior = 0

for c in range(1 , 5):
    name = str(input('qual o nome da {}° pessoa: '.format(c))).capitalize()
    idade = int(input('qual a idade da {}° pessoa: '.format(c)))
    sex = str(input('qual o genero da {}° pessoa (homem) ou (mulher): '.format(c))).strip().upper()

    if idade > maior and sex in 'HOMEM':
       maior = idade
       oldH = name

    if idade < 20 and sex in 'MULHER':
        contM += 1

    media += idade

print('O homem mais velho do grupo é {}\nTem {} mulhers com menos de 20 anos.\n{:.0f} É a media de idade do grupo.'.format(oldH , contM , media / 4))