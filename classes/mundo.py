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

        sprite_path = os.path.join(base_path, "bg.png")
        self.bg = pygame.image.load(sprite_path)
        self.bg = pygame.transform.scale(self.bg, (1280, 500))

        sprite_path = os.path.join(base_path, "stone-1.png")
        self.stone1 = pygame.image.load(sprite_path)
        self.stone1 = pygame.transform.scale(self.stone1, (100, 140))
        
    
    def chaodraw(self):
        self.tela.blit(self.bg, (0, 200))
        self.tela.blit(self.chao, (0, 620))
        self.tela.blit(self.stone1, (640, 500))
        