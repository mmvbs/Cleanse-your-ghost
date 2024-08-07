import pygame
import os
class Mundo:
    
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.chao = None
        self.tela = tela

         # Posições iniciais
        self.chao_x = 0
        self.bg_x = 0
        self.stone1_x = 640  # Posição inicial do obstáculo

        # Velocidade de movimento
        self.velocidade = 12

    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        #fundo
        sprite_path = os.path.join(base_path, "bg.png")
        self.bg = pygame.image.load(sprite_path)
        self.bg = pygame.transform.scale(self.bg, (1280, 500))
        #lua
        sprite_path = os.path.join(base_path, "bg-moon.png")
        self.bglua = pygame.image.load(sprite_path)
        self.bglua = pygame.transform.scale(self.bglua, (1280, 720))
      
      
        
    
    def draw(self):
        self.tela.blit(self.bglua, (0, 0))
        self.tela.blit(self.bg, (self.bg_x, 200))
        self.tela.blit(self.bg, (self.bg_x + self.bg.get_width(),200))#Repete o fundo para evitar as lacunas pretas

    #Função para movimentação do mundo
    def update(self):
        # Move o fundo e o chão para a esquerda
        self.bg_x -= self.velocidade

        # Se o fundo saiu da tela, reposicione-o
        if self.bg_x <= -self.bg.get_width():
            self.bg_x = 0
        