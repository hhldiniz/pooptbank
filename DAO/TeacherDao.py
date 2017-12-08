from DAO.BaseUserDao import BaseUser


class Teacher(BaseUser):
    def __init__(self, username, cpf, address):
        BaseUser.__init__(self, username, cpf, address)
