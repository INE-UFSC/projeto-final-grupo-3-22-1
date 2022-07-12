from Settings import Settings

settings = Settings()

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
<<<<<<< HEAD
		self.text = settings.main_font.render(self.text_input, True, (255,255,255))
=======
		self.text = settings.main_font.render(self.text_input, True, "white")
>>>>>>> eb7b48981a523e7afb062f2e263fb9243c00dfd0
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		settings.screen.blit(self.image, self.rect)
		settings.screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Pressionou!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
<<<<<<< HEAD
			self.text = settings.main_font.render(self.text_input, True, (255,0,255))
		else:
			self.text = settings.main_font.render(self.text_input, True, (255,255,255))
=======
			self.text = settings.main_font.render(self.text_input, True, "purple")
		else:
			self.text = settings.main_font.render(self.text_input, True, "white")
>>>>>>> eb7b48981a523e7afb062f2e263fb9243c00dfd0
