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
def iniciar():
    global jogador, tumulo, fantasma, mundo, nuvem
    jogador = pl.Player(largura, altura, tela)
    jogador.load_images()
    mundo = mu.Mundo(largura, altura, tela)
    mundo.load_images()
    nuvem = nu.Nuvem(largura, altura, tela)
    nuvem.load_images()
    tumulo = tu.Tumulos(largura, altura, tela)
    tumulo.load_images()
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
    
     
    if jogador.checar_colisao(fantasma):
        tela.blit(pygame.font.Font.render(pygame.font.Font(None, 64), "Você perdeu", True, (255, 0, 0)), ((largura/2)-200, altura/2))
        running = False
    if jogador.checar_colisao(tumulo):
        #tela.blit(pygame.font.Font.render(pygame.font.Font(None, 64), "Você perdeu", True, (255, 0, 0)), ((largura/2)-200, altura/2))
        
        mundo.velocidade = 0
        tumulo.velocidade = 0
        nuvem.velocidade = 0
        fantasma.velocidade = 0
        tela.blit(pygame.font.Font.render(pygame.font.Font(None, 64), "Precione r para re-iniciar", True, (255, 0, 0)), ((largura/2)-300, altura/4))
        execucacao = False
        if pygame.key.get_pressed()[pygame.K_r]:
            tumulo.stone1_x = 900
            mundo.velocidade = 12
            tumulo.velocidade = 12
            nuvem.velocidade = 3
            jogador.rect.x = 100
            jogador.rect.y = 500
            execucacao = True
            iniciar()
    
    # pygame.draw.rect(tela, (255, 0, 0), jogador.rect, 2)
    # pygame.draw.rect(tela, (255, 0, 0), tumulo.rect, 2) 
    # pygame.draw.rect(tela, (255, 0, 0), fantasma.rect, 2)
    

    if pygame.key.get_pressed()[pygame.K_j]:
        jogador.ataque()

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        jogador.jump()

    
    
    # Atualiza a tela
    pygame.display.update()

    # Controla a taxa de frames por segundo
    clock.tick(60) 

pygame.quit()