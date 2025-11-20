import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")


def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada \n {query}")
    except oracledb.DatabaseError as error:
        print(f"No se pudo crear la tabla: {error}")


tables = [
    (
        "CREATE TABLE Dueño ("
        "id_dueño NUMBER PRIMARY KEY UNIQUE,"
        "nombre VARCHAR2(50),"
        "numero VARCHAR2(20),"
        "direccion VARCHAR2(100)"
        ")"
    )(
        "CREATE TABLE Mascota ("
        "id_mascota NUMBER PRIMARY KEY,"
        "nombre VARCHAR2(50),"
        "edad NUMBER,"
        "id_dueño NUMBER,"
        "FOREIGN KEY (id_dueño) REFERENCES Dueño(id_dueño)"
        ")"
    )(
        "CREATE TABLE Perro ("
        "id_mascota NUMBER PRIMARY KEY,"
        "historial_vacunas CLOB,"
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
        ")"
    )(
        "CREATE TABLE Gato ("
        "id_mascota NUMBER PRIMARY KEY,"
        "registro_esterilizacion NUMBER(1),"
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
        ")"
    )(
        "CREATE TABLE Ave ("
        "id_mascota NUMBER PRIMARY KEY,"
        "tipo_jaula VARCHAR2(30),"
        "control_vuelo VARCHAR2(30),"
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
        ")"
    )
]

from datetime import datetime


def create_Dueño(id_dueño, nombre, numero, direccion):
    sql = ("INSERT INTO Dueño (id_dueño, nombre, numero, direccion) VALUES (:id_Dueño, :nombre, :numero, :direccion)"
    )

    parametros = {
        "id_Dueño":id_dueño,
        "nombre":nombre,
        "numero":numero,
        "direccion":direccion
        }

def create_Mascota(id_mascota, id_mascotanombre, edad, id_dueño):
    sql = ("INSERT INTO Mascota (id_mascota, nombre, edad, id_dueño) VALUES (:id_mascota, :nombre, :edad, :id_dueño)"
    )
    parametros = {
        "id_mascota":id_mascota,
        "nombre":id_mascotanombre,
        "edad":edad,
        "id_dueño":id_dueño
        }

def create_perro(id_mascota, historial_vacunas):
    sql = ("INSERT INTO Perro (id_mascota, historial_vacunas) VALUES (:id_mascota, :historial_vacunas)"
    )

    parametros = {
        "id_mascota":id_mascota,
        "historial_vacunas":historial_vacunas
        }

def create_gato(id_mascota, registro_esterilizacion):
    sql = ("INSERT INTO Gato (id_mascota, registro_esterilizacion) VALUES (:id_mascota, :registro_esterilizacion)"
        )
    parametros = { 
        "id_mascota":id_mascota,
        "registro_esterilizacion":registro_esterilizacion
        }

def create_ave(id_mascota, tipo_jaula, control_vuelo):
    sql = ("INSERT INTO Ave (id_mascota, tipo_jaula, control_vuelo) VALUES (:id_mascota, :tipo_jaula, :control_vuelo)"
    ) 
    parametros = {
        "id_mascota":id_mascota,
        "tipo_jaula":tipo_jaula,
        "control_vuelo":control_vuelo
        }