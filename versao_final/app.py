import pygame
from pygame.locals import *
import sys
import os
import random as rd
import numpy as np
from ControleArmas import ControleArmas

from ControleJogador import ControleJogador

from Jogador import Jogador
from InimigoBasico import InimigoBasico
from Arma import Arma
from InimigoRastreador import InimigoRastreador
from InimigoAtirador import InimigoAtirador
from InimigoCorredor import InimigoCorredor

from GrupoBalasJogador import GrupoBalasJogador
from GrupoBalasInimigo import GrupoBalasInimigo
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

inimigos_basicos = [
    InimigoBasico(350, 350, 15, 2, "assets/peixe_palhaco.png"),
    InimigoBasico(200, 470, 15, 2, "assets/bacalhau_radioativo.png"),
    InimigoBasico(120, 330, 15, 2, "assets/peixe_palhaco.png"),
    InimigoBasico(370, 100, 15, 2, "assets/peixe_palhaco.png"),
]

inimigos_atiradores = [
    InimigoAtirador(405, 250, 1, 20, "assets/lulaAtiradora.png", 6),
    InimigoAtirador(200, 230, 1, 20, "assets/lulaAtiradora.png", 6),
]

inimigos_rastreadores = [
    InimigoRastreador(330, 100, 3, 1, "assets/cobraD'agua.png"),
    InimigoRastreador(380, 120, 3, 1, "assets/cobraD'agua.png"),
]

inimigos_corredores = [
    InimigoCorredor(400, 110, 20, 20, "assets/peixe_espada.png")
]


jogador = Jogador(vida=20, velocidade_movimento=8)

controleArmas = ControleArmas(jogador)
controleArmas.trocar_arma("arpao")

controleArmas = ControleArmas(jogador)
controleJogador = ControleJogador(jogador)
grupoBalasJogador = GrupoBalasJogador()
grupoBalasInimigo = GrupoBalasInimigo()
collisionHandler = CollisionHandler()

sprites = pygame.sprite.Group()
sprites.add(jogador)

grupo_inimigos_basicos = pygame.sprite.Group()
grupo_inimigos_atiradores = pygame.sprite.Group()
grupo_inimigos_rastreadores = pygame.sprite.Group()
grupo_inimigos = pygame.sprite.Group()

for inimigo in inimigos_basicos:
    grupo_inimigos_basicos.add(inimigo)
    sprites.add(inimigo)
    grupo_inimigos.add(inimigo)

for inimigo in inimigos_atiradores:
    grupo_inimigos_atiradores.add(inimigo)
    sprites.add(inimigo)
    grupo_inimigos.add(inimigo)

for inimigo in inimigos_rastreadores:
    grupo_inimigos_rastreadores.add(inimigo)
    sprites.add(inimigo)
    grupo_inimigos.add(inimigo)

#######################################

jogando = True
morto = False
while jogando:
    if morto:
        pygame.display.set_caption("Chico Cunha está morto. Reflita sobre suas ações.")
        settings.DISPLAY_SURF.blit(jogador.sprite, jogador.rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                jogando = False
        continue  # continue faz com que se esse if seja ativado, o while loop vai continuar aqui dentro e não passar pros próximos

    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

        if event.type == pygame.MOUSEBUTTONDOWN:
            tiro = jogador.atirar(mouse_x, mouse_y)
            # caso detecte um tiro, adiciona ao controlador de balas do jogador
            if tiro:
                grupoBalasJogador.nova_bala(tiro)

    # fundo branco
    settings.DISPLAY_SURF.fill((255, 255, 255))

    # percorre todos os inimigos atiradores e executa suas funções
    for atirador in grupo_inimigos_atiradores:
        # fazendo o atirador atirar
        tiro_inimigo = atirador.atacar(jogador.x, jogador.y)
        if tiro_inimigo:
            grupoBalasInimigo.nova_bala(tiro_inimigo)

        # achando o caminho do atirador
        x, y = atirador.achar_caminho(jogador.x, jogador.y, 250)

        # movendo o atirador com os resultados obtidos anteriormente
        atirador.mover(x, y)

    for basico in grupo_inimigos_basicos:
        basico.mover()

    for rastreador in grupo_inimigos_rastreadores:
        # achando o caminho do rastreador
        x, y = rastreador.achar_caminho(rastreador, jogador.x, jogador.y)

        # movendo o rastreador com os resultados obtidos
        rastreador.mover(x, y)

    jogador.mover()
    jogador.mover_arma(mouse_x, mouse_y)

    grupoBalasJogador.desenhar()
    grupoBalasInimigo.desenhar()
    for entity in sprites:
        settings.DISPLAY_SURF.blit(entity.sprite, entity.rect)

    collisionHandler.verificar_colisoes(
        grupo_inimigos,
        jogador,
        grupoBalasJogador.grupo_balas,
        grupoBalasInimigo.grupo_balas,
    )

    if jogador.vida <= 0:
        jogador.set_sprite("assets/ChicoCunhaMorto.png")
        settings.DISPLAY_SURF.fill((255, 255, 255))
        settings.DISPLAY_SURF.blit(jogador.sprite, jogador.rect)
        morto = True

    pygame.display.update()
    FPS.tick(settings.FPS_VALUE)

pygame.quit()
