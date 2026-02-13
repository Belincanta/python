# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').upper().strip()
print(f'A letra "A" aparece {frase.count('A')} vezes na frase')
print(f'A primeira letra "A" aparece na posição {frase.find('A')+1}')
print(f'a última letra "A" aparece na posição {frase.rfind('A')+1}')

#upper é para deixar tudo em maiusculo
#strip é para tirar os espaços
#count é para contar
#find é para localizar
#rfind é para localizar da direira para esquerda