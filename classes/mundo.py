import pygame
import os
class Mundo:
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.chao = 100
        self.tela = tela


    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "chao.png")
        self.chao = pygame.image.load(sprite_path)
    
    def chaodraw(self):
        self.tela.blit(self.chao, (0, 620))
        