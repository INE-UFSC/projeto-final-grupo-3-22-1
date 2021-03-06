from Button import Button
from NameInputInterface import NameInputInterface

name_input = NameInputInterface()

class PlayButton(Button):
    def __init__(self, pos_x, pos_y, text_input):
        super().__init__(pos_x, pos_y, text_input)

    def nextStep(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            name_input.interfaceLoop()
