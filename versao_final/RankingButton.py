from Button import Button
from RankingInterface import RankingInterface


class RankingButton(Button):
    def __init__(self, pos_x, pos_y, text_input):
        super().__init__(pos_x, pos_y, text_input)
        self.__ranking = RankingInterface()

    @property
    def ranking(self) -> RankingInterface:
        return self.__ranking

    def nextStep(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.ranking.interfaceLoop()
