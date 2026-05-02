# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

pilha = []
expressao = input("Digite a expressão: ")
for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0: # se não estiver vazia, remove o último item
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")

# para cada parente aberto ideia é localizar o parênteses fechando para combinar o par, zerando então a pilha.


