from .Button import Button
from .Settings import Settings

settings = Settings()

class ToMenuButton(Button):
    def __init__(self, pos_x, pos_y, text_input):
        super().__init__(pos_x, pos_y, text_input)

    def nextStep(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
           and position[1] in range(self.rect.top, self.rect.bottom):
               
            from .MainMenuInterface import MainMenuInterface
            main_menu = MainMenuInterface()
            main_menu.interfaceLoop()
