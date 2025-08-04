import psycopg2
from abc import ABC, abstractmethod
#from app.core.recipient import Repository

class DB(ABC):

    def __init__(self):
        self.__host = ""
        self.__database = ""
        self.__user = ""
        self.__password = ""

    @abstractmethod
    def save(self, arg):pass

    @abstractmethod
    def get_object(self):pass

class DBRepository(DB):

    def save(self, repo):
        pass

    def repo(self):
        pass

class Database:

    def save(self, table:DB, object):
        table.save(object)