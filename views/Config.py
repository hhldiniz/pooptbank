from views.SubWindow import SubWindow


class Configuration(SubWindow):
    def __init__(self, app, title):
        self.__app = app
        self.__title = title
        SubWindow.__init__(self, app, title)
        SubWindow.set_size(self, "400x200")
        self.add_label(title)
