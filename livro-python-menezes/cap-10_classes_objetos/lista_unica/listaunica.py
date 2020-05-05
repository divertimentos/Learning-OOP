class ListaUnica:
    def __init__(self, elem_class):
        self.list = list()
        self.elem_class = elem_class
    def __len__(self):
        return len(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getitem__(self, p):
        return self.lista[p]
    
    def indice_valido(self, i):
        return i > 0 and i < len(self.lista)
    
    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)
    def remove(self, elem):
        self.lista.remove(elem)
    def pesquisa