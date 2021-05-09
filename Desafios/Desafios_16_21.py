""" Exercício 16: 
Crie um programa que leia um número Real qualquer pelo teclado e mostre 
na tela a sua porção Inteira. """
""" import math

num = float(input('Digite um número: '))

#print(f'O número {num} tem a parte inteira {num:.0f}')
print(f'O número {num} tem a parte inteira {math.trunc(num)}') """

""" Exercício 17: 
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. """
""" import math

cateto_opo = float(input('Digite o valor do cateto oposto: '))
cateto_adj = float(input('Digite o valor do catero adjacente: '))
#hipo = (cateto_opo ** 2 + cateto_adj ** 2) ** (1/2)
hipo = math.hypot(cateto_opo, cateto_adj)

print(f'O valor da hipotenusa é {hipo:.2f}') """

""" Exercício 18: 
Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
do seno, cosseno e tangente desse ângulo. """

""" import math

angulo = float(input('Digite o valor do ângulo: '))

print(f'O valor do seno é {math.sin(math.radians(angulo)):.2f}, o valor do cosseno é {math.cos(math.radians(angulo)):.2f}, e o valor da tangente é {math.tan(math.radians(angulo)):.2f}') """


""" Exercício 19: 
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido. """

""" from random import choice

pri = str(input('Primeiro Aluno: '))
seg = str(input('Segundo Aluno: '))
ter = str(input('Terceiro Aluno: '))
quar = str(input('Quarto Aluno: '))
alunos = [pri, seg, ter, quar]
escolhido = choice(alunos)
print(f'O Aluno escolhido foi {escolhido}') """


""" Exercício 20: 
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. """

""" from random import shuffle

pri = str(input('Primeiro Aluno: '))
seg = str(input('Segundo Aluno: '))
ter = str(input('Terceiro Aluno: '))
quar = str(input('Quarto Aluno: '))
alunos = [pri, seg, ter, quar]
shuffle(alunos)
print('A ordem da apresentação será: ')
print(alunos) """


""" Exercício 21: 
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. """

""" import pygame 
    pygame.init()
pygame.mixer.music.load('musi01.mp3')
pygame.mixer.music.play()
pygame.event.wait() """

from pygame import mixer
mixer.init()
mixer.music.load('musi01.mp3')
mixer.music.play()
input('CURTE O SOM MOZAAOO!')