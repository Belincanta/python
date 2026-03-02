#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual o valor da casa: "))
salario_comprador = float(input("Qual o salário do comprador: "))
prazo = int(input("Qual é o prazo para pagamento (anos): "))
prestacao = valor_casa / (prazo * 12)

print("="*20)
print("Simulação de aquisição")
print("="*20)

if prestacao <= salario_comprador*0.30:
    print(f"Você foi APROVADO com a sua parcela de R${prestacao:.2f}!")
else:
    print(f"Você foi REPROVADO, sua parcela de R${prestacao:.2f} está comprometendo 30% da sua renda de R${salario_comprador:.2f}!")