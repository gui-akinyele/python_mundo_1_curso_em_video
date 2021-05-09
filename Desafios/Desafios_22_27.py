"""  Exercício 22: 
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome. 

nome = str(input('Digite seu nome: ')).strip()
espaco = (nome.count(' '))
primeiro = nome.find(' ')
print('Analisando seu nome...')
print(f'Seu nome em maiuscúlas é ... {nome.upper()}')
print(f'Seu nome em minuscúlas é ... {nome.lower()}')
print(f'O total de letra no nome é ... {len(nome) - espaco}')
print(f'Seu primeiro nome tem ... {primeiro} letras') """


""" Exercício 23: 
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um numero de 0 a 9999: '))
und = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil  = num // 1000 % 10
print(f'Analisando o número {num} ....')
print(f'Unidade: {und}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}') """


""" Exercício 24: 
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”. 

cidade = str(input('Qual a cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')  """


""" Exercício 25:
 Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. 

nome = str(input('Qual seu nome completo? ')).strip()
print(f'Seu nome tem Silva?', 'SILVA' in nome.upper())"""

""" Exercício 26: 
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. 

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes na sua frase.')
print(f'A primeira letra A aparece na posição {frase.find("A")+1}')
print(f'A primeira letra A aparece na posição {frase.rfind("A")+1}')"""

""" Exercício 27: 
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente. 

nome = str(input('Digite seu nome completo: ')).strip()
nome_aux = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome_aux[0]}')
print(f'Seu último nome é {nome_aux[len(nome_aux)-1]}')"""
