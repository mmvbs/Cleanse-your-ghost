import pygame
import sys
import os
import player as pl

pygame.init()

# Configura a tela
largura = 1280
altura = 720

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cleanse your Ghost")

# Instancia o jogador
jogador = pl.Player(largura, altura, tela)
jogador.load_images()

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Preenche a tela
    tela.fill("black")

    # Desenha o jogador
    jogador.draw()


    # Atualiza a tela
    pygame.display.update()

    # Controla a taxa de frames por segundo
    clock.tick(60)  # Limita a FPS a 60

pygame.quit()
