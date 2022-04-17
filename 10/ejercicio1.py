import sqlite3

conexion = sqlite3.connect("app.db")
cursor = conexion.cursor()

def crear_tabla(cursor):
    cursor.execute("""CREATE TABLE Alumnos(
        id INT,
        nombre TEXT,
        apellido TEXT
        );"""
    )


# crear_tabla(cursor)

cursor.execute("INSERT INTO Alumnos VALUES(1, 'Juan', 'Perez')")
cursor.execute("INSERT INTO Alumnos VALUES(2, 'Salvador', 'Mellado')")
cursor.execute("INSERT INTO Alumnos VALUES(3, 'Carlos', 'Nuñez')")
cursor.execute("INSERT INTO Alumnos VALUES(4, 'Jose', 'Castro')")
cursor.execute("INSERT INTO Alumnos VALUES(5, 'Marcos', 'Contreras')")
cursor.execute("INSERT INTO Alumnos VALUES(6, 'Arturo', 'Vidal')")
cursor.execute("INSERT INTO Alumnos VALUES(7, 'Alexis', 'Sanchez')")
cursor.execute("INSERT INTO Alumnos VALUES(8, 'Claudio', 'Bravo')")

rows = cursor.execute("SELECT * FROM Alumnos")

for row in rows:
    print(row)

cursor.close()
conexion.close()