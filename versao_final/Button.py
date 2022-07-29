import pygame
from Settings import Settings
from abc import ABC

settings = Settings()

class Button(ABC):

	def __init__(self, pos_x, pos_y, text_input):
		self.__pos_x = pos_x
		self.__pos_y = pos_y
		self.__text_input = text_input
		self.__button_surface = pygame.image.load(f"assets/button.png")
		self.__image = pygame.transform.scale(self.button_surface, (200, 75))
		self.__rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
		self.__text = settings.main_font.render(self.text_input, True, (255,255,255))
		self.__text_rect = self.text.get_rect(center=(self.pos_x, self.pos_y))

	@property
	def pos_x(self):
		return self.__pos_x

	@property
	def pos_y(self):
		return self.__pos_y

	@property
	def text_input(self):
		return self.__text_input
	
	@property
	def button_surface(self):
		return self.__button_surface

	@property
	def image(self):
		return self.__image

	@property
	def rect(self):
		return self.__rect

	@property
	def text(self):
		return self.__text
	
	@text.setter
	def text(self, text):
		self.__text = text

	@property
	def text_rect(self):
		return self.__text_rect

	def update(self):
		settings.screen.blit(self.image, self.rect)
		settings.screen.blit(self.text, self.text_rect)

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = settings.main_font.render(self.text_input, True, (60,23,82))
		else:
			self.text = settings.main_font.render(self.text_input, True, (255,255,255))
