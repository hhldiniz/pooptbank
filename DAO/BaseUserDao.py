class BaseUser:
    def __init__(self, username, cpf, address, password, balance=0):
        self.__username = username
        self.__cpf = cpf
        self.__address = address
        self.__balance = balance
        self.__password = password

    def get_name(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_name(self, username):
        self.__username = username

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def save(self):
        pass
