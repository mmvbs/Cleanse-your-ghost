import pygame
import os

class Player:
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.x_player = 50
        self.y_player = 485
        self.velocidade = 5
        self.aceleracao_gravidade = 1

    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "ocultie1.png")
        self.player_image = pygame.image.load(sprite_path)
        self.player_image = pygame.transform.scale(self.player_image, (78, 138))
        player_down_path = os.path.join(base_path, "ocultiedown.png")
        self.player_down_image = pygame.image.load(player_down_path)
        self.player_down_image = pygame.transform.scale(self.player_down_image, (78, 138))

    def draw(self):
        self.tela.blit(self.player_image, (self.x_player, self.y_player))
