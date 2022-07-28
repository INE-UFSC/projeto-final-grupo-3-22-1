import os
import pygame
from Singleton import Singleton

pygame.init()  # necessário para abrir a fonte

# classe usada para guardar variáveis de acesso global e de configuração
class Settings(Singleton):
    FPS_VALUE = 20

    largura_tela = 640
    altura_tela = 640

    largura_tela_interface = 1280
    altura_tela_interface = 720

    main_font = pygame.font.Font(os.path.join("fonts", "alterebro-pixel-font.ttf"), 50)
    screen = pygame.display.set_mode((largura_tela_interface, altura_tela_interface))
