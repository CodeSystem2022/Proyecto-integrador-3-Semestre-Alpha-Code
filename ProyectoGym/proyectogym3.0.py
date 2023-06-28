## proyecto Grupo Alhpa Code
## Integrantes:
## Nicolás Castro
##
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

   
