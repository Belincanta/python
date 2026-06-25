# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

#solução: criar um novo parâmetro nas funções chamado 'formatado' e chamar aqui quando precisar retornar o formato moeda

import uteis

preco = float(input("Digite o valor R$ "))
uteis.resumo(preco)
