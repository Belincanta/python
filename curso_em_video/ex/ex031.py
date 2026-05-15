# começo com dicionários

pessoas = {"Nome": "Alessandro", "Idade": 29, "Sexo": "M"}
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
pessoas["peso"] = 98.5 # para adicionar uma keys e seu values
for k, v in pessoas.items():
    print(f"{k} = {v}")
