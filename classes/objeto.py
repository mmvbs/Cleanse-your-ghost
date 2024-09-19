import pygame
import os

class Objeto:
    def __init__(self, largura, altura, tela, sprite_nome, velocidade, x_inicial, y_inicial, largura_sprite, altura_sprite):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.velocidade = velocidade
        self.x = x_inicial
        self.y = y_inicial
        self.rect = pygame.Rect(self.x, self.y, largura_sprite, altura_sprite)
        self.image = None

    def load_images(self, sprite_nome, largura_sprite, altura_sprite):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, sprite_nome)
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, (largura_sprite, altura_sprite))

    def draw(self):
        self.tela.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.velocidade
        if self.x <= -self.image.get_width():
            self.x = self.largura
        self.rect.topleft = (self.x, self.y)
