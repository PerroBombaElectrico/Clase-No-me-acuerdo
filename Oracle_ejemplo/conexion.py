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

        "CREATE TABLE Dueño ("
        "id_dueño NUMBER PRIMARY KEY,"
        "nombre VARCHAR2(50),"
        "numero VARCHAR2(20),"
        "direccion VARCHAR2(100)"
        ");"

        "CREATE TABLE Mascota ("
        "id_mascota NUMBER PRIMARY KEY,"
        "nombre VARCHAR2(50),"
        "edad NUMBER,"
        "id_dueño NUMBER,"
        "FOREIGN KEY (id_dueño) REFERENCES Dueño(id_dueño)"
        ");"

        "CREATE TABLE Perro ("
        "id_mascota NUMBER PRIMARY KEY,"
        "historial_vacunas CLOB,"
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
        ");"

        "CREATE TABLE Gato ("
     "id_mascota NUMBER PRIMARY KEY,"
        "registro_esterilizacion NUMBER(1),"
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
        ");"

        "CREATE TABLE Ave ("
        "id_mascota NUMBER PRIMARY KEY,"
        "tipo_jaula VARCHAR2(30),"
        "control_vuelo VARCHAR2(30),"
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
        ");"
    ]