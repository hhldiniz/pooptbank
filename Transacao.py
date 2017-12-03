class Transacao:
    def __init__(self, data, descricao, valor):
        self.__data = data
        self.__descricao = descricao
        self.__valor = valor

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor