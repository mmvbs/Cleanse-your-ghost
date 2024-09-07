import pygame
import os

def carregar_imagem(path, tamanho):
     image = pygame.image.load(path)
     return pygame.transform.scale(image, tamanho)

class Entidade:
     def __init__(self, largura, altura, tela, x, y, velocidade, aceleracao_gravidade):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.aceleracao_gravidade = aceleracao_gravidade

     def draw(self):
          self.tela.blit(self.image, (self.x, self.y))
