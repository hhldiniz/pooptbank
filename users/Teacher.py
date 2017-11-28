from users.BaseUser import BaseUser


class Teacher(BaseUser):
    def __init__(self, name, cpf, address):
        BaseUser.__init__(self, name, cpf, address)
