import pygame
import os

class Moita:
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.velocidade = 12
        self.bushLarge_x = 400
        self.bushLarge_y = 500
        self.rect = pygame.Rect(self.bushLarge_x, 500, 90, 100)

       

    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "bush-large.png")
        self.bushLarge = pygame.image.load(sprite_path)
        self.bushLarge = pygame.transform.scale(self.bushLarge, (152, 130))
        self.image = self.bushLarge
        self.image_rect = self.image.get_rect()
        
    def draw(self):
         self.tela.blit(self.bushLarge, (self.bushLarge_x, 500))
    def update(self):
        self.bushLarge_x -= self.velocidade
        if self.bushLarge_x <= -self.bushLarge.get_width():
            self.bushLarge_x = self.largura
        self.rect.topleft = (self.bushLarge_x, 500)