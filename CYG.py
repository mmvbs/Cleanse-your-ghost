import pygame
import sys
import os
import random
import classes.player as pl
import classes.mundo as mu
import classes.nuvem as nu
import classes.tumulos as tu
import classes.fantasma as fa

pygame.init() 

# Configura a tela
largura = 1280
altura = 720

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cleanse your Ghost")

# Instancias
jogador = pl.Player(largura, altura, tela)
jogador.load_images()
mundo = mu.Mundo(largura, altura, tela)
mundo.load_images()
nuvem = nu.Nuvem(largura, altura, tela)
nuvem.load_images()
tumulo = tu.Tumulos(largura, altura, tela)
tumulo.load_images()
fantasma = fa.Fantasma(largura, altura, tela)
#fantasma.load_images()
# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Preenche a tela
    tela.fill("black")
    mundo.update()
    tumulo.update()
    nuvem.update()
    fantasma.update()

    # Desenha
    mundo.draw()
    fantasma.draw()
    tumulo.draw()
    nuvem.draw()
    jogador.draw()
    jogador.run()

    if pygame.key.get_pressed()[pygame.K_j]:
        jogador.ataque()

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        jogador.jump()
    
    # Atualiza a tela
    pygame.display.update()

    # Controla a taxa de frames por segundo
    clock.tick(60) 

pygame.quit()