from pymongo import MongoClient


class DBController:
    def __init__(self, host="localhost", port=27017, db_name="pooptbank", db_user="root", db_pass=""):
        try:
            self.__client = MongoClient(host)
            self.__db = self.__client[db_name]
        except:
            print("Conexão com o banco falhou")

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
