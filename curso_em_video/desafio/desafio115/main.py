from lib.interface.init import *
from time import sleep

while True:
    resposta = menu(["Cadastrar nova pessoa", "Listar pessoas", "Sair do sistema"])
    if resposta == 1:
        print("Opção 1")
    elif resposta == 2:
        print("Opção 2")
    elif resposta == 3:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Digite novamente.")
        sleep(2)
    