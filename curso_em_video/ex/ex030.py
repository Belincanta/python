galera = []
dado = []
for c in range(0, 3):
    galera.append(input("Nome: "))
    galera.append(int(input("Idade: ")))
    dado.append(galera[:])
    galera.clear()
print(dado)