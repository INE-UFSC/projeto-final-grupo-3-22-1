import pygame
from MainMenuInterface import MainMenuInterface

pygame.init()
pygame.display.set_caption("O Mar não está pra Gente")

main_menu = MainMenuInterface()

main_menu.interfaceLoop()
