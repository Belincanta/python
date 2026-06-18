import uteis #para chamar as funções
#from uteis import fatorial, dobro, triplo - usando assim não precisa do uteis.

num = int(input("Digite um número: "))
fat = uteis.fatorial(num)
print(f"O fatorial do número {num} é {fat}!")
print(f"O dobro do número {num} é {uteis.dobro(num)}!")
print(f"O triplo do número {num} é {uteis.triplo(num)}!")