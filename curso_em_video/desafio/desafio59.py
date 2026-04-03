# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo número: "))
opcao = int(input("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa"))
while not opcao == 5:
    v1 = int(input("Primeiro valor: "))
    v2 = int(input("Segundo número: "))
