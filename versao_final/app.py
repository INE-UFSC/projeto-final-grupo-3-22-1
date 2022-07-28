import pygame
from pygame.locals import *
import sys

from Jogador import Jogador
from InimigoBasico import InimigoBasico
from InimigoRastreador import InimigoRastreador
from InimigoAtirador import InimigoAtirador
from InimigoDirecional import InimigoDirecional
from Boss import Boss

from ControleArmas import ControleArmas
from ControleJogador import ControleJogador
from GrupoBalasJogador import GrupoBalasJogador
from GrupoBalasInimigo import GrupoBalasInimigo
from CollisionHandler import CollisionHandler
from ControlePowerUps import ControlePowerUps

from Settings import Settings
from Globals import Globals

#######################################
# parte do pygame (ficara no app.py)
pygame.init()
settings = Settings()
globals = Globals()

FPS = pygame.time.Clock()

# tela
globals.DISPLAY_SURF.fill((255, 255, 255))
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
    InimigoRastreador(330, 100, 3, 1, "assets/cobra.png"),
    InimigoRastreador(380, 120, 3, 1, "assets/cobra-esticada.png"),
]

inimigos_direcionais = [InimigoDirecional(610, 50, 10, 10, "assets/peixe_espada.png")]

# TESTE BOSS
# boss = Boss(400, 400, 5, 20, "assets/ChicoCunha.png", 6, 500)

jogador = Jogador(vida=20, velocidade_movimento=8)

controleArmas = ControleArmas(jogador)
controleArmas.trocar_arma("arpao")

controleArmas = ControleArmas(jogador)
controleJogador = ControleJogador(jogador)
grupoBalasJogador = GrupoBalasJogador()
grupoBalasInimigo = GrupoBalasInimigo()
controle_powerUps = ControlePowerUps(jogador)
collisionHandler = CollisionHandler(jogador, controle_powerUps)

controle_powerUps.spawn_powerUp("pureza", 100, 100)
controle_powerUps.spawn_powerUp("tresVidas", 200, 100)


sprites = pygame.sprite.Group()
sprites.add(jogador)

grupo_inimigos_basicos = pygame.sprite.Group()
grupo_inimigos_atiradores = pygame.sprite.Group()
grupo_inimigos_rastreadores = pygame.sprite.Group()
grupo_inimigos_direcionais = pygame.sprite.Group()
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

for inimigo in inimigos_direcionais:
    grupo_inimigos_direcionais.add(inimigo)
    sprites.add(inimigo)
    grupo_inimigos.add(inimigo)

# TESTE BOSS
# grupo_inimigos.add(boss)
# sprites.add(boss)

#######################################

jogando = True
while jogando:
    if jogador.morto:
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
    globals.DISPLAY_SURF.fill((255, 255, 255))

    # percorre todos os inimigos atiradores e executa suas funções
    for atirador in grupo_inimigos_atiradores:
        # fazendo o atirador atirar
        ataque_inimigo = atirador.atacar(jogador.x, jogador.y)
        if ataque_inimigo:
            grupoBalasInimigo.nova_bala(ataque_inimigo)

        # achando o caminho do atirador
        x, y = atirador.achar_caminho(jogador.x, jogador.y, 250)

        # movendo o atirador com os resultados obtidos anteriormente
        atirador.mover(x, y)

    for basico in grupo_inimigos_basicos:
        basico.mover()

    for rastreador in grupo_inimigos_rastreadores:
        # achando o caminho do rastreador
        x, y = rastreador.achar_caminho(jogador.x, jogador.y)

        # movendo o rastreador com os resultados obtidos
        rastreador.mover(x, y)

    for direcional in grupo_inimigos_direcionais:
        # achando o caminho do corredor
        x, y = direcional.achar_caminho(jogador.x, jogador.y)

        # movendo o corredor com os resultados obtidos
        direcional.mover(x, y)
    
    # TESTE BOSS
    # boss.mover()

    jogador.mover()
    jogador.mover_arma(mouse_x, mouse_y)

    grupoBalasJogador.desenhar()
    grupoBalasInimigo.desenhar()

    controle_powerUps.grupo_powerUps.desenhar()
    controle_powerUps.verificar_fim_temporarios()

    for entity in sprites:
        globals.DISPLAY_SURF.blit(entity.sprite, entity.rect)

    collisionHandler.verificar_colisoes(
        grupo_inimigos,
        grupoBalasJogador.grupo_balas,
        grupoBalasInimigo.grupo_balas,
        controle_powerUps.grupo_powerUps.grupo_todos_caidos,
    )

    pygame.display.update()
    FPS.tick(settings.FPS_VALUE)

pygame.quit()
sys.exit()
