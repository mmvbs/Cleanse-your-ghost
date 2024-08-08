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

        # P/Pulo
        self.AlturaPulo = -25  # Tamanho do pulo
        self.tempopulo = 0
        self.pulando = False
        self.velocidade_pulo = self.AlturaPulo
        self.gravity = 1.5
        self.tempo_pulo = self.tempopulo

        self.tamanho_imagem = (384, 384)
        self.rect = pygame.Rect(self.x_player +150, 470, 80, 150)
        self.ataquerect = pygame.Rect(self.x_player +150, 700, 200, 150)

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
        self.image = self.correndo[0]

        # Cooldown e ataque
        self.cooldown_ataque = 750
        self.ultimo_ataque = 0
        self.ataque_count = 0
        self.barra_cor = (255, 0, 0)
        self.barra_fundo_cor = (0, 0, 0)
        self.barra_altura = 12
        self.barra_largura = self.tamanho_imagem[0] / 5  # Tamanho da barra de cooldown

    def load_images(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'texturas'))
        sprite_path = os.path.join(base_path, "ocultie1.png")
        self.player_image = carregar_imagem(sprite_path, self.tamanho_imagem)
        player_down_path = os.path.join(base_path, "ocultiedown.png")
        self.player_down_image = carregar_imagem(player_down_path, self.tamanho_imagem)

    def ataque(self):
        tempo_atual = pygame.time.get_ticks()

        if tempo_atual - self.ultimo_ataque >= self.cooldown_ataque:
            self.image = self.atacando[self.ataque_index]
            self.ataque_index += 1
            self.ataque_count += 1
            self.ataquerect = pygame.Rect(self.x_player +150, 470, 200, 150)

            if self.ataque_index >= len(self.atacando):
                self.ataque_index = 0
                self.ataquerect = pygame.Rect(self.x_player +150, 700, 200, 150)

            if self.ataque_count >= 4:
                self.ataquerect = pygame.Rect(self.x_player +150, 700, 200, 150)
                self.ultimo_ataque = tempo_atual
                self.ataque_count = 0

    def run(self):
        # Atualiza o frame da animação de corrida
        self.image = self.correndo[self.step_index // 5]
        self.step_index = (self.step_index + 1) % (len(self.correndo) * 5)  # Mantém o índice dentro dos limites

        # Atualiza Física do Pulo
        self.atualiza_pulo()

    def jump(self):
        # Faz o personagem pular
        if not self.pulando:
            self.pulando = True
            self.tempo_pulo = self.tempopulo

    def atualiza_pulo(self):
        # Atualiza a física do pulo
        if self.pulando:
            self.y_player += self.velocidade_pulo
            self.rect.y += self.velocidade_pulo
            self.tempo_pulo += 1
            self.velocidade_pulo += self.gravity

            # Verifica se o pulo terminou (se o jogador voltou ao chão)
            if self.y_player >= 235:
                self.y_player = 235
                self.rect.y = 470
                self.pulando = False
                self.velocidade_pulo = self.AlturaPulo
                self.tempo_pulo = self.tempopulo

    def draw(self):
        self.tela.blit(self.image, (self.x_player, self.y_player))  # Desenha personagem
        self.draw_cooldown_bar()  # Desenha Cooldown

    def draw_cooldown_bar(self):
        tempo_atual = pygame.time.get_ticks()
        tempo_restante = max(0, self.cooldown_ataque - (tempo_atual - self.ultimo_ataque))

        # Calcula a largura da barra
        barra_largura = (tempo_restante / self.cooldown_ataque) * self.barra_largura

        # Desenha a barra de fundo
        pygame.draw.rect(self.tela, self.barra_fundo_cor, (self.x_player * 5, self.y_player - (-200), self.barra_largura, self.barra_altura))

        # Desenha a barra de cooldown
        pygame.draw.rect(self.tela, self.barra_cor, (self.x_player * 5, self.y_player - (-200), barra_largura, self.barra_altura))

    def checar_colisao(self, objeto):
        return self.rect.colliderect(objeto.rect)
    def checar_colisaoataque(self, objeto):
        return self.ataquerect.colliderect(objeto.rect)