import pygame
import os

def carregar_imagem(path, tamanho):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, tamanho)

class Entidade:
    def __init__(self, largura, altura, tela, x, y, velocidade, escala):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.escala = escala
        self.rect = pygame.Rect(self.x, self.y, largura, altura)
        self.imagens = []
        self.image = None
        self.step_index = 0

    def carregar_imagens(self, caminhos, tamanho):
        self.imagens = [carregar_imagem(caminho, tamanho) for caminho in caminhos]
        self.image = self.imagens[0]

    def atualizar_posicao(self, dx=0, dy=0):
        self.x += dx * self.velocidade
        self.y += dy * self.velocidade
        self.rect.topleft = (self.x, self.y)

    def desenhar(self):
        self.tela.blit(self.image, (self.x, self.y))

    def atualizar_animacao(self, frame_rate):
        
        self.step_index = (self.step_index + 1) % (len(self.imagens) * frame_rate)
        self.image = self.imagens[self.step_index // frame_rate]

    def checar_colisao(self, objeto):
        return self.rect.colliderect(objeto.rect)
