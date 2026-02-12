# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = input('Qual é o seu nome? ').strip()
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')

#strip para tirar os espaços
#in nome para dizer se este texto está dentro da variável
#upper é para deixar tudo em maiusculo