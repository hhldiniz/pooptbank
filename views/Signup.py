from DBController import DBController
from views.SubWindow import SubWindow


class Signup(SubWindow):
    def __init__(self, app, title="Poopt Signup"):
        self.__app = app
        self.__title = title
        SubWindow.__init__(self, app, title)
        SubWindow.add_label_validation_field(self, "New Username")
        SubWindow.add_label_secret_field(self, "New Password")
        SubWindow.set_btn_callback(self, self.btn_callback)
        SubWindow.add_btn(self, "Finalizar Cadastro")
        SubWindow.add_btn(self, "Cancelar Cadastro")

    def destroy_window(self):
        self.__app.destroySubWindow(self.__title)

    def btn_callback(self, btn):
        if btn == "Finalizar Cadastro":
            new_user = self.__app.getEntry("New Username")
            new_password = self.__app.getEntry("New Password")
            db_controller = DBController("localhost", "pooptbank", "postgres", "cgch36AA!@")
            print(db_controller.insert_data("user", "username,password", f"'{new_user}','{new_password}'"))
        elif btn == "Cancelar Cadastro":
            self.destroy_window()
