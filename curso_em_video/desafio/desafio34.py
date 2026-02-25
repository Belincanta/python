# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário R$ "))
if salario > 1250:
    print(f"Para um salário de R$ {salario:.2f}, após o aumento será R$ {(salario*0.10) + salario:.2f}")
else:
    print(f"Para um salário de R$ {salario:.2f}, após o aumento será R$ {(salario*0.15) + salario:.2f}")
