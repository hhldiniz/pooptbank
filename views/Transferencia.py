from views.SubWindow import SubWindow


class TransferenciasView(SubWindow):
    def __init__(self, app, title, all_users, current_user):
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "500x400")
        SubWindow.add_label(self, "Transferencias")

        # so vai aprecer se usuario for professor
        SubWindow.add_option_box(self, "De Aluno", [current_user])

        SubWindow.add_option_box(self, "Para Aluno", all_users)

        SubWindow.add_entry(self, "Valor")

        SubWindow.add_btns(self, ["Efetivar Transferencia", "Sair das Transferencias"], self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Sair das Transferencias":
            SubWindow.hide(self, "Transferencias")
        if btn == "Efetivar Transferencia":
            print("logica para Efetivar Transferencia")