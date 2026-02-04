# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import os

# Obtém o caminho completo para o arquivo MP3
caminho_musica = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ex021.mp3')

pygame.init() # para iniciar o pygame
pygame.mixer.music.load(caminho_musica) # carrega o arquivo
pygame.mixer.music.play() # reproduz o arquivo

# Adiciona um input para o programa não fechar imediatamente
input("Pressione Enter para sair...")


# pygame tem a funcionalidade para criar jogos
# os descobre onde está o arquivo que quero executar 