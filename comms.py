import sqlite3 as sql


class Database:

    def __init__(self):
        print("Arrived at __init__")
        self.__DEFAULT_PATH = 'db.sqlite3'
        self.connect()

    def connect(self):
        conn = sql.connect(self.__DEFAULT_PATH)
        print("Connected.")
        return conn
