import pygame
import os
import random

class Cenario:
    def __init__(self, largura, altura, tela, velocidade):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.velocidade = velocidade
        self.x_pos = 0
        self.y_pos = 0

    def load_images(self, image_file, scale_size):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, image_file)
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, scale_size)

    def draw(self):
        self.tela.blit(self.image, (self.x_pos, self.y_pos))

    def update(self):
        self.x_pos -= self.velocidade
        if self.x_pos <= -self.image.get_width():
            self.x_pos = self.largura


#classe mundo
class Mundo(Cenario):
    def __init__(self, largura, altura, tela):
        super().__init__(largura, altura, tela, velocidade=12)
        self.chao_x = 0
        self.bg_x = 0

        self.load_images("bg.png", (1280, 500))
        self.load_moon_image()

    def load_moon_image(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "bg-moon.png")
        self.bglua = pygame.image.load(sprite_path)
        self.bglua = pygame.transform.scale(self.bglua, (1280, 720))

    def draw(self):
        self.tela.blit(self.bglua, (0, 0))
        self.tela.blit(self.image, (self.bg_x, 200))
        self.tela.blit(self.image, (self.bg_x + self.image.get_width(), 200))  # Repete o fundo

    def update(self):
        self.bg_x -= self.velocidade
        if self.bg_x <= -self.image.get_width():
            self.bg_x = 0

#classe nuvem

class Nuvem(Cenario):
    def __init__(self, largura, altura, tela):
        super().__init__(largura, altura, tela, velocidade=3)
        self.x_size = 630
        self.y_size = 100
        self.x_pos = largura
        self.y_pos = 30
        self.load_images("nuvem.png", (self.x_size, self.y_size))

    def update(self):
        super().update()
        if self.x_pos <= -self.image.get_width():
            self.x_pos = self.largura
            self.y_pos = random.randint(8, 10) * 9

