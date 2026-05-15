# dicionário
estado = dict()
brasil = list()
for c in range(0,3):
    estado["uf"] = input("Digite a Unidade federativa: ")
    estado["sigla"] = input("Digite a sigla: ")
    brasil.append(estado.copy())
for e in brasil: #repetição dentro da lista
    for v in e.values(): #repetição dentro do dicionário
        print(v, end = " ")

