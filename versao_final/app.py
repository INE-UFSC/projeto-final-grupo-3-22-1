from ControleBalasInimigo import ControleBalasInimigo
import pygame
from pygame.locals import *
import sys
import random as rd
import numpy as np
from ControleArmas import ControleArmas

from ControleInimigo import ControladorInimigo
from ControleJogador import ControleJogador

from Jogador import Jogador
from InimigoBasico import InimigoBasico
from Arma import Arma
from InimigoRastreador import InimigoRastreador
from InimigoAtirador import InimigoAtirador

from ControleBalasJogador import ControleBalasJogador
from ControleBalasInimigo import ControleBalasInimigo
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
    InimigoBasico(350, 350, 15, 2, "assets/tilapia.png"),
    InimigoBasico(200, 470, 15, 2, "assets/bacalhau_radioativo.png"),
    InimigoBasico(120, 330, 15, 2, "assets/tilapia.png"),
    InimigoBasico(370, 100, 15, 2, "assets/tilapia.png"),
]

inimigos_atiradores = [
    InimigoAtirador(405, 250, 1, 20, "assets/lulaAtiradora.png", 6),
    InimigoAtirador(200, 230, 1, 20, "assets/lulaAtiradora.png", 6)
]

inimigos_rastreadores = [
    InimigoRastreador(330, 100, 3, 1, "assets/cobraD'agua.png"),
    InimigoRastreador(380, 120, 3, 1, "assets/cobraD'agua.png")
]



jogador = Jogador(vida=20, velocidade_movimento=8)
# controleArmas.trocar_arma("rede")

controleInimigo = ControladorInimigo()
controleArmas = ControleArmas(jogador)
controleJogador = ControleJogador(jogador)
controleBalasJogador = ControleBalasJogador()
controleBalasInimigo = ControleBalasInimigo()
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

    for atirador in grupo_inimigos_atiradores:
        # fazendo o atirador atirar
        tiro_inimigo = atirador.atacar(jogador.x, jogador.y)
        if tiro_inimigo:
            controleBalasInimigo.nova_bala(tiro_inimigo)
        
        # achando o caminho do atirador
        x, y = controleInimigo.caminho_atirador(
            atirador, jogador.x, jogador.y, 250
        )

        # movendo o atirador com os resultados obtidos anteriormente
        atirador.mover(x, y)


    for basico in grupo_inimigos_basicos:
        basico.mover()

    for rastreador in grupo_inimigos_rastreadores:
        # achando o caminho do rastreador
        x, y = controleInimigo.caminho_rastreador(rastreador, jogador.x, jogador.y)
        
        # movendo o rastreador com os resultados obtidos
        rastreador.mover(x, y)

    jogador.mover()

    controleBalasJogador.desenhar()
    controleBalasInimigo.desenhar()
    for entity in sprites:
        settings.DISPLAY_SURF.blit(entity.sprite, entity.rect)

    collisionHandler.verificar_colisoes(
        grupo_inimigos, jogador, controleBalasJogador.grupo_balas, controleBalasInimigo.grupo_balas
    )

    if jogador.vida <= 0:
        jogador.set_sprite("assets/ChicoCunhaMorto.png")
        settings.DISPLAY_SURF.fill((255, 255, 255))
        settings.DISPLAY_SURF.blit(jogador.sprite, jogador.rect)
        morto = True

    pygame.display.update()
    FPS.tick(settings.FPS_VALUE)
