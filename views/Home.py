from views.SubWindow import SubWindow
from views.Historico import HistoricoView
from views.Trocas import TrocasView
from views.Transferencia import TransferenciasView


class HomeView(SubWindow):
    def __init__(self, app, title):
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "500x400")
        SubWindow.add_label(self, "Bem vindo, Hugo.")
        SubWindow.add_btns(self, ["Historico", "Trocas", "Transferencias", "Deposito", "Logout"], self.__btn_callback)
        SubWindow.add_label(self, "Seu saldo é 0")
        SubWindow.add_label(self, "Sua ultima transação foi ...")

        self.historicoView = HistoricoView(SubWindow.get_app_gui(self), "Historico")
        self.trocasView = TrocasView(SubWindow.get_app_gui(self), "Trocas")
        self.transferenciasView = TransferenciasView(SubWindow.get_app_gui(self), "Transferencias")

    def __btn_callback(self, btn):
        if btn == "Historico":
            self.historicoView.show("Historico")
        if btn == "Trocas":
            self.trocasView.show("Trocas")
        if btn == "Transferencias":
            self.transferenciasView.show("Transferencias")
        # if btn == "Deposito":
        #     HomeView(SubWindow.get_app_gui(self), "Deposito")
        if btn == "Logout":
            SubWindow.get_app_gui(self).stop()