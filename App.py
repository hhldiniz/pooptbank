from appJar import gui


class Main:
    def __init__(self, title="Poopt Bank", size="800x600"):
        self.__app = gui(title, size)

    def add_label(self, label_name, label_text):
        self.__app.addLabel(label_name, label_text)

    def add_buttons(self, buttons):
        self.__app.addButtons(buttons, self.__btn_callback)

    def add_button(self, button):
        self.__app.addButton(button, self.__btn_callback)

    def add_entries(self, entry_name):
        self.__app.addLabelEntry(entry_name)

    def add_secret_entries(self, entry_name):
        self.__app.addLabelSecretEntry(entry_name)

    def get_app_gui(self):
        return self.__app

    def initialize_gui(self):
        self.__app.go()

    def __btn_callback(self, btn):
        print('clicked')
