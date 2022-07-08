import pygame
from pygame.locals import *
import sys
import random as rd
import numpy as np
from ControleArmas import ControleArmas

from ControleInimigo import ControladorInimigo
from ControleJogador import ControleJogador

from Jogador import Jogador
from Inimigo import Inimigo
from Arma import Arma
from InimigoRastreador import InimigoRastreador
from InimigoAtirador import InimigoAtirador

from ControleBalasJogador import ControleBalasJogador
from CollisionHandler import CollisionHandler

from Settings import Settings

#######################################
# parte do pygame (ficara no app.py)
pygame.init()
settings = Settings()

settings.FPS_VALUE = 20

FPS = pygame.time.Clock()

settings.largura_tela = 640
settings.altura_tela = 640

# tela
settings.DISPLAY_SURF = pygame.display.set_mode(
    (settings.largura_tela, settings.altura_tela)
)
settings.DISPLAY_SURF.fill((255, 255, 255))
pygame.display.set_caption("Game")

#######################################

lista_inimigos = [
    # Inimigo(350, 350, 15, 2, "assets/tilapia.png"),
    # Inimigo(200, 470, 15, 2, "assets/bacalhau_radioativo.png"),
    # Inimigo(120, 330, 15, 2, "assets/tilapia.png"),
    InimigoAtirador(405, 250, 5, 20, "assets/lulaAtiradora.png"),
    # Inimigo(370, 100, 15, 2, "assets/tilapia.png"),
    # InimigoRastreador(380, 120, 3, 1, "assets/cobraD'agua.png")
]
controleInimigo = ControladorInimigo()

jogador = Jogador(vida=20, velocidade_movimento=8)
controleArmas = ControleArmas(jogador)
# controleArmas.trocar_arma("rede")

controleJogador = ControleJogador(jogador)
controleBalasJogador = ControleBalasJogador()

collisionHandler = CollisionHandler()

sprites = pygame.sprite.Group()
sprites.add(jogador)

grupo_inimigos = pygame.sprite.Group()

for inimigo in lista_inimigos:
    grupo_inimigos.add(inimigo)
    sprites.add(inimigo)

#######################################

morto = False
while True:
    if morto:
        pygame.display.set_caption("Chico Cunha está morto. Reflita sobre suas ações.")
        settings.DISPLAY_SURF.blit(jogador.sprite, jogador.rect)
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
            
            # caso detecte um tiro, adiciona ao controlador de balas do jogador
            if tiro:
                controleBalasJogador.nova_bala(tiro)

    # fundo branco
    settings.DISPLAY_SURF.fill((255, 255, 255))

    # laço que percorre todos inimigos e jogador e redesenha

    # for entity in sprites:
    # settings.DISPLAY_SURF.blit(entity.sprite, entity.rect)
    # x, y = controleInimigo.caminho_atirador(inimigo, jogador.x, jogador.y, 5)
    # entity.mover(x, y)

    x, y = controleInimigo.caminho_atirador(
        lista_inimigos[0], jogador.x, jogador.y, 250
    )

    tiro_inimigo = inimigo.atacar(x, y)
    if tiro_inimigo:
        controleBalasJogador.nova_bala(tiro_inimigo)

    jogador.mover()
    inimigo.mover(x, y)

    controleBalasJogador.desenhar()
    for entity in sprites:
        settings.DISPLAY_SURF.blit(entity.sprite, entity.rect)

    collisionHandler.verificar_colisoes(
        grupo_inimigos, jogador, controleBalasJogador.grupo_balas
    )

    if jogador.vida <= 0:
        jogador.set_sprite("assets/ChicoCunhaMorto.png")
        settings.DISPLAY_SURF.fill((255, 255, 255))
        settings.DISPLAY_SURF.blit(jogador.sprite, jogador.rect)
        morto = True

    pygame.display.update()
    FPS.tick(settings.FPS_VALUE)
