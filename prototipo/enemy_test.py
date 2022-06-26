import sys
import pygame
from pygame.locals import *
from ControleInimigo import ControladorInimigo

from Jogador import Jogador
from Inimigo import Inimigo
from Arma import Arma
import numpy as np

#######################################
# parte do pygame (ficara no app.py)
pygame.init()
FPS_VALUE = 15
FPS = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# tela
DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURF.fill((255, 255, 255))
pygame.display.set_caption("Game")

#######################################
# propriedades iniciais do jogador
VIDA = 20
MOV_SPEED = 10
arma_inicial = Arma(4, 0, 20, 5)

inimigo = Inimigo(350, 350, 15, 2, "tilapia.png")
jogador = Jogador(VIDA, MOV_SPEED, arma_inicial, DISPLAY_SURF, SCREEN_WIDTH)
controleInimigo = ControladorInimigo(lista_inimigos=[inimigo], jogador=jogador)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

    DISPLAY_SURF.fill((255, 255, 255))
    jogador.mover()
    inimigo.desenhar(DISPLAY_SURF)
    controleInimigo.checar_colisao()
    DISPLAY_SURF.blit(jogador.sprite, jogador.rect)
    jogador.mover()


    pygame.display.update()
    FPS.tick(FPS_VALUE)
