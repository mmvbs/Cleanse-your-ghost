import pygame
import os
class Mundo:
    
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.chao = 100
        self.tela = tela

         # Posições iniciais
        self.chao_x = 0
        self.bg_x = 0
        self.stone1_x = 640  # Posição inicial do obstáculo

        # Velocidade de movimento
        self.velocidade = 7

        self.load_images()

    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "chao.png")
        self.chao = pygame.image.load(sprite_path)

        sprite_path = os.path.join(base_path, "bg.png")
        self.bg = pygame.image.load(sprite_path)
        self.bg = pygame.transform.scale(self.bg, (1280, 500))

        sprite_path = os.path.join(base_path, "stone-1.png")
        self.stone1 = pygame.image.load(sprite_path)
        self.stone1 = pygame.transform.scale(self.stone1, (100, 140))
        
    
    def chaodraw(self):
        self.tela.blit(self.bg, (self.bg_x, 200))
        self.tela.blit(self.bg, (self.bg_x + self.bg.get_width(),200))#Repete o fundo para evitar as lacunas pretas
        self.tela.blit(self.chao, (self.chao_x, 620))
        self.tela.blit(self.chao, (self.chao_x + self.chao.get_width(),620))##Repete o châo para evitar as lacunas pretas
        self.tela.blit(self.stone1, (self.stone1_x, 500))

    #Função para movimentação do mundo
    def update(self):
        # Move o fundo e o chão para a esquerda
        self.bg_x -= self.velocidade
        self.chao_x -= self.velocidade

        # Se o fundo saiu da tela, reposicione-o
        if self.bg_x <= -self.bg.get_width():
            self.bg_x = 0
        
        # Se o chão saiu da tela, reposicione-o
        if self.chao_x <= -self.chao.get_width():
            self.chao_x = 0

        # Move o obstáculo para a esquerda
        self.stone1_x -= self.velocidade

        # Se o obstáculo saiu da tela, reposicione-o
        if self.stone1_x <= -self.stone1.get_width():
            self.stone1_x = self.largura