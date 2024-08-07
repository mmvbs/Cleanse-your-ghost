import pygame
import os

class Tumulos:
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.velocidade = 12
        self.stone1_x = 640

       

    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "stone-1.png")
        self.stone1 = pygame.image.load(sprite_path)
        self.stone1 = pygame.transform.scale(self.stone1, (100, 140))
        self.image = self.stone1
        self.image_rect = self.image.get_rect()
        
    def draw(self):
         self.tela.blit(self.stone1, (self.stone1_x, 480))
    def update(self):
        self.stone1_x -= self.velocidade
        if self.stone1_x <= -self.stone1.get_width():
            self.stone1_x = self.largura