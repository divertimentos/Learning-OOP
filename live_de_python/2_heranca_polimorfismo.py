class Pizza:
    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def comer_pedaco(self):
        self.pedacos -= 1

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

    @staticmethod
    def ingredientes():
        ingredientes = ["molho de tomate", "orégano", "azeitona"]
        return ingredientes

