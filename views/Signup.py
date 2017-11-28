from views.Modal import ModalWindow


class Signup(ModalWindow):
    def __init__(self, app, title="Poopt Signup"):
        ModalWindow.__init__(self, app, title)
        app.addValidationEntry("New Username")
        app.addSecretLabelEntry("New Password")

    def destroy_window(self):
        self.__app.destroySubWindow(self.__title)