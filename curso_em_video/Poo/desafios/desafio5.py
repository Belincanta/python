from rich import print
from rich.panel import Panel
from rich import inspect
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick    
        self.favoritos = list()

    def adicionar_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def status(self):
        conteudo = f"Nome real: [black on white] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [green] {game} [/]"

        panel = Panel(conteudo, title = f"Jogador <{self.nick}>", width=40)
        print(panel)

j1 = Gamer(nome="Alessandro", nick="ale_belo")
j1.adicionar_favoritos("Mario bross")
j1.adicionar_favoritos("Left 4 dead")
j1.adicionar_favoritos("Man Hunt")
j1.adicionar_favoritos("Sonic")
j1.status()

j2 = Gamer(nome="Belincanta", nick="belin_canta")
j2.adicionar_favoritos("GTA")
j2.adicionar_favoritos("Need for Speed")
j2.adicionar_favoritos("Resident evil")
j2.status()