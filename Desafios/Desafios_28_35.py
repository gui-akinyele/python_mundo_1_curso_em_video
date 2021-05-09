""" Exercício 28: 
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça 
para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá 
escrever na tela se o usuário venceu ou perdeu.
 """
""" from random import randint
from time import sleep
computador = randint(0, 5) #Faz o sorteio do número
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar!!!')
print('-=-'*20)
jogador = int(input('Em que número pensei??? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você ACERTOU!')
else:
    print(f'Você ERROU! Pensei em {computador} e você em {jogador}') """

    #Exercicio 29
''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.  

velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
  print(f'Você ultrapassou o limite! MULTA de R$ {(velocidade - 80)*7} ')
print('Tenha um bom dia, dirija com cuidado') '''

  #Exercicio 30

''' Crie um programa que leia um numero inteiro e mostre na tela se ele é IMPAR ou PAR. '''

''' num = int(input('Digite um número para verificar se ele é Ímpar ou Par: '))

if num % 2 == 0:
  print('O número é PAR')
else:
  print('O número é IMPAR') '''

  #Exercicio 31
#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.

''' km = int(input('Qual a distância da sua viagem? '))
if km <= 200:
  print(f'Sua viagem fica no valor de R$ {km * 0.5}')
if km > 200:
  print(f'Sua viagem fica no valor de R$ {km * 0.45}') '''

 #Exercicio 32
#Faça um programa que leia o ano qualquer e mostre se ele é bissexto.

''' from datetime import date
ano = int(input('Digite o ano que deseja analisar ou zero para o Ano Atual: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano {ano} é bissexto!')
else:
  print(f'O ano {ano} não é bissexto') '''

  
  #Exercicio 32
#Faça um programa que leia três números e mostre qual é o maior e o menor.

""" num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

# quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
  menor = num2
if num3 < num1 and num3 < num2:
  menor = num3


# quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
  maior = num2
if num3 > num1 and num3 > num2:
  maior = num3

print(f'Menor valor é {menor}')
print(f'Menor valor é {maior}') """


#Exercicio 34
""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. """
""" salario = float(input('Qual o valor do seu salário: '))

if salario > 1250:
    print(f'Seu novo salário é de R$ {(salario * 0.1) + salario:.2f}')
else:
    print(f'Seu novo salário é de R$ {(salario * 0.15) + salario:.2f}') """


#Exercicio 35
""" Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. """
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO')
else:
    print('Os segmentos acima NÃO FORMAM UM TRÂNGULO!')

