from users.BaseUser import BaseUser


class Student(BaseUser):
    def __init__(self, name, cpf, address, balance):
        BaseUser.__init__(self, name, cpf, address, balance)
