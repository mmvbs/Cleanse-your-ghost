import pygame
import os

class Obstaculo:
    def __init__(self, largura, altura, tela, x, y, velocidade, image_file, scale_size):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.rect = pygame.Rect(self.x, self.y, 90, 100)
        self.load_images(image_file, scale_size)

    def load_images(self, image_file, scale_size):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, image_file)
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, scale_size)

    def draw(self):
        self.tela.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.velocidade
        if self.x <= -self.image.get_width():
            self.x = self.largura
        self.rect.topleft = (self.x, self.y)


