from DBController import DBController
from views.Modal import ModalWindow


class Signup(ModalWindow):
    def __init__(self, app, title="Poopt Signup"):
        self.__app = app
        ModalWindow.__init__(self, app, title)
        ModalWindow.add_label_validation_field(self, "New Username")
        ModalWindow.add_label_secret_field(self, "New Password")
        ModalWindow.set_btn_callback(self, self.btn_callback)
        ModalWindow.add_btn(self, "Finalizar Cadastro")

    def destroy_window(self):
        self.__app.destroySubWindow(self.__title)

    def btn_callback(self, btn):
        if btn == "Finalizar Cadastro":
            new_user = self.__app.getEntry("New Username")
            new_password = self.__app.getEntry("New Password")
            db_controller = DBController("localhost", "pooptbank", "postgres", "cgch36AA!@")
            db_controller.insert_data("user", "username,password", f"'{new_user}','{new_password}'")
