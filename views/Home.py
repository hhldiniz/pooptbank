from DBController import DBController
from views.Deposito import DepositoView
from views.Historico import HistoricoView
from views.SubWindow import SubWindow
from views.Transferencia import TransferenciasView
from views.Trocas import TrocasView


class HomeView(SubWindow):
    def __init__(self, app, title, user, balance):
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "500x400")
        SubWindow.add_label(self, "Bem vindo,"+user+" .")
        SubWindow.add_btns(self, ["Historico", "Trocas", "Transferencias", "Deposito", "Logout"], self.__btn_callback)
        SubWindow.add_label(self, "Seu saldo é "+balance)
        SubWindow.add_label(self, "Sua ultima transação foi ...")
        db_controller = DBController()
        all_users = db_controller.select_data("users")
        all_users_array = []
        for obj in all_users:
            all_users_array.append(obj['username'])
        self.historicoView = HistoricoView(SubWindow.get_app_gui(self), "Historico")
        self.trocasView = TrocasView(SubWindow.get_app_gui(self), "Trocas")
        self.transferenciasView = TransferenciasView(SubWindow.get_app_gui(self), "Transferencias",
                                                     all_users_array, user)
        self.depositoView = DepositoView(SubWindow.get_app_gui(self), "Deposito")

    def __btn_callback(self, btn):
        if btn == "Historico":
            self.historicoView.show(btn)
        if btn == "Trocas":
            self.trocasView.show(btn)
        if btn == "Transferencias":
            self.transferenciasView.show(btn)
        if btn == "Deposito":
            self.transferenciasView.show(btn)
        if btn == "Logout":
            SubWindow.get_app_gui(self).stop()