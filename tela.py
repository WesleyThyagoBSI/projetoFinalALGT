import pygame
from pygame.locals import *
from sys import exit #função pra fechar a janela

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
