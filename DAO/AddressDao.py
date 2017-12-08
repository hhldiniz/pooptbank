class Address:
    def __init__(self, street, neighborhood, number, city, state):
        self.__street = street
        self.__neighborhood = neighborhood
        self.__number = number
        self.__city = city
        self.__state = state

    def __str__(self):
        return "St: "+self.__street+"Neighborhood: "+self.__neighborhood+"Number: "+self.__number

    def get_street(self):
        return self.__street

    def set_street(self, street):
        self.__street = street

    def get_neighborhood(self):
        return self.__neighborhood

    def set_neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_date(self):
        return self.__state

    def set_state(self, state):
        self.__state = state