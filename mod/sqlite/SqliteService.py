import sqlite3


class SqliteService :

    __connection = None

    def __init__(self):
        self.__connection = sqlite3.connect("member.db")

    def createDb(self):
        cursor = self.__connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS member (name text , isCriminal int)")
        cursor.execute("INSERT INTO member VALUES ('Nagase' , 0) , ('Kokubun' , 0) , ('Yamaguchi' , 1)")

    def commit(self):
        self.__connection.commit()

    def __del__(self):
        self.__connection.close()


