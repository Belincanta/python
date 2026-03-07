#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
print("="*10, "Lojas Belincanta", "="*10)
valor = float(input("Qual o valor das compras? R$ "))
print("[0] à vista dinheiro/cheque: 10% de desconto")
print("[1] à vista no cartão: 5% de desconto")
print("[2] em até 2x no cartão: preço formal")
print("[3] 3x ou mais no cartão: 20% de juros")
opcao = int(input("Escolha uma das opções acima: "))
if opcao == 0:
    total = valor - (valor * 0.10)
elif opcao == 1:
    total = valor - (valor * 0.05)    
elif opcao == 2:
    total = valor
    parcela = valor / 2
    print(f"A sua compra de R${valor:.2f} será parcelada em 2x de R${parcela:.2f}!")
elif opcao == 3:
    total = valor + (valor * 0.20)
    parcela = int(input("Quantas parcelas?"))
    juros = (total / parcela)
    print(f"A sua compra de R${valor:.2f}, será parcelada em {parcela}x de R${juros:.2f} com juros!")
else:
    total = valor
    print("Opção inválida de pagamento, tente novamente.")
print(f"A sua compra de R${valor:.2f}, será de R${total:.2f} no final!")        