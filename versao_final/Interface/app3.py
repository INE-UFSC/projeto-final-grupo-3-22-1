import pygame
import sys
import numpy
from Button import Button
from Settings import Settings
from MainMenu import MainMenu

pygame.init()
pygame.display.set_caption("O Mar não está pra Gente")

settings = Settings()

settings.FPS_VALUE = 20
FPS = pygame.time.Clock()
settings.largura_tela = 1280
settings.altura_tela = 720
settings.main_font = pygame.font.Font(f"Interface/alterebro-pixel-font.ttf", 50)
settings.screen = pygame.display.set_mode((settings.largura_tela, 
				settings.altura_tela))
settings.menu_background = pygame.image.load(f'Interface/background.png')

button_surface = pygame.image.load(f"Interface/button.png")
button_surface = pygame.transform.scale(button_surface, (200, 75))

button = Button(button_surface, 665, 220, "Jogar")
button2 = Button(button_surface, 665, 320, "Opções")
button3 = Button(button_surface, 665, 420, "Controles")
button4 = Button(button_surface, 665, 520, "Ranking")
button5 = Button(button_surface, 665, 620, "Sair")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())
			button2.checkForInput(pygame.mouse.get_pos())
			button3.checkForInput(pygame.mouse.get_pos())
			button4.checkForInput(pygame.mouse.get_pos())
			button5.checkForInput(pygame.mouse.get_pos())

	settings.screen.blit(settings.menu_background, (0,0))

	button.update()
	button.changeColor(pygame.mouse.get_pos())
	button2.update()
	button2.changeColor(pygame.mouse.get_pos())
	button3.update()
	button3.changeColor(pygame.mouse.get_pos())
	button4.update()
	button4.changeColor(pygame.mouse.get_pos())
	button5.update()
	button5.changeColor(pygame.mouse.get_pos())

	pygame.display.update()
