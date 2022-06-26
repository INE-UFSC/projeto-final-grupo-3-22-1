import pygame 
from pygame.locals import *
from Jogador import Jogador

class InterfaceMorte():
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    def mostrar_tela(self, win):
        win.fill((0, 0, 0))
        pygame.display.set_caption("Chico Cunha está morto. Reflita sobre suas ações.")
        font = pygame.font.Font('freesansbold.ttf', 16)
        text1 = font.render('Chico Cunha está morto.', True, (255, 255, 255), (0, 0, 0))
        text2 = font.render('Reflita sobre suas ações (CTRL+C PARA SAIR)', True, (255, 255, 255), (0, 0, 0))
        win.blit(text1, (100, 0)) 
        win.blit(text2, (100, 30)) 