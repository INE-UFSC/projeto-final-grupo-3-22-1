import os
import pygame
from .Singleton import Singleton

pygame.init()  # necessário para abrir a fonte

# classe usada para guardar variáveis de acesso global e de configuração
class Settings(Singleton):
    largura_tela = 1280
    altura_tela = 720

    main_font = pygame.font.Font(os.path.join("Interface", "alterebro-pixel-font.ttf"), 50)
    screen = pygame.display.set_mode((largura_tela, altura_tela))
