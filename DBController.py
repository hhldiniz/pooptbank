from pymongo import MongoClient


class DBController:
    class __DBController:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val
    instance = None

    def __init__(self, host="localhost", port=27017, db_name="pooptbank", db_user="root", db_pass=""):
        if not DBController.instance:
            DBController.instance = DBController.__DBController(arg="db_controller")
        else:
            DBController.instance.val = "db_controller"
        try:
            if host == "localhost" or "127.0.0.1":
                url_con = "localhost"
            else:
                url_con = "mongodb://"+db_user+":"+db_pass+"@"+host+":"+str(port)+"/"+db_name+""
            self.__client = MongoClient(url_con)
            self.__db = self.__client[db_name]
            self.__db_name = db_name
            self.__db_pass = db_pass
            self.__db_host = host
            self.__db_user = db_user
            self.__db_port = port
        except:
            print("Conexão com o banco falhou")

    def set_db_name(self, db_name):
        self.__db_name = db_name

    def set_db_host(self, db_host):
        self.__db_host = db_host

    def set_db_pass(self, db_pass):
        self.__db_pass = db_pass

    def set_db_port(self, port):
        self.__db_port = port

    def insert_data(self, collection="", data=None):
        if data is None:
            data = {}
        collection = self.__db[collection]
        print(collection)
        result = collection.insert_one(data)
        return result.inserted_id

    def select_data(self, collection="", conditions=None):
        if conditions is None:
            conditions = {}
        collection = self.__db[collection]
        return collection.find(conditions)

    def select_data_single(self, collection="", condition=None):
        if condition is None:
            condition = {}
        collection = self.__db[collection]
        return collection.find_one(condition)

    def update_data(self, collection="", conditions=None, data=None):
        if data is None:
            data = dict()
        if conditions is None:
            conditions = {}
        collection = self.__db[collection]
        return collection.find_one_and_update(conditions, data)
