import sqlite3

conn = sqlite3.connect("intentos.db")

cursor = conn.cursor()

_SQL= """
CREATE TABLE if not exists ACCIDENTES(
RADICADO TEXT,
FECHA1 TEXT,
HORA TEXT,
DÍADELASEMANA TEXT,
CLASE TEXT,
DIRECCIÓN TEXT,
GRAVEDAD TEXT,
BARRIO TEXT,
DISEÑO TEXT);

"""

cursor.execute(_SQL)


with open('sql.sql', 'r',encoding="UTF-8") as f:
    cursor.executescript(f.read())

conn.commit()

conn.close()