# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contador = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
            "Seis", "Sete", "Oito", "Nove", "Dez",
            "Onze", "Doze", "Treze", "Quatorze", "Quinze",
            "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if numero >= 0 and numero <= 20:
        print("=-"*12)
        print(f"Você digitou o número {contador[numero]}") #vai trazer conforme a posição do número digitado.
        print("=-"*12)
    else:
        print("Número não está catalogado!", end=" ")
    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer digitar outro número? S/N: " ).strip().upper()[0]
    if opcao == "N":
        break
print("Acabou a contagem")
    
