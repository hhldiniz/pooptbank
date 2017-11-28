class ModalWindow:
    def __init__(self, app, title):
        self.__modal = self
        self.__app = app
        self.__title = title
        self.__app.startSubWindow(title, modal=True)
        self.__app.showSubWindow(title)