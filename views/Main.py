from DBController import DBController
from views.Config import Configuration
from views.Error import ErrorView
from views.Home import HomeView
from views.Signup import Signup
from views.View import View


class Main(View):
    def __init__(self, title="Poopt Bank", size="500x400"):
        View.__init__(self, title, size)
        View.set_btn_callback(self, self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Entrar":
            # db_controller = DBController(host="ds133856.mlab.com", port=33856, db_name="pooptbank", db_user="manager",
            #                              db_pass="pooptmaster")
            db_controller = DBController(host="localhost", port=27017, db_name="pooptbank", db_user="",
                                         db_pass="")
            username = self.get_app_gui().getEntry("Username")
            password = self.get_app_gui().getEntry("Password")
            data = db_controller.select_data_single('users', {'username': username, 'password': password})
            if data is not None and data['username'] == username and data['password'] == password:
                home_view = HomeView(View.get_app_gui(self), "Home", data['username'], str(data['balance']))
                home_view.show("Home")
            else:
                error_view = ErrorView(View.get_app_gui(self), "Erro")
                error_view.show("Erro")
        elif btn == "Sair":
            View.get_app_gui(self).stop()
        elif btn == "Cadastrar":
                signup_view = Signup(View.get_app_gui(self), btn)
                signup_view.show(btn)
        elif btn == "Configurar":
            config_view = Configuration(View.get_app_gui(self), btn)
            config_view.show(btn)
