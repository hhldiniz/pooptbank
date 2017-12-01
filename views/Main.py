from DBController import DBController
from views.Config import Configuration
from views.Signup import Signup
from views.View import View


class Main(View):
    def __init__(self, title="Poopt Bank", size="800x600"):
        View.__init__(self, title, size)
        View.set_btn_callback(self, self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Entrar":
            db_controller = DBController("localhost", "pooptbank", "postgres", "cgch36AA!@")
            username = self.get_app_gui().getEntry("Username")
            password = self.get_app_gui().getEntry("Password")
            data = db_controller.select_data()
            print(data)
        elif btn == "Sair":
            View.get_app_gui(self).stop()
        elif btn == "Cadastrar":
            signup_view = Signup(View.get_app_gui(self))
        elif btn == "Configurar":
            config_view = Configuration(View.get_app_gui(self), btn)
