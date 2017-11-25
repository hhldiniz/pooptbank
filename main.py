from App import Main

if __name__ == '__main__':
    main_app = Main()
    main_app.add_label("main_title", "Bem vindo. Identifique-se para continuar.")
    main_app.add_entries("Username")
    main_app.add_secret_entries("Password")
    main_app.add_buttons(['Entrar', 'Sair'])
    main_app.add_button("Cadastrar")
    main_app.initialize_gui()
