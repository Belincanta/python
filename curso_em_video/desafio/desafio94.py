# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = input("Digite o nome: ")    
    while True:
        pessoa["sexo"] = input("Digite o sexo [M/F]: ").strip().upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Digite apenas M ou F")    
    pessoa["idade"] = int(input("Digite a idade: "))
    soma =+ pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = input("Quer continuar? [S/N]: ").strip().upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        break
print("=-"*15)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A média de idade é {media:.1f} anos")
print(f"C) Lista de mulheres: ",end="")
for p in galera:
    if p["sexo"] in "F":
        print(f"{p["nome"]}", end="")
print()
print(f"D) Lista de pessoas com idade acima da média ")
for p in galera:
    if p["idade"] >= media:
        print("  ", end="")
        for k, v in p.items():
            print(f"{k} = {v} ", end="")
        print()
print("<<< PROGRAMA ENCERRADO >>>")