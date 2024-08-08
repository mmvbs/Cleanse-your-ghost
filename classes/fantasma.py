import pygame
import os

def carregar_imagem(path, tamanho):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, tamanho)

class Fantasma:
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.x_Fantasma = 300
        self.y_Fantasma = 530
        self.aceleracao_gravidade = 1
        self.tamanho_imagem = (135, 87)
        self.velocidade = 0.5
        self.rect = pygame.Rect(self.x_Fantasma, 530, 70, 87)
        
        
        self.imagens = [
            carregar_imagem(os.path.join('texturas', 'fantasma1.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'fantasma2.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'fantasma3.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'fantasma4.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'fantasma5.png'), self.tamanho_imagem)
        ]
        
        self.step_index = 0
        self.image = self.imagens[0]
    
    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))

        sprite_path = os.path.join(base_path, "fantasma1.png")
        self.fantasma = pygame.image.load(sprite_path)
        self.fantasma = pygame.transform.scale(self.fantasma, (self.x_Fantasma, self.y_Fantasma))
    
    def draw(self):
        self.tela.blit(self.image, (self.x_Fantasma, self.y_Fantasma))

    def update(self):
        # Atualiza a animação
        self.step_index = (self.step_index + 1) % (len(self.imagens) * 5)
        self.image = self.imagens[self.step_index // 5]
        self.x_Fantasma -= self.velocidade
        self.rect.topleft = (self.x_Fantasma+50, 530)

  