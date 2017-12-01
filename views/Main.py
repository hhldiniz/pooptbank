from DBController import DBController
from views.Config import Configuration
from views.Home import HomeView
from views.Signup import Signup
from views.View import View


class Main(View):
    def __init__(self, title="Poopt Bank", size="800x600"):
        View.__init__(self, title, size)
        View.set_btn_callback(self, self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Entrar":
            db_controller = DBController("localhost", "pooptbank")
            username = self.get_app_gui().getEntry("Username")
            password = self.get_app_gui().getEntry("Password")
            data = db_controller.select_data('users', {'username':username, 'password': password})
            print(data)
            home_view = HomeView(View.get_app_gui(self), "Home")
        elif btn == "Sair":
            View.get_app_gui(self).stop()
        elif btn == "Cadastrar":
            signup_view = Signup(View.get_app_gui(self))
        elif btn == "Configurar":
            config_view = Configuration(View.get_app_gui(self), btn)
