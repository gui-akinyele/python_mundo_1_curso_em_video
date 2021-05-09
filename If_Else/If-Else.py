""" #Algoritmo que identifique se o carro é novo ou velho.

tempo = int(input('Quantos anos tem seu carro: '))

if tempo <= 3 :
    print('Seu carro está novo!')
else: 
    print('Seu carro está ficando velho!')
print('--Fim--') """

""" nome = str(input('Qual seu nome? ')).upper()
if nome == 'GUILHERME':
    print('Bem-vindo de volta!')
else:
    print('Você não é o Guilherme!')
print(f'Bom dia, {nome}') """

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi {media:.2f}')
if media >= 7.0:
    print('Sua média foi boa, PARABÉNS!')
else:
    print('Sua média foi baixa, ESTUDE MAIS!!!')