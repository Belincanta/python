# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input('Digite o preço deste produto: '))
d = p*0.05
print(f'Com o desconto aplicado, o novo valor fica {p-d:.2f} reais.')