
# importando as bibliotecas
import pygame
from pygame.locals import *
from sys import exit

pygame.init() #inicializando o pygmae

largura = 640
altura = 480
 # criando a tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Velha')

def posicao_mouse(numero_jogada):
    posicao_mouse = pygame.mouse.get_pos()
    
    if ((posicao_mouse[0]>10 and posicao_mouse[0]<110) and (posicao_mouse[1]>50 and posicao_mouse[1]<150)): #defininco o primeiro quadrante
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (60, 100), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (45, 85, 30, 30))
    elif ((posicao_mouse[0]>110 and posicao_mouse[0]<210) and (posicao_mouse[1]>50 and posicao_mouse[1]<150)):
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (160, 100), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (145, 85, 30, 30))        
    elif ((posicao_mouse[0]>210 and posicao_mouse[0]<310) and (posicao_mouse[1]>50 and posicao_mouse[1]<150)):
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (260, 100), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (245, 85, 30, 30))  
    elif ((posicao_mouse[0]>10 and posicao_mouse[0]<110) and (posicao_mouse[1]>150 and posicao_mouse[1]<250)): #defininco o primeiro quadrante
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (60, 200), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (45, 185, 30, 30))
    elif ((posicao_mouse[0]>110 and posicao_mouse[0]<210) and (posicao_mouse[1]>=150 and posicao_mouse[1]<=250)):
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (160, 200), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (145, 185, 30, 30))
    elif ((posicao_mouse[0]>210 and posicao_mouse[0]<310) and (posicao_mouse[1]>=150 and posicao_mouse[1]<=250)):
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (260, 200), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (245, 185, 30, 30))
    elif ((posicao_mouse[0]>10 and posicao_mouse[0]<110) and (posicao_mouse[1]>250 and posicao_mouse[1]<350)): #defininco o primeiro quadrante
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (60, 300), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (45, 285, 30, 30))
    elif ((posicao_mouse[0]>110 and posicao_mouse[0]<210) and (posicao_mouse[1]>=250 and posicao_mouse[1]<=350)):
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (160, 300), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (145, 285, 30, 30))
    elif ((posicao_mouse[0]>210 and posicao_mouse[0]<310) and (posicao_mouse[1]>=250 and posicao_mouse[1]<=350)):
        if (numero_jogada % 2 != 0):
            pygame.draw.circle(tela, (0,255,0), (260, 300), 15)
        else:
            pygame.draw.rect(tela, (0,0,255), (245, 285, 30, 30))

numero_jogada = 0
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            numero_jogada += 1
            print(f"Numero da jogada: {numero_jogada}")
            posicao_mouse(numero_jogada)
    # definindo cor e largura da linha
    cor_da_linha = (255, 0, 0)  # vermelho
    largura_linha = 2


    # desenhando um quadrado sem preenchimento
    square_rect = pygame.Rect(10, 50, 300, 300)
    pygame.draw.rect(tela, cor_da_linha, square_rect, largura_linha)
    # traçando as linhas verticais da grade 3x3
    pygame.draw.line(tela, (255,0,0), (110, 50), (110, 350))
    pygame.draw.line(tela, (255,0,0), (210, 50), (210, 350))
    # traçando as linhas horizontais da grade 3x3
    pygame.draw.line(tela, (255,0,0), (10, 150), (310, 150))
    pygame.draw.line(tela, (255,0,0), (10, 250), (310, 250))
    # pygame.draw.line(tela, (255,0,0), (210, 50), (210, 350))
    pygame.display.update()


