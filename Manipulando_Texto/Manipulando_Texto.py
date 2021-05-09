# #! FATIAMENTO: 
#TODO: funcionalidade que permiti selecionar caracteres da string
#! Exemplo:
#*  Curso em Vídeo Python - sintaxe -> frase[1:4] - irá selecionar o caracter na posição 1 e na posição 4
#* a impressão será -> "u" e "o".
#* frase[0:6:2] - seleção da posição 0 a 6 pulando de 2 em 2 posições.
#* frase[:5] - seleção do zero até 4, ou seja início até o anterior ao último.
#* frase[15:] - seleção do inicio setado "15" até o final.
#* frase[9::3] - seleção do nono caracter até o último, pulando de 3 em 3.

#! ANÁLISE
#! Contador de CARACTERES:
#* len(frase) 

#! CONTADOR DE "LETRAS/ELEMENTOS" DA STRING
#* frase.count('o') - irá contar quantas vezes o 'o' aparece na frase.
#* frase.count('o,0,13') - irá contar quantas vezes o 'o' aparece na frase de 0 até posição 12.

#! "BUSCADOR DE CARACTERES"
#* permite encontrar o valor da string setado - > frase.find('deo') - irá indicar em que posição inicia 
#* o valor 'deo'.
#* frase.find('Android') -> retorna -1, pois não existe o valor setado.

#! VERIFICA EXISTENCIA DO TERMO
#* 'Curso' in frase -> verifica se o termo 'Curso' existe em frase e retorna, True ou False.

#! TRANSFORMAÇÃO 
#* mémoto REPLACE - troca o termo.
#* frase.replace('Python','Android')
#* MAISCULAS -> frase.upper()
#* minusculas -> frase.lower()
#* Somente a primeiro caractere da frase em maiscula -> frase.capitalize()
#* Maiscula Todos Os Primeiros Caracteres Das Palavras -> frase.title()
#* Remove espaços inutilizados -> frase.strip()
#* Remove os espaços a direita -> frase.rstrip()
#* Remove os espaços a esquerda -> frase.lstrip()

#! DIVISÂO
#* Transforma uma cadeia de caracteres (frase) em uma lista de palavras -> frase.split()

#! JUNÇÂO
#* Reuni uma cadeia de caracteres -> '-'.join(frase)
#* exemplo Curso em vídeo - Curso-em-vídeo

#Todo - PRÁTICA

frase = 'Curso em video Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('video'))
print(frase.split())
dividido = frase.split()
print(dividido[2][3])


