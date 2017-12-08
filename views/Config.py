from DBController import DBController
from views.SubWindow import SubWindow


class Configuration(SubWindow):
    def __init__(self, app, title):
        self.__app = app
        self.__title = title
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "400x200")
        SubWindow.add_entry(self, "Database Host")
        SubWindow.add_entry(self, "Database Name")
        SubWindow.add_label_secret_field(self, "Database Password")
        SubWindow.add_btn(self, "Confirm")
        SubWindow.set_btn_callback(self, self.confirm_callback)

    def confirm_callback(self, btn):
        db_controller = DBController()
