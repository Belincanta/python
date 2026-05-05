# lista dentro de outra lista
pessoas = list()
pessoas.append("Alessandro")
pessoas.append(29)
galera = list()
galera.append(pessoas[:])
pessoas[0] = "Hellen"
pessoas[1] = 28
galera.append(pessoas[:])
print(galera)
