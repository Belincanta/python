# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

#solução: criar um novo parâmetro nas funções chamado 'formatado' e chamar aqui quando precisar retornar o formato moeda

import uteis

preco = float(input("Digite o valor R$ "))
print(f"O dobro de {uteis.moeda(preco)} é {uteis.dobro(preco, True)}")
print(f"A metade de {uteis.moeda(preco)} é {uteis.metade(preco, True)}")
print(f"Aumentando o valor {uteis.moeda(preco)} em 10% fica {uteis.aumentar(preco, 10, True)}")
print(f"Diminuindo o valor {uteis.moeda(preco)} em 10% fica {uteis.diminuir(preco, 10, True)}")
