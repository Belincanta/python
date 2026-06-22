# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import uteis

preco = float(input("Digite o valor R$ "))
print(f"O dobro de {uteis.moeda(preco)} é {uteis.moeda(uteis.dobro(preco))}")
print(f"A metade de {uteis.moeda(preco)} é {uteis.moeda(uteis.metade(preco))}")
print(f"Aumentando o valor {uteis.moeda(preco)} em 10% fica {uteis.moeda(uteis.aumentar(preco, 10))}")
print(f"Diminuindo o valor {uteis.moeda(preco)} em 10% fica {uteis.moeda(uteis.diminuir(preco, 10))}")
