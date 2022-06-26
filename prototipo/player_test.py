import sys
import pygame
from pygame.locals import *

from Jogador import Jogador
from Arma import Arma

#######################################
# parte do pygame (ficara no app.py)
pygame.init()
FPS_VALUE = 60
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

player = Jogador(VIDA, MOV_SPEED, arma_inicial, DISPLAY_SURF, SCREEN_WIDTH)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

    DISPLAY_SURF.fill((255, 255, 255))
    DISPLAY_SURF.blit(player.sprite, player.rect)
    player.mover()

    pygame.display.update()
    FPS.tick(FPS_VALUE)
