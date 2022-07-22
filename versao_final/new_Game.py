import pygame
from pygame.locals import *
import sys

from Settings import Settings
from Globals import Globals

from Jogador import Jogador
from CollisionHandler import CollisionHandler

from ControleJogador import ControleJogador
from ControleArmas import ControleArmas
from ControlePowerUps import ControlePowerUps
from GrupoBalasJogador import GrupoBalasJogador
from GrupoBalasInimigo import GrupoBalasInimigo

# TODO: remover e substituir pelas classes comentadas em jogar()
# código procedural para testes
from InimigoBasico import InimigoBasico
from InimigoAtirador import InimigoAtirador
from InimigoRastreador import InimigoRastreador
from InimigoDirecional import InimigoDirecional

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

sprites = pygame.sprite.Group()

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


class new_Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("O mar não está pra gente")
        self.__FPS = pygame.time.Clock()

        self.__jogando = True
        self.__jogador = Jogador(vida=20, velocidade_movimento=8)

        self.__settings = Settings()
        self.__globals = Globals()

        # controladores e grupos
        self.__controleJogador = ControleJogador(self.jogador)
        self.__controleArmas = ControleArmas(self.jogador)
        self.__controlePowerUps = ControlePowerUps(self.jogador)
        self.__grupoBalasJogador = GrupoBalasJogador()
        self.__grupoBalasInimigo = GrupoBalasInimigo()

        self.__collisionHandler = CollisionHandler()

        # ! início seção transitória; remover após implementação
        # TODO: remover essa seção de código (implementação transitória)
        sprites.add(self.jogador)
        # ! fim seção transitória

    # getters and setters
    @property
    def FPS(self) -> pygame.time.Clock:
        return self.__FPS

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
    def controleJogador(self) -> ControleJogador:
        return self.__controleJogador

    @property
    def controleArmas(self) -> ControleArmas:
        return self.__controleArmas

    @property
    def controlePowerUps(self) -> ControlePowerUps:
        return self.__controlePowerUps

    @property
    def grupoBalasJogador(self) -> GrupoBalasJogador:
        return self.__grupoBalasJogador

    @property
    def grupoBalasInimigo(self) -> GrupoBalasInimigo:
        return self.__grupoBalasInimigo

    @property
    def collisionHandler(self) -> CollisionHandler:
        return self.__collisionHandler

    def jogar(self):
        # TODO: chamar os menus primeiro

        while self.jogando:
            if self.jogador.morto:
                # TODO: trocar por tela de fim de jogo
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.jogando = False
                continue

            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    tiro = self.jogador.atirar(mouse_x, mouse_y)
                    if tiro:
                        self.grupoBalasJogador.nova_bala(tiro)

            # ! inicio seção transitória
            # TODO: implementar mapa; substituir por função de renderizar o mapa
            # fundo de tela branco
            self.globals.DISPLAY_SURF.fill((255, 255, 255))

            # TODO: implementar controleInimigos
            # percorre todos os inimigos atiradores e executa suas funções
            for atirador in grupo_inimigos_atiradores:
                # fazendo o atirador atirar
                ataque_inimigo = atirador.atacar(self.jogador.x, self.jogador.y)
                if ataque_inimigo:
                    self.grupoBalasInimigo.nova_bala(ataque_inimigo)

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
            # ! fim seção transitória

            self.jogador.mover()
            self.jogador.mover_arma(mouse_x, mouse_y)

            self.grupoBalasJogador.desenhar()
            self.grupoBalasInimigo.desenhar()

            self.controlePowerUps.grupo_powerUps.desenhar()
            self.controlePowerUps.verificar_fim_temporarios()

            for entity in sprites:
                self.globals.DISPLAY_SURF.blit(entity.sprite, entity.rect)

            self.collisionHandler.verificar_colisoes(
                grupo_inimigos,  # TODO: trocar pela implementação feita para o grupo de inimigos
                self.jogador,
                self.grupoBalasJogador.grupo_balas,
                self.grupoBalasInimigo.grupo_balas,
                self.controlePowerUps.grupo_powerUps.grupo_todos_caidos,
            )

            pygame.display.update()
            self.FPS.tick(self.settings.FPS_VALUE)
