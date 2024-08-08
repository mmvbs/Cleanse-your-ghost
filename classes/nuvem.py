import os 
import pygame
import random

class Nuvem:
    
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.x_size = 288
        self.y_size = 224
        self.x_pos = largura
        self.y_pos = 100
        self.velocidade = 3  # Velocidade das nuvens
        
        
    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))

        sprite_path = os.path.join(base_path, "nuvem.png")
        self.nuvem = pygame.image.load(sprite_path)
        self.nuvem = pygame.transform.scale(self.nuvem, (self.x_size, self.y_size))
    
    def draw(self):
        self.tela.blit(self.nuvem, (self.x_pos, self.y_pos))

    def update(self):
        self.x_pos -= self.velocidade
        if self.x_pos <= -self.nuvem.get_width():
            self.x_pos = self.largura  # Reposiciona a nuvem à direita da tela
            self.y_pos = random.randint(7,10)*10