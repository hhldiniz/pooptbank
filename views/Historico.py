from views.SubWindow import SubWindow
from Transacao import Transacao


class HistoricoView(SubWindow):
    def __init__(self, app, title):
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "500x400")
        SubWindow.add_label(self, "Historico de Transacoes")

        # so vai aprecer se usuario for professor
        SubWindow.add_option_box(self, "Aluno", ["Hugo", "Romulo"])

        historico = [
            Transacao("10/10/2017", "Aquisicao de Premio", -10),
            Transacao("15/10/2017", "Bonificacao do Professor", 30),
            Transacao("10/11/2017", "Tranferencia para amigo", -10),
        ]

        for t in historico:
            SubWindow.add_label(self, t.get_data() + "\t" + t.get_descricao() + "\t" + str(t.get_valor()) + " poopts")

        SubWindow.add_btns(self, ["Sair do Historico"], self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Sair do Historico":
            SubWindow.hide(self, "Historico")
