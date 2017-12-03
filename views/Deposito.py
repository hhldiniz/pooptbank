from views.SubWindow import SubWindow

# essa tela é vista somento pelo professor


class DepositoView(SubWindow):
    def __init__(self, app, title):
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "500x400")
        SubWindow.add_label(self, "Deposito")

        SubWindow.add_option_box(self, "Aluno a Receber Deposito", ["Hugo", "Romulo"])

        SubWindow.add_entry(self, "Valor Do Deposito")

        SubWindow.add_btns(self, ["Efetivar Deposito", "Sair de Deposito"], self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Sair de Deposito":
            SubWindow.hide(self, "Deposito")
        if btn == "Efetivar Deposito":
            print("logica para Efetivar Deposito")