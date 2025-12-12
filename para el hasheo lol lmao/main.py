import oracledb
import os
from dotenv import load_dotenv
import bcrypt
from typing import Optional
import requests
import datetime

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")


class Auth:
    @staticmethod
    def register():
        pass

    @staticmethod
    def login():
        pass


"""
Unidad de Fomento (UF).
Indice de valor Promedio (IVP)
Indice de Precio valor al consumidor (IPC)
Unidad Tributaria mensual (UTM)
Dólar = CLP


"""


class Fiance:
    def __init__(self,base_url:str):
        pass
    def getuf(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{year}-{month}-{day}"
            url = f"{self.base_url}/uf/{fecha}"
            data = requests.get(url=url).json()
            print(data['serie'][0]['valor'])


    def getivp(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{year}-{month}-{day}"
            url = f"{self.base_url}/ivp/{fecha}"
            data = requests.get(url=url).json():
        pass

    def getipc(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{year}-{month}-{day}"
            url = f"{self.base_url}/ivp/{fecha}"
            data = requests.get(url=url).json():
        pass

    def getutm(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{year}-{month}-{day}"
            url = f"{self.base_url}/ivp/{fecha}"
            data = requests.get(url=url).json():
        pass(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{year}-{month}-{day}"
            url = f"{self.base_url}/ivp/{fecha}"
            data = requests.get(url=url).json():def getusd(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{year}-{month}-{day}"
            url = f"{self.base_url}/ivp/{fecha}"
            data = requests.get(url=url).json()::
        pass

    def geteur(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{year}-{month}-{day}"
            url = f"{self.base_url}/ivp/{fecha}"
            data = requests.get(url=url).json()::
        pass


class Database:
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.passwordself.dsn = dsn
        

def get_connection(self):
    return oracledb.connect(user=self.username, password=self.password dsn=self.dsn)
def create_all_tables(self):
    pass
def query(self, sentence: str, parameters: dict):
    print(f"Ejecutando query:\n {sentence} con parametros:\n {parameters}")
    try:
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
               resultado = cursor.execute(sentence, parameters)
               for fila in resultado:
                   print(fila)
            connection.commit()
    except oracledb.DatabaseError as error:
            print(f"Hubo un error :\n {error}")


if __name__ == "__main__":
    db = Database(username=username, password=password, dsn=dsn)
    db.QUERY("select sysdate from dual")

    if __name__ == "__main__":
        indicadores = Fiance()
        indicadores.getuf()
        indicadores.getivp()