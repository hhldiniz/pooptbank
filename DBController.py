import psycopg2


class DBController:
    def __init__(self, host, db_name, db_user, db_pass):
        try:
            self.__con = psycopg2.connect(f"dbname='{db_name}' user='{db_user}' host='{host}' password='{db_pass}'")
            self.__cursor = self.__con.cursor()
        except:
            print("Conexão com o banco falhou")

    def insert_data(self, table="", fields="", data=""):
        prepare_value_string = "("
        data_as_array = data.split(",")
        for obj in data_as_array:
            prepare_value_string+="%s,"
        prepare_value_string = prepare_value_string[:-1]
        prepare_value_string += ")"
        query = f"INSERT INTO \"{table}\" ({fields}) VALUES ({prepare_value_string})"
        print(query)
        result = self.__cursor.execute(query, data)
        return result

    def select_data(self, table="", fields="", conditions="WHERE 1"):
        self.__cursor.execute(f"SELECT {fields} FROM {table} {conditions}")
        return self.__cursor.fetchall()

    def update_data(self, table="", field="", value="", conditions="WHERE 1"):
        result = self.__cursor.execute(f"UPDATE {table} SET {field}='{value}' {conditions}")
        return result
