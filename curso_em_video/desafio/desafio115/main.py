from lib.interface.init import *
from lib.arquivo.init import *
from time import sleep

arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Cadastrar nova pessoa", "Listar pessoas", "Sair do sistema"])
    if resposta == 1:
        print("Opção 1")        
    elif resposta == 2:
        #listas as opções do arquivo
        lerArquivo(arq)
    elif resposta == 3:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Digite novamente.")
        sleep(2)
    