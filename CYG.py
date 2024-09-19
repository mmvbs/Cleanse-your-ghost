import pygame
import sys
import os
import random
import classes.player as pl
import classes.fantasma as fa
from classes.player import Player
from classes.fantasma import Fantasma
from classes.obstaculos import Obstaculo
from classes.cenario import Mundo, Nuvem

pygame.init()

# Configura a tela
largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cleanse your Ghost")

# Instâncias
jogador = pl.Player(largura, altura, tela)
mundo = Mundo(largura, altura, tela)
nuvem = Nuvem(largura, altura, tela)
tumulo = Obstaculo(largura, altura, tela, 900, 480, 12, "stone-1.png", (100, 140))
moita = Obstaculo(largura, altura, tela, 400, 500, 12, "bush-large.png", (152, 130))
fantasma = fa.Fantasma(largura, altura, tela)

def iniciar():
    global jogador, tumulo, fantasma, mundo, nuvem, moita
    jogador = pl.Player(largura, altura, tela)
    mundo = Mundo(largura, altura, tela)
    nuvem = Nuvem(largura, altura, tela)
    tumulo = Obstaculo(largura, altura, tela, 900, 480, 12, "stone-1.png", (100, 140))
    moita = Obstaculo(largura, altura, tela, 400, 500, 12, "bush-large.png", (152, 130))
    fantasma = fa.Fantasma(largura, altura, tela)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()
execucacao = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tela.fill("black")

    # Atualização dos objetos do jogo
    mundo.update()
    tumulo.update()
    moita.update()
    nuvem.update()
    fantasma.update()

    # Desenho dos objetos na tela
    mundo.draw()
    fantasma.draw()
    tumulo.draw()
    moita.draw()
    nuvem.draw()
    jogador.draw()
    jogador.run()

    # Verifica colisões
    if jogador.checar_colisaoataque(moita):
        moita.bushLarge_x = 1290
        jogador.ataquerect = pygame.Rect(jogador.x +150, 700, 200, 150)
        fantasma.velocidade = 3

    if jogador.checar_colisao(moita):
        fantasma.velocidade = 0.5

    if jogador.checar_colisao(fantasma):
        tela.blit(pygame.font.Font.render(pygame.font.Font(None, 64), "Você capturou o fantasma", True, (0, 255, 0)), ((largura / 2) - 200, altura / 2))
        mundo.velocidade = 0
        tumulo.velocidade = 0
        moita.velocidade = 0
        nuvem.velocidade = 0
        fantasma.velocidade = 0
        tela.blit(pygame.font.Font.render(pygame.font.Font(None, 64), "Pressione R para reiniciar", True, (255, 0, 0)), ((largura / 2) - 200, altura / 4))
        execucacao = False

        if pygame.key.get_pressed()[pygame.K_r]:
            fantasma.x = 1000
            mundo.velocidade = 12
            fantasma.velocidade = 0.5
            nuvem.velocidade = 3
            jogador.rect.x = 100
            jogador.rect.y = 500
            execucacao = True
            iniciar()

    if jogador.checar_colisao(tumulo):
        mundo.velocidade = 0
        tumulo.velocidade = 0
        moita.velocidade = 0
        nuvem.velocidade = 0
        fantasma.velocidade = 0
        tela.blit(pygame.font.Font.render(pygame.font.Font(None, 64), "Pressione R para reiniciar", True, (255, 0, 0)), ((largura / 2) - 300, altura / 4))
        execucacao = False

        if pygame.key.get_pressed()[pygame.K_r]:
            tumulo.x = 900
            moita.x = 400
            mundo.velocidade = 12
            tumulo.velocidade = 12
            moita.velocidade = 12
            nuvem.velocidade = 3
            jogador.rect.x = 100
            jogador.rect.y = 500
            execucacao = True
            iniciar()
    
    pygame.draw.rect(tela, (255, 0, 0), jogador.rect, 2)
    pygame.draw.rect(tela, (255, 0, 0), tumulo.rect, 2) 
    pygame.draw.rect(tela, (255, 0, 0), fantasma.rect, 2)
    pygame.draw.rect(tela, (255, 0, 0), moita.rect, 2)
    pygame.draw.rect(tela, (255, 0, 0), jogador.ataquerect, 2)
    
    if pygame.key.get_pressed()[pygame.K_j]:
        jogador.ataque()
        

        

    # Pulo do jogador
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        jogador.jump()

    # Atualiza a tela
    pygame.display.update()

    # Controla a taxa de frames por segundo
    clock.tick(60)

pygame.quit()
