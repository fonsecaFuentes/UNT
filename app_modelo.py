import sqlite3
import re


def create_db():
    conection = sqlite3.connect("database.db")
    return conection


def create_table():
    conection = create_db()
    cursor = conection.cursor()
    slq = "CREATE TABLE IF NOT EXISTS data_game (id INTEGER PRIMARY KEY,\
            titulo VARCHAR(255), estilo VARCHAR(255), desarrollador\
            VARCHAR(255), precio INTEGER (5))"
    cursor.execute(slq)
    conection.commit()


def validate_fields(titulo, estilo, desarrollador, precio):
    nulo = r"^(?!\s*$).+"

    if (
        re.match(nulo, titulo)
        and re.match(nulo, estilo)
        and re.match(nulo, desarrollador)
        and re.match(nulo, precio)
    ):
        return True
    else:
        return False


def validate_price(precio):
    numero = r"^\d+(\.\d{1,2})?$"
    if re.match(numero, precio):
        return True
    else:
        return False


def alta_item(titulo, estilo, desarrollador, precio):
    data = (titulo, estilo, desarrollador, precio)

    conection = create_db()
    cursor = conection.cursor()
    slq = "INSERT INTO data_game (titulo, estilo, desarrollador,\
                precio) VALUES (?, ?, ?, ?)"
    cursor.execute(slq, data)
    conection.commit()


def del_item(mi_id):
    conection = create_db()
    cursor = conection.cursor()
    data = (mi_id,)
    sql = "DELETE FROM data_game WHERE id = ?"
    cursor.execute(sql, data)
    conection.commit()


def modify_item(mi_id, titulo, estilo, desarrollador, precio):
    data = (titulo, estilo, desarrollador, precio, mi_id)

    conection = create_db()
    cursor = conection.cursor()
    slq = "UPDATE data_game SET titulo=?, estilo=?,\
           desarrollador=?, precio=? WHERE id=?"
    cursor.execute(slq, data)
    conection.commit()


def get_item():
    conection = create_db()
    cursor = conection.cursor()
    sql = "SELECT *  FROM data_game ORDER BY id ASC"
    data = cursor.execute(sql)

    return data.fetchall()


def search_item(imput_search):
    conection = create_db()
    cursor = conection.cursor()
    sql = "SELECT titulo, estilo, desarrollador, precio FROM data_game WHERE\
    titulo LIKE ? OR estilo LIKE ? OR desarrollador LIKE ?"
    data = cursor.execute(sql, (imput_search, imput_search, imput_search))

    return data.fetchall()
