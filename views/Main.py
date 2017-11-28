from DBController import DBController
from views.Signup import Signup
from views.View import View


class Main(View):
    def __init__(self, title="Poopt Bank", size="800x600"):
        View.__init__(self, title, size)
        View.set_btn_callback(self, self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Entrar":
            db_controller = DBController("localhost", "poopt", "postgres", "cgch36AA")
            data = db_controller.select_data("user", "username,password")
        elif btn == "Sair":
            View.get_app_gui(self).stop()
        elif btn == "Cadastrar":
            signup_view = Signup(View.get_app_gui(self))

