a = [2, 5, 8]
# b = a # neste formato vai alterar ambas as listas, pois cria um ligação entre elas, quando são igualadas.
b = a[:] # neste formato só irá alterar a lista b, pois é como se eu copiasse a lista A
b[2] = 9 
print(f"Lista A: {a}")
print(f"Lista B: {b}")
