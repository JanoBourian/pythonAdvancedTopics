import sqlite3
##conexion = sqlite3.connect("usuarios.db")
##conexion = sqlite3.connect("productos.db")
conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()
"""
cursor.execute('''
    CREATE TABLE usuarios (
    dni VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(100),
    edad INTEGER,
    email VARCHAR(100)
    )
''')

usuarios = [
    ('000000001','Hector', 27, 'hector@email.com.mx'),
    ('000000002','Mario', 53, 'mario@ejemplo.com'),
    ('000000003','Juan', 27, 'juan@ejemplo.com'),
    ('000000004','Mercedes', 19, 'mercedesf@ejemplo.com.mx'),
    ('000000005','Julieta', 29,'julieta@ejemplo.com.mx'),
    ('000000006','Maria', 35,'origin@maria.com'),
    ('000000007','Rosalia', 24,'contactorosalia@ejemplo.com')
    ]

"""
## cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

##Campos autoincrementales al crear nuevos registros
"""
cursor.execute('''
    CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    precio FLOAT NOT NULL
    )
''')

productos = [
    ('teclado', 'logitech', 19.96),
    ('pantalla', 'samsung', 89.95)
    ]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

##Ahora vamos a consultar estos productos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
"""

##La última tabla

cursor.execute('''
    CREATE TABLE inventario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad  INTEGER,
        email VARCHAR(100)
    )
''')

usuarios = [
    ('000000001','Hector', 27, 'hector@email.com.mx'),
    ('000000002','Mario', 53, 'mario@ejemplo.com'),
    ('000000003','Juan', 27, 'juan@ejemplo.com'),
    ('000000004','Mercedes', 19, 'mercedesf@ejemplo.com.mx'),
    ('000000005','Julieta', 29,'julieta@ejemplo.com.mx'),
    ('000000006','Maria', 35,'origin@maria.com'),
    ('000000007','Rosalia', 24,'contactorosalia@ejemplo.com')
    ]

cursor.executemany("INSERT INTO inventario VALUES (null,?,?,?,?)", usuarios)

conexion.commit()
conexion.close()
