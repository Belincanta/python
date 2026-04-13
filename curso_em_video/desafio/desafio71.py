#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print("="*40)
print("{:^40}". format(" BANCO ALE"))
print("="*40)
valor = int(input("Qual o valor deseja sacar? R$ "))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula: 
        total -= cedula
        totalcedula += 1
    else: #quando o valor que sobrar é menor que 50.00
        if totalcedula > 0:
            print(f"Para este valor será necessário {totalcedula} notas de R$ {cedula}.")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print("="*40)
print("Obrigado e volte sempre")