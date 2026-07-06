# tratamento de erros com try e except.

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b

except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados")
except ZeroDivisionError:
    print("Não pode ser dividido por zero")
except KeyboardInterrupt:
    print("Usuário não quis digitar os dados")
except Exception as erro: #criando uma variável é possivel retornar o tipo do erro, se houver
    print(f"Erro encontrato foi {erro.__class__}")

else:
    print(f"O resultado é {r}")