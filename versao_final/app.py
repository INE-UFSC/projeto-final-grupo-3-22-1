import sys
import pygame
from pygame.locals import *
import random as rd

from ControleInimigo import ControladorInimigo
from ControleJogador import ControleJogador

from Jogador import Jogador
from Inimigo import Inimigo
from Arma import Arma
from BulletHandler import BulletHandler
from CollisionHandler import CollisionHandler
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

lista_inimigos = [
    Inimigo(350, 350, 15, 2, "assets/tilapia.png", SCREEN_WIDTH),
    Inimigo(200, 470, 15, 2, "assets/bacalhau_radioativo.png", SCREEN_WIDTH),
    Inimigo(120, 330, 15, 2, "assets/tilapia.png", SCREEN_WIDTH),
    Inimigo(405, 250, 15, 2, "assets/bacalhau_radioativo.png", SCREEN_WIDTH),
    Inimigo(370, 100, 15, 2, "assets/tilapia.png", SCREEN_WIDTH),
]
jogador = Jogador(VIDA, MOV_SPEED, arma_inicial, DISPLAY_SURF, SCREEN_WIDTH)
controleInimigo = ControladorInimigo()
controleJogador = ControleJogador(jogador=jogador)

bulletHandler = BulletHandler()
collisionHandler = CollisionHandler()

sprites = pygame.sprite.Group()
sprites.add(jogador)

for inimigo in lista_inimigos:
    sprites.add(inimigo)

morto = False
while True:
    if morto:
        pygame.display.set_caption("Chico Cunha está morto. Reflita sobre suas ações.")
        DISPLAY_SURF.blit(
            jogador.sprite, jogador.rect
        )  # isso aqui era só pra deixar a imagem do Chico Cunha morto na tela de morte
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        continue  # continue faz com que se esse if seja ativado, o while loop vai continuar aqui dentro e não passar pros próximos

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tiro = jogador.atirar(mouse_x, mouse_y)
            bulletHandler.nova_bala(tiro)

    # fundo branco
    DISPLAY_SURF.fill((255, 255, 255))

    # laço que percorre todos inimigos e jogador e redesenha
    for entity in sprites:
        DISPLAY_SURF.blit(entity.sprite, entity.rect)
        entity.mover()

    bulletHandler.desenhar(DISPLAY_SURF)
    collisionHandler.verificar_colisoes(
        lista_inimigos, jogador, bulletHandler.lista_balas
    )

    if jogador.vida <= 0:
        jogador.set_sprite("assets/ChicoCunhaMorto.png")
        DISPLAY_SURF.fill((255, 255, 255))
        DISPLAY_SURF.blit(jogador.sprite, jogador.rect)
        morto = True

    pygame.display.update()
    FPS.tick(FPS_VALUE)
