##Conexión a base de datos.
##Primero creamos la base de datos. 
import sqlite3

conexion = sqlite3.connect("ejemplo.db")

##Un curso similar a los ficheros pero ahora trabajamos sobre la base de datos

cursor = conexion.cursor() ##Ahora ya ejecutamos en formato SQL
"""
# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

##Ahora vamos a insertar un registro
##cursor.execute("INSERT INTO usuarios VALUES ('Hector', 27, 'hector@email.com.mx')")

##Recuperar el primer registro
##cursor.execute("SELECT * FROM usuarios")
##print(cursor) ##Se debe traducir para que lo podamos leer

##usuario = cursor.fetchone()
##print(usuario)## Regresa una tupla

##Ahora vamos a agregar varios datos, que sabemos son de tipo tupla
##Ejecutar una ocnsulta para insertar varios registros


usuarios = [
    ('Mario', 53, 'mario@ejemplo.com'),
    ('Juan', 27, 'juan@ejemplo.com'),
    ('Mercedes', 19, 'mercedesf@ejemplo.com.mx'),
    ('Julieta', 29,'julieta@ejemplo.com.mx'),
    ('Maria', 35,'origin@maria.com'),
    ('Rosalia', 24,'contactorosalia@ejemplo.com')
    ]
##Insertar de forma masiva
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)


##Recuperar de forma masiva
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
##print(usuarios)
for usuario in usuarios:
    print(usuario)
"""


##Confirmar todos los cambios realizados
conexion.commit()

print("Se ejecutó el código completamente")
conexion.close()

