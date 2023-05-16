import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Velha')

# Variáveis de pontuação
score = {"jogador_1": 0, "jogador_2": 0}

def update_score(winner):
    global score

    if winner == "jogador_1":
        score["jogador_1"] += 1
    elif winner == "jogador_2":
        score["jogador_2"] += 1

def render_score(screen):
    score_text = f"Jogador 1: {score['jogador_1']}  Jogador 2: {score['jogador_2']}"
    font = pygame.font.Font(None, 36)
    text = font.render(score_text, True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Resto do seu código...

ganhou = True
if ganhou:
    quem_ganhou = input("Quem foi o jogador que ganhou?")
    if quem_ganhou == "jogador_1" or quem_ganhou == "jogador_2":
        update_score(quem_ganhou)

print(f"Jogador 1: {score['jogador_1']}")
print(f"Jogador 2: {score['jogador_2']}")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.fill((0, 0, 0))  # Limpar a tela

    # Restante do seu código...

    render_score(tela)  # Renderizar as pontuações

    pygame.display.update()
