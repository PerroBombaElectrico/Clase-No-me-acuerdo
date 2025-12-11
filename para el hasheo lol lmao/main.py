import oracledb
import os 
from dotenv import load_dotenv
import bccrypt

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

Class Auth:
    @staticmethod
    def register():
        pass
    @staticmethod
def login():
    pass


"""
Unidad de 
"""

class Fiance:
    @staticmethod
    def getuf():
        pass
    def getivp():
        pass
    def getipc():
        pass
    def getutm():
        pass
    def getusd():
        pass
    def geteur():
        pass


class Database:
    def__init__(self,username,password,dsn):
    self.username = username
    self.password = passwordself.dsn = dsn
def get_connection(self):
    return oracledb.connect(user=self.username, password=self.password dsn=self.dsn)
