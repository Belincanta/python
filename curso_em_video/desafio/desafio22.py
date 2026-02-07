# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip() #strip para tirar os espaços 
print(f'Seu nome com letras maiúsculas é {nome.upper()}')
print(f'Seu nome com letras minúsculas é {nome.lower()}')
print(f'Seu nome tem o total de {len(nome) - nome.count(' ')} letras') # len para contar quantas letras menos os espaços
print(f'Seu primeiro nome tem {nome.find(' ')} letras') # find encontra o primeiro espaço
