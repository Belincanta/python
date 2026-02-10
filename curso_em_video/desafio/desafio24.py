# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite a sua cidade: ').strip()
print(cidade[0:5].upper() == 'SANTO')

#strip tiro os espaços
#cidade [0:5] pois a palavra santo, começa em 0 e termina em 4, porém para pegar o 4, uso o 5
#upper transfor esta parte em maiuscula
#== é igual