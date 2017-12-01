from pymongo import MongoClient


class DBController:
    def __init__(self, host="localhost", port="27017", db_name="pooptbank", db_user="root", db_pass=""):
        try:
            self.__client = MongoClient(host, port)
            self.__db = self.__client[db_name]
        except:
            print("Conexão com o banco falhou")

    def insert_data(self, collection="", data=None):
        if data is None:
            data = {}
        collection = self.__db[collection]
        return collection.insert_one(data).inserted_id

    def select_data(self, collection="", conditions=None):
        if conditions is None:
            conditions = {}
        collection = self.__db[collection]
        return collection.find(conditions)

    def update_data(self, collection="", conditions=None, data=None):
        if data is None:
            data = dict()
        if conditions is None:
            conditions = {}

