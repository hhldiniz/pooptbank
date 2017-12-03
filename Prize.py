class Prize:
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor