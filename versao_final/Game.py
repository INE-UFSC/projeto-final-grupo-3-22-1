import pygame
from pygame.locals import *
import sys

from Settings import Settings
from Globals import Globals

from MainMenuInterface import MainMenuInterface
from PauseMenuInterface import PauseMenuInterface
from GameOverInterface import GameOverInterface

from Jogador import Jogador
from CollisionHandler import CollisionHandler

from ControleArmas import ControleArmas
from ControlePowerUps import ControlePowerUps
from GrupoAtaques import GrupoAtaques

from InimigoBasico import InimigoBasico
from InimigoAtirador import InimigoAtirador
from InimigoRastreador import InimigoRastreador
from InimigoDirecional import InimigoDirecional
from Mapa import Mapa

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

sprites = pygame.sprite.RenderUpdates()

grupo_inimigos_basicos = pygame.sprite.RenderUpdates()
grupo_inimigos_atiradores = pygame.sprite.RenderUpdates()
grupo_inimigos_rastreadores = pygame.sprite.RenderUpdates()
grupo_inimigos_direcionais = pygame.sprite.RenderUpdates()
grupo_inimigos = pygame.sprite.RenderUpdates()

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


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("O mar não está pra gente")
        self.__FPS = pygame.time.Clock()

        self.__jogando = True
        self.__jogador = Jogador(vida=20, velocidade_movimento=8)

        self.__settings = Settings()
        self.__globals = Globals()

        # controladores e grupos
        self.__controleArmas = ControleArmas(self.jogador)
        self.__controlePowerUps = ControlePowerUps(self.jogador)
        self.__grupoAtaquesInimigo = GrupoAtaques()
        self.__grupoAtaquesJogador = GrupoAtaques()

        self.__collisionHandler = CollisionHandler(self.jogador, self.controlePowerUps)

        self.mapa = Mapa('teste', 2, 'teste2')
        self.background_sprites, self.blocks = self.mapa.change_map(["BBBBBBBBBBBBBBBBBBBB","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","B..................B","BBBBBBBBBBBBBBBBBBBB"])
        self.mapa.draw_map([self.background_sprites, self.blocks], self.globals.DISPLAY_SURF)

        @property
        def mapa(self) -> Mapa:
            return self.__mapa

        @property
        def background_sprites(self):
            return self.__background_sprites

        @property 
        def blocks(self):
            return self.__blocks

        sprites.add(self.jogador)

    # getters and setters
    @property
    def FPS(self) -> pygame.time.Clock:
        return self.__FPS

    @property
    def playlist(self) -> list:
        return self.__playlist

    @property
    def jogando(self) -> bool:
        return self.__jogando

    @jogando.setter
    def jogando(self, state: bool):
        self.__jogando = state

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    @property
    def settings(self) -> Settings:
        return self.__settings

    @property
    def globals(self) -> Globals:
        return self.__globals


    @property
    def controleArmas(self) -> ControleArmas:
        return self.__controleArmas

    @property
    def controlePowerUps(self) -> ControlePowerUps:
        return self.__controlePowerUps

    @property
    def grupoAtaquesInimigo(self) -> GrupoAtaques:
        return self.__grupoAtaquesInimigo
    
    @property
    def grupoAtaquesJogador(self) -> GrupoAtaques:
        return self.__grupoAtaquesJogador

    @property
    def collisionHandler(self) -> CollisionHandler:
        return self.__collisionHandler

    def render_screen(self):
        self.globals.DISPLAY_SURF.fill((255, 255, 255))
        self.background_sprites.draw(self.globals.DISPLAY_SURF)
        sprites.draw(self.globals.DISPLAY_SURF)
        self.grupoAtaquesInimigo.desenhar()
        self.grupoAtaquesJogador.desenhar()
        self.blocks.draw(self.globals.DISPLAY_SURF)
        pygame.display.update()

    def jogar(self):
        self.render_screen()
        main_menu = MainMenuInterface()
        main_menu.interfaceLoop()
        
        self.comecar_jogo()

    def comecar_jogo(self):
        while self.jogando:
            if self.jogador.morto:
                self.finalizar_jogo()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():              
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pausar_jogo()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    tiro = self.jogador.atirar(mouse_x, mouse_y)
                    if tiro:
                        self.grupoAtaquesJogador.nova_bala(tiro)

            self.globals.DISPLAY_SURF.fill((255, 255, 255))

            # percorre todos os inimigos atiradores e executa suas funções
            for atirador in grupo_inimigos_atiradores:
                # fazendo o atirador atirar
                ataque_inimigo = atirador.atacar(self.jogador.x, self.jogador.y)
                if ataque_inimigo:
                    self.grupoAtaquesInimigo.nova_bala(ataque_inimigo)

                # achando o caminho do atirador
                x, y = atirador.achar_caminho(self.jogador.x, self.jogador.y, 250)

                # movendo o atirador com os resultados obtidos anteriormente
                atirador.mover(x, y)

            for basico in grupo_inimigos_basicos:
                basico.mover()

            for rastreador in grupo_inimigos_rastreadores:
                # achando o caminho do rastreador
                x, y = rastreador.achar_caminho(self.jogador.x, self.jogador.y)

                # movendo o rastreador com os resultados obtidos
                rastreador.mover(x, y)

            for direcional in grupo_inimigos_direcionais:
                # achando o caminho do corredor
                x, y = direcional.achar_caminho(self.jogador.x, self.jogador.y)

                # movendo o corredor com os resultados obtidos
                direcional.mover(x, y)

            self.jogador.mover()
            self.jogador.mover_arma(mouse_x, mouse_y)

            self.grupoAtaquesJogador.desenhar()
            self.grupoAtaquesInimigo.desenhar()

            self.controlePowerUps.grupo_powerUps.desenhar()
            self.controlePowerUps.verificar_fim_temporarios()

            for entity in sprites:
                self.globals.DISPLAY_SURF.blit(entity.sprite, entity.rect)

            self.collisionHandler.verificar_colisoes(
                grupo_inimigos,
                self.grupoAtaquesJogador.grupo_balas,
                self.grupoAtaquesInimigo.grupo_balas,
                self.controlePowerUps.grupo_powerUps.grupo_todos_caidos,
            )

            self.render_screen()
            self.FPS.tick(self.settings.FPS_VALUE)

    def finalizar_jogo(self):
        game_over = GameOverInterface()
        game_over.interfaceLoop()

    def pausar_jogo(self):
        pausar_jogo = PauseMenuInterface()
        pausar_jogo.interfaceLoop()
