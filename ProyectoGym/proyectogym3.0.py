## proyecto Grupo Alhpa Code
## Integrantes:
## Nicolás Castro
## Natalia Rivarola
## Daniel Alessio
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



























 if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            dni = input("DNI: ")
            peso = float(input("Peso: "))
            altura = float(input("Altura: "))
            objetivo = input("Objetivo de entrenamiento (perdida de grasa / hipertrofia): ")
            pagado = input("¿Pagado? (Sí / No): ").lower() == "sí"

            db.insert_cliente(nombre, apellido, edad, dni, peso, altura, objetivo, pagado)
            print("Cliente agregado con éxito.")

        elif opcion == "2":
            cliente_id = int(input("Ingrese el ID del cliente a editar: "))
            clientes = db.filter_clientes(cliente_id)
            if clientes:
                cliente = clientes[0]
                print("Cliente encontrado:")
                print("ID:", cliente[0])
                print("Nombre:", cliente[1])
                print("Apellido:", cliente[2])
                print("Edad:", cliente[3])
                print("DNI:", cliente[4])
                print("Peso:", cliente[5])
                print("Altura:", cliente[6])
                print("Objetivo:", cliente[7])
                print("Pagado:", "Sí" if cliente[8] else "No")
   
