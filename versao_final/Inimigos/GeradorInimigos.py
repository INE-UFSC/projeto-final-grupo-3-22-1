class GeradorInimigos:
    def __init__(self, mapa: str):
        self.__mapa = mapa
    
    @property
    def mapa(self) -> str:
        return self.__mapa
    
    def gerar_inimigo_comum(self):
        ...
        
    def gerar_boss(self):
        ...