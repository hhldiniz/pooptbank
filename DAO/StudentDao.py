from DAO.BaseUserDao import BaseUser
from DBController import DBController


class Student(BaseUser):
    def __init__(self, username, cpf, address, password):
        BaseUser.__init__(self, username, cpf, address, password)

    def save(self):
        try:
            db_controller = DBController()
            address = BaseUser.get_address(self)
            query = db_controller.insert_data('users',{'username': BaseUser.get_name(self), 'password': BaseUser.get_password(self),
                                               'address': address.get_street(), 'cpf': BaseUser.get_cpf(self),
                                               'admin': False,'balance': 0})
            if query is None:
                return False
            else:
                return True
        except:
            return False
