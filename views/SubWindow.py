class SubWindow:
    def __init__(self, app, title):
        self.__modal = self
        self.__app = app
        self.__title = title
        self.__app.startSubWindow(title, modal=True)
        self.__app.showSubWindow(title)
        self.__btn_callback = None

    def add_btn(self, title):
        self.__app.addButton(title, self.__btn_callback)

    def set_btn_callback(self, callback):
        self.__btn_callback = callback

    def add_label_secret_field(self, title):
        self.__app.addSecretLabelEntry(title)

    def add_label_validation_field(self, title):
        self.__app.addLabelValidationEntry(title)

    def add_label(self, label):
        self.__app.addLabel(label, label)

    def set_size(self, size):
        self.__app.setGeometry(size)
