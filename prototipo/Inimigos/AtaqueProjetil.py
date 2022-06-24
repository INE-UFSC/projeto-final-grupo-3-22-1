from Ataque import Ataque


class AtaqueProjetil(Ataque):
    def __init__(self, dano: int, distancia_maxima: int, velocidade_projetil: int):
        super().__init__(dano)
        self.__distancia_maxima = distancia_maxima
        self.__velocidade_projetil = velocidade_projetil
    
    @property
    def dano(self) -> int:
        return self.__dano
    
    @property
    def distancia_maxima(self) -> int:
        return self.__distancia_maxima
    
    @property
    def velocidade_projetil(self) -> int:
        return self.__velocidade_projetil
    
    def deletar_projetil(self):
        ...