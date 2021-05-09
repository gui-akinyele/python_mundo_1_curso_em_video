# Operadores Aritméticos

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da Divisão ou Módulo

#Ordem de Precedência

# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +,-

#5 + 2 =
#5 - 2==
#5 * 2==
#5 / 2==
# ** 2==
# // 2==
#5 % 2==

#5 + 2 * 3 == 11
#3 * 5 + 4 ** 2 == 31
#3 * ( 5 + 4 ) ** 2 == 243


#print(5+3*2)

#print(5**2)

#print(19//2)

#print(19/2)

##print(365**522)

#print(18%2)

#print (122%3)

#print(4**3)

#print(pow(4,3))

#Cálculo de Raiz

#print(81**(1/2))

#print(25**(1/2))

#print(127**(1/3))

#nome = str(input('Qual seu nome? '))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input(' Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}, \n o produto é {}, \n e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))







