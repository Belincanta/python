#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import uteis #importando as funções

preco = float(input("Digite o preço R$ "))
print(f"O dobro é R$ {uteis.dobro(preco):.2f}")
print(f"A metade é R$ {uteis.metade(preco):.2f}")
print(f"Aumentando o valor em 10% fica R$ {uteis.aumentar(preco):.2f}")
print(f"Diminuindo o valor em 10% fica R$ {uteis.diminuir(preco):.2f}")