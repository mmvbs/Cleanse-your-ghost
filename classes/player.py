import pygame
import os



def carregar_imagem(path, tamanho):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, tamanho)
class Player:
    def __init__(self, largura, altura, tela):
        self.largura = largura
        self.altura = altura
        self.tela = tela
        self.x_player = 40
        self.y_player = 235
        self.velocidade = 5
        self.aceleracao_gravidade = 1

        
        self.tamanho_imagem = (384, 384)

        self.correndo = [
            carregar_imagem(os.path.join('texturas', 'correr1.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'correr2.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'correr3.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'correr4.png'), self.tamanho_imagem),
        ]
        self.atacando = [
            carregar_imagem(os.path.join('texturas', 'ataque1.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'ataque2.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'ataque3.png'), self.tamanho_imagem),
            carregar_imagem(os.path.join('texturas', 'ataque4.png'), self.tamanho_imagem),
        ]
        self.step_index = 0
        self.ataque_index = 0
        self.image = self.atacando[0]
        self.image = self.correndo[0]  
    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "ocultie1.png")
        self.player_image = carregar_imagem(sprite_path, self.tamanho_imagem)
        player_down_path = os.path.join(base_path, "ocultiedown.png")
        self.player_down_image = carregar_imagem(player_down_path, self.tamanho_imagem)

    def draw(self):
        self.tela.blit(self.image, (self.x_player, self.y_player))

    def ataque(self):
        self.image = self.atacando[self.ataque_index// 5]
        self.ataque_index =(self.ataque_index + 1) % (len(self.atacando) *5)

    def run(self):
        # Atualiza o frame da animação de corrida
        self.image = self.correndo[self.step_index // 5]
        self.step_index = (self.step_index + 1) % (len(self.correndo) * 5)  # Mantém o índice dentro dos limites
