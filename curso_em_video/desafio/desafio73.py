# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ("Palmeiras", "Flamengo", "São Paulo", "Fluminense", "Bahia", 
         "Athetico-PR", "Coritiba", "Atlético-MG", "Bragantino", "Vitória",
         "Botafogo", "Grêmio", "Vasco da Gama", "Internacional", "Santos", 
         "Corinthians","Cruzeiro", "Remo", "Chapecoense", "Mirassol")

print("=-"*20, "BRASILEIRÃO 2026", "=-"*20)
print(f"Os 5 primeiros colocados são {times[0:5]}")
print("=-"*49)
print(f"Os times na zona de rebaixamento são {times[-4:]}")
print("=-"*49)
print(f"Os times em ordem alfabética são {sorted(times)}")
print("=-"*49)
print(f"A Chapecoense está na posição {times.index('Chapecoense')+1}")
print("=-"*49)
    