class Ataque:
    def __init__(self, dano: int):
        self.__dano = dano
    
    @property
    def dano(self) -> int:
        return self.__dano