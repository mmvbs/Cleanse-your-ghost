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
        self.x_Fantasma = 40
        self.y_Fantasma = 500
        self.velocidade = 3
        self.aceleracao_gravidade = 1
        self.tamanho_imagem = (120, 100)
        
        
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
      
        self.step_index = (self.step_index + 1) % (len(self.imagens) * 10)  
        self.image = self.imagens[self.step_index // 10] 

        self.x_Fantasma += self.velocidade
        if self.x_Fantasma > self.largura:  
            self.x_Fantasma = -self.tamanho_imagem[0]

  