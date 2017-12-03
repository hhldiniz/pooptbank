from DBController import DBController
from views.Config import Configuration
from views.Home import HomeView
from views.Signup import Signup
from views.View import View


class Main(View):
    def __init__(self, title="Poopt Bank", size="500x400"):
        View.__init__(self, title, size)
        View.set_btn_callback(self, self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Entrar":
            db_controller = DBController("localhost", "pooptbank")
            username = self.get_app_gui().getEntry("Username")
            password = self.get_app_gui().getEntry("Password")
            data = db_controller.select_data_single('users', {'username': username, 'password': password})
            if data is not None and data['username'] == username and data['password'] == password:
                homeView = HomeView(View.get_app_gui(self), "Home")
                homeView.show("Home")
        elif btn == "Sair":
            View.get_app_gui(self).stop()
        elif btn == "Cadastrar":
            Signup(View.get_app_gui(self))
        elif btn == "Configurar":
            Configuration(View.get_app_gui(self), btn)
