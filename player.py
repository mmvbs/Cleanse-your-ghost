import pygame


sprite_path = os.path.join(os.path.dirname(__file__), "ocultie1.png")
bloco_sprite_right = pygame.image.load(sprite_path)
bloco_sprite_right = pygame.transform.scale(bloco_sprite_right, (78, 138))
bloco_sprite_left = pygame.transform.flip(bloco_sprite_right, True, False)
bloco_sprite_down = pygame.image.load(os.path.join(os.path.dirname(__file__), "ocultiedown.png"))
bloco_sprite_down = pygame.transform.scale(bloco_sprite_down, (78, 138))
bloco_sprite_down_left = pygame.transform.flip(bloco_sprite_down, True, False)

# Posição inicial do bloco
x_player = largura // 2 - bloco_sprite_right.get_width() // 2
y_player = y_chao - bloco_sprite_right.get_height() - 10

#velocidades
velocidade = 5
aceleracao_gravidade = 1
ultima_tecla= pygame.K_RIGHT    