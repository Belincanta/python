#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input("Digite um número para calcular a tabuada: "))
for tab in range(1, 11):
    print(f"{num} X {tab} = {num*tab}")