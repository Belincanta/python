#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print("ERRO! o número digitado não é inteiro.")
            continue
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print("ERRO! O número digitado não é real.")
            continue
        else:
            return n


#programa principal
num = leiaInt("Digite um número inteiro: ")
print(f"O número digitado foi {num}")
num_float = leiaFloat('Digite um número real: ')
print(f"O número real é {num_float}")