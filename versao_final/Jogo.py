import pygame
from pygame.locals import *
from Settings import Settings
import os

from Mapa import Mapa
from CollisionHandler import CollisionHandler
from ControleArmas import ControleArmas
from ControleBalasJogador import ControleBalasJogador
from ControleInimigo import ControladorInimigo
from ControleJogador import ControleJogador
from Jogador import Jogador
from InimigoAtirador import InimigoAtirador
from Inimigo import Inimigo


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
        self.lista_inimigos = [InimigoAtirador(405, 250, 5, 20, os.path.join(
        "versao_final/assets", "lulaAtiradora.png"))]
        self.controleArmas = ControleArmas(self.jogador)
        self.controleJogador = ControleJogador(self.jogador)
        self.controleBalasJogador = ControleBalasJogador()
        self.collisionHandler = CollisionHandler()

        #inicializando sprites e grupos
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador)
        self.grupo_inimigos = pygame.sprite.Group()

        #adiciona os inimigos ao grupo de sprites de inimigos
        for inimigo in self.lista_inimigos:
            self.grupo_inimigos.add(inimigo)
            self.sprites.add(inimigo)
    
    def rodar_jogo(self):
        while self.rodando:
            self.verificar_eventos()
            self.desenhar_tela()
            self.atualizar()
    
    def desenhar_tela(self):
        self.settings.DISPLAY_SURF.fill((255, 255, 255))
        self.sprites.draw(self.settings.DISPLAY_SURF)
        for entity in self.sprites:
            self.settings.DISPLAY_SURF.blit(entity.sprite, entity.rect)
        self.controleBalasJogador.desenhar()
        pygame.display.update()
        self.FPS.tick(self.settings.FPS_VALUE)

    def atualizar(self):
        self.jogador.mover()
        x, y = self.controleInimigo.caminho_atirador(
        self.lista_inimigos[0], self.jogador.x, self.jogador.y, 250)

        tiro_inimigo = Inimigo.atacar(self, x, y)
        if tiro_inimigo:
            self.controleBalasJogador.nova_bala(tiro_inimigo)
        ##Inimigo.mover()
        self.sprites.update()

    def verificar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tiro = self.jogador.atirar(mouse_x, mouse_y)
                if tiro:
                    self.controleBalasJogador.nova_bala(tiro)
        self.collisionHandler.verificar_colisoes(
        self.grupo_inimigos, self.jogador, self.controleBalasJogador.grupo_balas)


    def pausar(self):
        ...
    
    def mudar_mapa(self, mapa: Mapa):
        ...
    
    def encerrar_jogo(self):
        ...