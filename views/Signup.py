from DAO.AddressDao import Address
from DAO.StudentDao import Student
from views.Error import ErrorView
from views.SubWindow import SubWindow


class Signup(SubWindow):
    def __init__(self, app, title="Poopt Signup"):
        SubWindow.__init__(self, app, title)
        self.__app = app
        self.__title = title
        SubWindow.add_label_validation_field(self, "New Username")
        SubWindow.add_label_secret_field(self, "New Password")
        SubWindow.add_entry(self, "CPF")
        SubWindow.add_entry(self, "St.")
        SubWindow.add_entry(self, "Neighborhood")
        SubWindow.add_spin_box_range(self, "Number", 1, 9999)
        SubWindow.add_entry(self, "City")
        SubWindow.add_option_box(self, "State", ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA",
                                                  "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
                                                  "RO", "RS", "RR", "SC", "SE", "SP", "TO"])
        SubWindow.set_btn_callback(self, self.btn_callback)
        SubWindow.add_btn(self, "End Signup")
        SubWindow.add_btn(self, "Cancel Signup")

    def destroy_window(self):
        self.__app.destroySubWindow(self.__title)

    def btn_callback(self, btn):
        if btn == "End Signup":
            new_street = SubWindow.get_entry(self, "St.")
            new_neighborhood = SubWindow.get_entry(self, "Neighborhood")
            new_city = SubWindow.get_entry(self, "City")
            new_state = SubWindow.get_option_box(self, "State")
            new_number = SubWindow.get_entry(self, "Number")
            new_address = Address(street=new_street, neighborhood=new_neighborhood, city=new_city,
                                  state=new_state, number=new_number)
            new_user = self.__app.getEntry("New Username")
            new_password = self.__app.getEntry("New Password")
            new_cpf = self.__app.getEntry("CPF")
            new_student = Student(address=new_address, username=new_user, cpf=new_cpf, password=new_password)
            if new_student.save():
                self.hide(self.__title)
            else:
                error_view = ErrorView(self.__app, "Signup Error")
                error_view.show(self)
        elif btn == "Cancel Signup":
            self.hide(self.__title)
