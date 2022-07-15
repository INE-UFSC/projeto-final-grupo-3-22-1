import pygame
from pygame.locals import *
from Settings import Settings
import os

from Mapa import Mapa
from CollisionHandler import CollisionHandler
from ControleArmas import ControleArmas
from GrupoBalasJogador import GrupoBalasJogador
from ControleInimigo import ControladorInimigo
from ControleJogador import ControleJogador
from Jogador import Jogador
from InimigoAtirador import InimigoAtirador
from Inimigo import Inimigo
from Bloco import Bloco
from SpritesFlyweight import SpritesFlyweight
from GrupoBalasInimigo import GrupoBalasInimigo

tilemap = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B..................B",
    "B..................B",
    "B............B.....B",
    "B............B.....B",
    "B............B.....B",
    "B............B.....B",
    "B............B.....B",
    "B............B.....B",
    "B..B.........B.....B",
    "B..B.....J...B.....B",
    "B..B.........B.....B",
    "B..B.........B.....B",
    "B..B...............B",
    "B..B...............B",
    "B..B...............B",
    "B..B...............B",
    "B..B...............B",
    "B..................B",
    "BBBBBBBBBBBBBBBBBBBB",
]

class Jogo(pygame.sprite.Sprite):
    def __init__(self):
        #inicializando configurações do jogo
        pygame.init()
        pygame.display.set_caption("Game")
        self.rodando = True
        self.settings = Settings()
        self.FPS = pygame.time.Clock()
        self.settings.FPS_VALUE = 20
        self.settings.largura_tela = 640
        self.settings.altura_tela = 640
        self.settings.DISPLAY_SURF = pygame.display.set_mode((self.settings.largura_tela, self.settings.altura_tela))

        #inicializando entidades e controladores
        self.controleInimigo = ControladorInimigo()
        self.jogador = Jogador(vida=20, velocidade_movimento=8)
        self.lista_inimigos = [InimigoAtirador(405, 250, 5, 20, os.path.join(os.path.dirname(__file__), "assets" ,"lulaAtiradora.png"), 6)]
        self.controleArmas = ControleArmas(self.jogador)
        self.controleJogador = ControleJogador(self.jogador)
        self.grupoBalasJogador = GrupoBalasJogador()
        self.grupoBalasInimigo = GrupoBalasInimigo()
        self.collisionHandler = CollisionHandler()

        #inicializando sprites e grupos
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador)
        self.grupo_inimigos = pygame.sprite.Group()

        #inicializando as sprites a serem utilizadas no jogo
        self.caixaSprite = SpritesFlyweight(os.path.join(
        "versao_final/assets", "caixa1.png"))

        #adiciona os inimigos ao grupo de sprites de inimigos
        for inimigo in self.lista_inimigos:
            self.grupo_inimigos.add(inimigo)
            self.sprites.add(inimigo)
    
    def iniciar_nova_rodada(self):
        self.mudar_mapa(tilemap)

    def rodar_jogo(self):
        while self.rodando:
            self.verificar_eventos()
            self.desenhar_tela()
            self.atualizar()
    
    def desenhar_tela(self):
        self.settings.DISPLAY_SURF.fill((0, 255, 255))
        #self.sprites.draw(self.settings.DISPLAY_SURF)
        for entity in self.sprites:
            self.settings.DISPLAY_SURF.blit(entity.sprite, entity.rect)
        self.grupoBalasJogador.desenhar()
        pygame.display.update()
        self.FPS.tick(self.settings.FPS_VALUE)

    def atualizar(self):
            # percorre todos os inimigos atiradores e executa suas funções
        for atirador in self.lista_inimigos:
            # fazendo o atirador atirar
            tiro_inimigo = atirador.atacar(self.jogador.x, self.jogador.y)
            if tiro_inimigo:
                self.grupoBalasInimigo.nova_bala(tiro_inimigo)

            # achando o caminho do atirador
            x, y = atirador.achar_caminho(self.jogador.x, self.jogador.y, 250)

            # movendo o atirador com os resultados obtidos anteriormente
            atirador.mover(x, y)
        if tiro_inimigo:
            self.grupoBalasInimigo.nova_bala(tiro_inimigo)
        ##Inimigo.mover()
        self.jogador.mover()
        
        self.sprites.update()

    def verificar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tiro = self.jogador.atirar(mouse_x, mouse_y)
                self.jogador.mover_arma(mouse_x, mouse_y)
                if tiro:
                    self.grupoBalasJogador.nova_bala(tiro)
        self.collisionHandler.verificar_colisoes(
        self.grupo_inimigos, self.jogador, self.grupoBalasJogador.grupo_balas, self.grupoBalasInimigo.grupo_balas)


    def pausar(self):
        ...
    
    def mudar_mapa(self, tilemap:list):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    block = Bloco(j, i, self.caixaSprite.spriteAddress)
                    self.sprites.add(block)
                if column == "J":
                    pass
    
    def encerrar_jogo(self):
        ...