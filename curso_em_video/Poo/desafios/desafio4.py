from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":open_book: Você acabou de abrir o livro '{self.titulo}', com {self.paginas} número de páginas, agora você está na página {self.pagina_atual}!")

    def avancar_paginas(self, qtde = 1):
        cont = 0
        for pg in range(0, qtde, 1):
            if not self.fim_livro():
                sleep(0.5)
                self.pagina_atual += 1
                print(f"Pág.{self.pagina_atual} :arrow_forward: ", end="")
                cont +=1

        print(f"\nVocê avançou {cont} páginas. Agora você está na página {self.pagina_atual}")

        if self.fim_livro():
            print(f":closed_book: Você chegou no final do livro {self.titulo}!")


    def fim_livro(self) -> bool:
        if self.pagina_atual == self.paginas:
            return True
        else:
            return False
        

l1 = Livro(titulo="'Como treinar seu dragão'", paginas=20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
