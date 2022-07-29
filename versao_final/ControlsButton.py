from Button import Button
from ControlsInterface import ControlsInterface


class ControlsButton(Button):
    def __init__(self, pos_x, pos_y, text_input):
        super().__init__(pos_x, pos_y, text_input)
        self.__controls = ControlsInterface()

    @property
    def controls(self) -> ControlsInterface:
        return self.__controls

    def nextStep(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.controls.interfaceLoop()
