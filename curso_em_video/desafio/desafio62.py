# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end = " > ")
        termo += razao
        cont += 1        
    print("PAUSE")
    mais = int(input("Quantos termos que você quer mais? '0 para encerrar': "))
print(f"FIM! Foram ao todo {total} de termos digitados.")