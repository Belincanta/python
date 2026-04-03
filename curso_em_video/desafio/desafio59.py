# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo número: "))
sleep(1)
resultado = 0
opcao = 0
while not opcao == 5:
    print("="*30)
    print("Olha o que podemos fazer com estes números")
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    opcao = int(input(">>>>> Qual opção escolher? "))
    print("="*30)
    print("Calculando....")
    sleep(1)
    if opcao == 1:
        resultado = v1 + v2
        print(f"A soma entre os números é {resultado}")
    elif opcao == 2:
        resultado = v1 * v2
        print(f"A multiplicação entre os números é {resultado}")
    elif opcao == 3:
        if v1 > v2:
            resultado = v1
            print(f"O número maior entre os números é o {resultado}")
        else:
            resultado = v2
            print(f"O número menor entre eles é o {resultado}")
    elif opcao == 4:
        v1 = int(input("Primeiro valor: "))
        v2 = int(input("Segundo número: "))
    else:
        print("Ops! Opção inválida, tente novamente")
    sleep(2)
print("FIM DO PROGRAMA!")
