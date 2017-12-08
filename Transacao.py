from DBController import DBController

class Transacao:
    def __init__(self, data, descricao, valor, user1, user2):
        self.__data = data
        self.__descricao = descricao
        self.__valor = valor
        self.__user1 = user1
        self.__user2 = user2

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

    def execute(self):
        try:
            db_controller = DBController()
            user1_balance = db_controller.select_data_single("users", {"username": self.__user1})['balance']
            user2_balance = db_controller.select_data_single("users",  {"username": self.__user2})['balance']
            db_controller.update_data("users", {'username':self.__user1}, {'balance': user1_balance - self.get_valor()})
            db_controller.update_data("users", {'username': self.__user2}, {'balance': user2_balance + self.get_valor()})
            return True
        except:
            return False
