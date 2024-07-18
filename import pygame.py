import pygame
import sys
import os
import player


pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cleanse your Ghost")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    tela.fill("black")

    # RENDER YOUR GAME HERE

   
    pygame.display.update()

    pygame.time.Clock().tick(60)  # limits FPS to 60

pygame.quit()