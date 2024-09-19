from classes.entidade import Entidade
import pygame
import os

def carregar_imagem(path, tamanho):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, tamanho)

class Fantasma(Entidade):
    def __init__(self, largura, altura, tela):
        super().__init__(largura, altura, tela, 1000, 530, 0.5, 1)  # Chama o construtor da superclasse
        
        self.tamanho_imagem = (135, 87)
        self.rect = pygame.Rect(self.x, 530, 70, 87)
        
        # Carrega as imagens específicas do Fantasma
        caminhos_imagens = [
            os.path.join('texturas', 'fantasma1.png'),
            os.path.join('texturas', 'fantasma2.png'),
            os.path.join('texturas', 'fantasma3.png'),
            os.path.join('texturas', 'fantasma4.png'),
            os.path.join('texturas', 'fantasma5.png')
        ]
        self.carregar_imagens(caminhos_imagens, self.tamanho_imagem)  # Usa o método da superclasse

    def update(self):
        # Atualiza a animação e posição usando os métodos da superclasse
        super().atualizar_animacao(5)  # Atualiza a animação com a taxa de quadros por segundo
        super().atualizar_posicao(dx=-1)  # Move o fantasma para a esquerda

        # Atualiza a posição do rect (ajuste extra)
        self.rect.topleft = (self.x + 50, 530)

    def draw(self):
        # Desenha o fantasma usando o método da superclasse
        super().desenhar()