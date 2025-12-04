import oracledb
import os
from dotenv import load_dotenv

from typing import Optional

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
                import os
                from datetime import datetime
                from typing import Optional

                import oracledb
                from dotenv import load_dotenv

                load_dotenv()

                username = os.getenv("ORACLE_USER")
                dsn = os.getenv("ORACLE_DSN")
                password = os.getenv("ORACLE_PASSWORD")


                def get_connection():
                    return oracledb.connect(user=username, password=password, dsn=dsn)


                def create_schema():
                    """Crea las tablas en el orden correcto (Dueño -> Mascota -> Perro/Gato/Ave)."""
                    tables = [
                        (
                            "CREATE TABLE Dueño ("
                            "id_dueño NUMBER PRIMARY KEY UNIQUE,"
                            "nombre VARCHAR2(50),"
                            "numero VARCHAR2(20),"
                            "direccion VARCHAR2(100)"
                            ")"
                        ),
                        (
                            "CREATE TABLE Mascota ("
                            "id_mascota NUMBER PRIMARY KEY,"
                            "nombre VARCHAR2(50),"
                            "edad NUMBER,"
                            "id_dueño NUMBER,"
                            "FOREIGN KEY (id_dueño) REFERENCES Dueño(id_dueño)"
                            ")"
                        ),
                        (
                            "CREATE TABLE Perro ("
                            "id_mascota NUMBER PRIMARY KEY,"
                            "historial_vacunas CLOB,"
                            "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
                            ")"
                        ),
                        (
                            "CREATE TABLE Gato ("
                            "id_mascota NUMBER PRIMARY KEY,"
                            "registro_esterilizacion NUMBER(1),"
                            "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
                            ")"
                        ),
                        (
                            "CREATE TABLE Ave ("
                            "id_mascota NUMBER PRIMARY KEY,"
                            "tipo_jaula VARCHAR2(30),"
                            "control_vuelo VARCHAR2(30),"
                            "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
                            ")"
                        ),
                    ]

                    with get_connection() as conn:
                        with conn.cursor() as cur:
                            for sql in tables:
                                try:
                                    cur.execute(sql)
                                    print("Tabla creada: ", sql.split("(", 1)[0].strip())
                                except oracledb.DatabaseError as err:
                                    print(f"No se pudo crear la tabla: {err}")
                        conn.commit()


                def create_dueno(id_dueño: int, nombre: str, numero: str, direccion: str):
                    sql = "INSERT INTO Dueño (id_dueño, nombre, numero, direccion) VALUES (:id_dueño, :nombre, :numero, :direccion)"
                    params = {"id_dueño": id_dueño, "nombre": nombre, "numero": numero, "direccion": direccion}
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, params)
                            conn.commit()
                            print("Inserción de dueño correcta.")
                    except oracledb.DatabaseError as error:
                        print(f"No se pudo insertar el dueño: {error}\nSQL: {sql}\nParams: {params}")


                def create_mascota(id_mascota: int, nombre: str, edad: int, id_dueño: int):
                    sql = "INSERT INTO Mascota (id_mascota, nombre, edad, id_dueño) VALUES (:id_mascota, :nombre, :edad, :id_dueño)"
                    params = {"id_mascota": id_mascota, "nombre": nombre, "edad": edad, "id_dueño": id_dueño}
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, params)
                            conn.commit()
                            print("Inserción de mascota correcta.")
                    except oracledb.DatabaseError as error:
                        print(f"No se pudo insertar la mascota: {error}\nSQL: {sql}\nParams: {params}")


                def create_perro(id_mascota: int, historial_vacunas: str):
                    sql = "INSERT INTO Perro (id_mascota, historial_vacunas) VALUES (:id_mascota, :historial_vacunas)"
                    params = {"id_mascota": id_mascota, "historial_vacunas": historial_vacunas}
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, params)
                            conn.commit()
                            print("Inserción de perro correcta.")
                    except oracledb.DatabaseError as error:
                        print(f"No se pudo insertar el perro: {error}\nSQL: {sql}\nParams: {params}")


                def create_gato(id_mascota: int, registro_esterilizacion: int):
                    sql = "INSERT INTO Gato (id_mascota, registro_esterilizacion) VALUES (:id_mascota, :registro_esterilizacion)"
                    params = {"id_mascota": id_mascota, "registro_esterilizacion": registro_esterilizacion}
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, params)
                            conn.commit()
                            print("Inserción de gato correcta.")
                    except oracledb.DatabaseError as error:
                        print(f"No se pudo insertar el gato: {error}\nSQL: {sql}\nParams: {params}")


                def create_ave(id_mascota: int, tipo_jaula: str, control_vuelo: str):
                    sql = "INSERT INTO Ave (id_mascota, tipo_jaula, control_vuelo) VALUES (:id_mascota, :tipo_jaula, :control_vuelo)"
                    params = {"id_mascota": id_mascota, "tipo_jaula": tipo_jaula, "control_vuelo": control_vuelo}
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, params)
                            conn.commit()
                            print("Inserción de ave correcta.")
                    except oracledb.DatabaseError as error:
                        print(f"No se pudo insertar el ave: {error}\nSQL: {sql}\nParams: {params}")


                # -- Lectura / Consultas simples
                def list_duenos():
                    sql = "SELECT id_dueño, nombre, numero, direccion FROM Dueño ORDER BY id_dueño"
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql)
                                rows = cur.fetchall()
                                if not rows:
                                    print("No hay dueños registrados.")
                                    return
                                for r in rows:
                                    print(f"ID={r[0]} | Nombre={r[1]} | Tel={r[2]} | Direc={r[3]}")
                    except oracledb.DatabaseError as error:
                        print(f"Error al listar dueños: {error}")


                def get_dueno_by_id(id_dueño: int):
                    sql = "SELECT id_dueño, nombre, numero, direccion FROM Dueño WHERE id_dueño = :id_dueño"
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, {"id_dueño": id_dueño})
                                row = cur.fetchone()
                                if row:
                                    print(f"ID={row[0]} | Nombre={row[1]} | Tel={row[2]} | Direc={row[3]}")
                                else:
                                    print("Dueño no encontrado.")
                    except oracledb.DatabaseError as error:
                        print(f"Error al consultar dueño: {error}")


                def update_dueno(id_dueño: int, nombre: Optional[str] = None, numero: Optional[str] = None, direccion: Optional[str] = None):
                    modificaciones = []
                    params = {"id_dueño": id_dueño}
                    if nombre is not None:
                        modificaciones.append("nombre = :nombre")
                        params["nombre"] = nombre
                    if numero is not None:
                        modificaciones.append("numero = :numero")
                        params["numero"] = numero
                    if direccion is not None:
                        modificaciones.append("direccion = :direccion")
                        params["direccion"] = direccion

                    if not modificaciones:
                        print("No hay campos para actualizar.")
                        return

                    sql = f"UPDATE Dueño SET {', '.join(modificaciones)} WHERE id_dueño = :id_dueño"
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, params)
                            conn.commit()
                            print(f"Dueño con ID={id_dueño} actualizado.")
                    except oracledb.DatabaseError as error:
                        print(f"Error al actualizar dueño: {error}\nSQL: {sql}\nParams: {params}")


                def delete_dueno(id_dueño: int):
                    sql = "DELETE FROM Dueño WHERE id_dueño = :id_dueño"
                    try:
                        with get_connection() as conn:
                            with conn.cursor() as cur:
                                cur.execute(sql, {"id_dueño": id_dueño})
                            conn.commit()
                            print(f"Dueño con ID={id_dueño} eliminado.")
                    except oracledb.DatabaseError as error:
                        print(f"Error al eliminar dueño: {error}")


                def print_menu():
                    print(
                        """
                ╔════════════════════════════╗
                ║ Crud: Oracle + python ☻☻   ║
                ╠════════════════════════════╣
                ║1. Insertar un dato         ║
                ║2. Listar dueños            ║
                ║3. Consultar dueño por ID   ║
                ║4. Modificar dueño          ║
                ║5. Eliminar dueño           ║
                ║6. Crear esquema (tablas)   ║
                ║0. Salir                    ║
                ╚════════════════════════════╝
                """
                    )


                def main():
                    while True:
                        print_menu()
                        opcion = input("Seleccione una opción: ").strip()
                        if opcion == "0":
                            print("Saliendo...")
                            break
                        elif opcion == "1":
                            print("Insertar dueño:")
                            try:
                                id_dueño = int(input("ID del dueño: "))
                            except ValueError:
                                print("ID inválido.")
                                continue
                            nombre = input("Nombre: ")
                            numero = input("Número: ")
                            direccion = input("Dirección: ")
                            create_dueno(id_dueño, nombre, numero, direccion)
                        elif opcion == "2":
                            list_duenos()
                        elif opcion == "3":
                            try:
                                idq = int(input("ID del dueño: "))
                            except ValueError:
                                print("ID inválido.")
                                continue
                            get_dueno_by_id(idq)
                        elif opcion == "4":
                            try:
                                idq = int(input("ID del dueño a modificar: "))
                            except ValueError:
                                print("ID inválido.")
                                continue
                            nombre = input("Nuevo nombre (enter para omitir): ") or None
                            numero = input("Nuevo número (enter para omitir): ") or None
                            direccion = input("Nueva dirección (enter para omitir): ") or None
                            update_dueno(idq, nombre=nombre, numero=numero, direccion=direccion)
                        elif opcion == "5":
                            try:
                                idq = int(input("ID del dueño a eliminar: "))
                            except ValueError:
                                print("ID inválido.")
                                continue
                            delete_dueno(idq)
                        elif opcion == "6":
                            print("Creando esquema (intente esto solo si la BD está vacía)...")
                            create_schema()
                        else:
                            print("Opción no válida.")


                if __name__ == "__main__":
                    main()