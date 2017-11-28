class BaseUser:
    def __init__(self, name, cpf, address, balance=None):
        self.__name = name
        self.__cpf = cpf
        self.__address = address
        self.__balance = balance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
