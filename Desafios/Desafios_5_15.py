#a = input('Digite algo: ')
#print('O tipo primitivo desse valor é ', type(a))
#print('Só tem espaços? ', a.isspace())
#print('É um número? ' , a.isnumeric())
#print('É alfabético? ' , a.isalpha())
#print('É alfanumérico ? ', a.isalnum())
#print('Está em maiúsculas? ', a.isupper())
#print('Está em minúsculas? ', a.islower())
#print('Está capitalizada? ' , a.istitle())
'''
a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maúscula? {a.isupper()}')
print(f'Está em minúscula? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')


# ==== Desafio 5 ====

# Faça um programa que leia um número inteiro e mostre seu sucessor e seu antecessor.

x = int(input('Digite um valor: '))
suc = x+1
ant = x-1
print(f'O sucessor do valor é {x+1} e o antecessor é {x-1}!')

# ==== Desafio 6 ====

# Faça um programa que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada.

x = int(input('Digite um valor: '))
dob = x * 2
tri = x * 3
raiz = x ** 0.5

print(f'O dobro de {x} é {dob} O triplo de {x} é {tri} A raiz de {x} é {raiz:.2f}!')

# ==== Desafio 7 ====

# Faça um programa que leia duas notas, calcule sua media e mostre sua nota

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média do Aluno é {media:.2f}!')

# ==== Desafio 8 ====

# Faça um programa que converta Metros para Centímetros e Milimetros.

metro = float(input('Digite seu valor em METROS: '))
km = metro/1000
hm = metro/100
dam = metro/10
dm = metro*10
cent = metro*100
mili = metro*1000

print(f'A conversão de {metro:.2f} é: \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cent}cm \n{mili}mm ')

# ==== Desafio 9 ====

# Faça um programa que calcule a tabuada de um número

num = int(input('Digite um número para a tabuada: '))

print('-' * 12)
print(f'{num} x {1} =  {num*1}')
print(f'{num} x {2} =  {num*2}')
print(f'{num} x {3} =  {num*3}')
print(f'{num} x {4} =  {num*4}')
print(f'{num} x {5} =  {num*5}')
print(f'{num} x {6} =  {num*6}')
print(f'{num} x {7} =  {num*7}')
print(f'{num} x {8} =  {num*8}')
print(f'{num} x {9} =  {num*9}')
print(f'{num} x {10} = {num*10}')
print('-' * 12)


# ==== Desafio 10 ====

# Faça um programa que leia quanto dinheiro a pessoa tem na carteira e quantos dólares ela pode comprar. 
# CONSIDERE US$ 1.00 = R$ 3.27

reais = float(input('Quantos Reais você tem? '))
conver = reais / 3.27

print(f'Você pode comprar US$ {conver:.2f}')

# ==== Desafio 11 ====

"""Faça um programa que leia a largura e altura de uma parede,calcule sua área e a quantidade de tinta 
necessária para pinta-lá, sabendo que cada litro pinta 2m²"""
'''
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
tinta = int(2)
ar_parede = altura * largura
qtd_tinta = ar_parede / tinta

print(f'A area da sua parede é {ar_parede}m² e a quantidade de tinta necessário para pintar é de {qtd_tinta}l')
'''
# ==== Desafio 12 ====

#Faça um programa que leia um preço e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto R$: '))
novo_preco = preco - (preco*0.05)
print(f'O preço do produto com 5% de desconto é R$ {novo_preco:.2f}')


# ==== Desafio 13 ====

#Faça um programa que leia o salário de um funcionário e mostre seu novo salario com 15% de aumento


salario = float(input('Digite o salário do funcionário: R$ '))

aument = salario + (salario * 0.15)

print(f'O novo salário é: R$ {aument:.2f}')

# ==== Desafio 14 ====
# Escreva um programa que converta uma temperatura digitando em 
# graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em graus Celsius: '))
print(f'A temperatura em Fahrenheit é: {(celsius *1.8) +32 :.2f}ºF')

# ==== Desafio 15 ====
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
# carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos quilômetros você percorreu? '))
dias = int(input('Quantos dias você irá alugar o carro? '))

print(f'Você percorreu: {km} km')
print(f'Você utilizei por quantos: {dias}')
print(f'Você ira pagar R$: {(km * 0.15) + (dias * 60)}')
'''