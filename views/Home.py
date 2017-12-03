from views.SubWindow import SubWindow
from views.Historico import HistoricoView


class HomeView(SubWindow):
    def __init__(self, app, title):
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "500x400")
        SubWindow.add_label(self, "Bem vindo, Hugo.")
        SubWindow.add_btns(self, ["Historico", "Trocas", "Transferencias", "Deposito", "Logout"], self.__btn_callback)
        SubWindow.add_label(self, "Seu saldo é 0")
        SubWindow.add_label(self, "Sua ultima transação foi ...")

    def __btn_callback(self, btn):
        if btn == "Historico":
            HistoricoView(SubWindow.get_app_gui(self), "Historico")