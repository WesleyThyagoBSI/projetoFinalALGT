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
    global fonte
    score_jogador1 = f"Pontos: {score['jogador_1']}"
    score_jogador2 = f"Pontos: {score['jogador_2']}"
    
    # Preencher a área da pontuação com a cor de fundo
    screen.fill((0, 0, 0), (330, 120, 200, 50))
    screen.fill((0, 0, 0), (490, 120, 200, 50))
    
    textJogador1 = fonte.render(score_jogador1, True, (255, 0, 0))
    textJogador2 = fonte.render(score_jogador2, True, (0, 0, 255))
    screen.blit(textJogador1, (330, 120))
    screen.blit(textJogador2, (490, 120))

# Resto do seu código...

ganhou = True
if ganhou:
    quem_ganhou = input("Quem foi o jogador que ganhou?")
    if quem_ganhou == "jogador_1" or quem_ganhou == "jogador_2":
        update_score(quem_ganhou)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.fill((0, 0, 0))  # Limpar a tela

    print(f"Jogador 1: {score['jogador_1']}")
    print(f"Jogador 2: {score['jogador_2']}")

    render_score(tela)  # Renderizar as pontuações

    pygame.display.update()
