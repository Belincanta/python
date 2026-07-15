from lib.interface.init import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Arquivo não criado!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Não foi possível abrir o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(a.read())

