from views.View import View


class Signup(View):
    def __init__(self, title="Poopt Bank - Singup", size='800x600'):
        View.__init__(self, title, size)