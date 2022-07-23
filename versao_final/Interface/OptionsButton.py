from .Button import Button
from .OptionsInterface import OptionsInterface


class OptionsButton(Button):
    def __init__(self, pos_x, pos_y, text_input):
        super().__init__(pos_x, pos_y, text_input)
        self.__options = OptionsInterface()
    
    @property
    def options(self) -> OptionsInterface:
        return self.__options
        
    def nextStep(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
            and position[1] in range(self.rect.top, self.rect.bottom):
            self.options.interfaceLoop()
