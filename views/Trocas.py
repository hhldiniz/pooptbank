from Prize import Prize
from views.SubWindow import SubWindow
from Transacao import Transacao


class TrocasView(SubWindow):
    def __init__(self, app, title):
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "500x400")
        SubWindow.add_label(self, "Trocas")

        prizes = [
            Prize("Meio Ponto da Media", 10),
            Prize("Correcao Mais Leve", 30),
            Prize("Trabalho Mais Facil", 30),
            Prize("Duplas de 3", 50)
        ]

        for p in prizes:
            SubWindow.add_check_box(self, p.get_descricao(), p.get_descricao() + "\t" + str(p.get_valor()) + " poopts")

        SubWindow.add_btns(self, ["Efetivar Trocas", "Sair das Trocas"], self.__btn_callback)

    def __btn_callback(self, btn):
        if btn == "Sair das Trocas":
            SubWindow.hide(self, "Trocas")
        if btn == "Efetivar Trocas":
            print("logica para efetivar trocas")