from views.Modal import ModalWindow


class Signup(ModalWindow):
    def __init__(self, app, title="Poopt Signup"):
        ModalWindow.__init__(self)
        self.__app = app
        self.__title = title
        self.__app.startSubWindow(title, modal=True)
        self.__app.showSubWindow(title)

    def destroy_window(self):
        self.__app.destroySubWindow(self.__title)