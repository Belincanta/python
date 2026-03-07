#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 26 até 30: Sobrepeso
#– 31 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
imc = peso / (altura * altura)
print(f"Seu IMC é de {imc:.1f}")
if imc < 18.5:
    print("Você está com peso ABAIXO do normal!")
elif imc <= 25:
    print("Você está com peso NORMAL!")
elif imc <= 30:
    print("Você está SOBREPRESO! Atenção!")
elif imc <= 40:
    print("Você está com OBESIDADE! Atenção!")
else:
    print("Você está com OBESIDADE MÓRBIDA! Cuidado!")

