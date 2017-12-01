from views.SubWindow import SubWindow


class HomeView(SubWindow):
    def __init__(self, app, title):
        SubWindow.__init__(self, app, title)
        SubWindow.add_btn(self, "Saldo")
        SubWindow.add_btn(self, "Historico")
        SubWindow.add_btn(self, "Premios")
        SubWindow.add_btn(self, "Transferencia")
        SubWindow.add_btn(self, "Deposito")
        SubWindow.add_separator(self, "vertical", 1, 2)
