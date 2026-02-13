# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Whats your name? ')
n = nome.split()
print('Nice to meet you!')
print(f'Your first name is {n[0]}')
print(f'Your last name is {n[-1]}')

#split separa a string