## proyecto Grupo Alhpa Code
## Integrantes:
## Nicolás Castro
## Natalia Rivarola
##
##
##
##
##
import psycopg2

class GymDatabase:
    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            port=self.port,
            user=self.user,
            password=self.password
        )
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                edad INTEGER,
                dni VARCHAR(15),
                peso FLOAT,
                altura FLOAT,
                objetivo VARCHAR(50),
                pagado BOOLEAN
            )
        """)
        self.conn.commit()
    def insert_cliente(self, nombre, apellido, edad, dni, peso, altura, objetivo, pagado):
        self.cur.execute("""
            INSERT INTO clientes (nombre, apellido, edad, dni, peso, altura, objetivo, pagado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombre, apellido, edad, dni, peso, altura, objetivo, pagado))
        self.conn.commit()

    def update_cliente(self, cliente_id, nombre, apellido, edad, dni, peso, altura, objetivo, pagado):
        self.cur.execute("""
            UPDATE clientes
            SET nombre = %s, apellido = %s, edad = %s, dni = %s, peso = %s, altura = %s, objetivo = %s, pagado = %s
            WHERE id = %s
        """, (nombre, apellido, edad, dni, peso, altura, objetivo, pagado, cliente_id))
        self.conn.commit()

    def delete_cliente(self, cliente_id):
        self.cur.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        self.conn.commit()

    def filter_clientes(self, filtro):
        self.cur.execute("""
            SELECT id, nombre, apellido, edad, dni, peso, altura, objetivo, pagado
            FROM clientes
            WHERE nombre ILIKE %s OR apellido ILIKE %s OR dni ILIKE %s
        """, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
        return self.cur.fetchall()

    def get_lista_clientes(self):
        self.cur.execute("""
            SELECT id, nombre, apellido, edad, dni, peso, altura, objetivo, pagado
            FROM clientes
        """)
        return self.cur.fetchall()

    def close_connection(self):
        self.cur.close()
        self.conn.close()
   
