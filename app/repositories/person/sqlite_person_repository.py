# app/repositories/person/sqlite_person_repository.py
import sqlite3
from app.repositories.person.iperson_repository import IPersonRepository

class SQLitePersonRepository(IPersonRepository):
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS persons (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        middle_name TEXT,
                        last_name TEXT,
                        second_last_name TEXT,
                        sex TEXT,
                        age INTEGER,
                        location TEXT
                    )
                ''')
            #print("Tabla 'persons' creada o existente.")
        except sqlite3.Error as e:
            #print(f"Error al crear la tabla: {e}")
            pass

    def get_next_id(self):
        try:
            #print("Entra a generar ID del repo")
            cursor = self.conn.cursor()
            #print("Abrindo conexión")
            cursor.execute("SELECT MAX(id) FROM persons")
            result = cursor.fetchone()
            #print(f"NUEVO ID desde el repositorio: {result}")
            return (result[0] + 1) if result[0] else 1
        except sqlite3.Error as e:
            #print(f"Error al obtener el siguiente ID: {e}")
            return None

    def add(self, person):
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO persons (id, first_name, middle_name, last_name, second_last_name, sex, age, location)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (person.id, person.first_name, person.middle_name, person.last_name, person.second_last_name, person.sex, person.age, person.location))
            #print(f"Persona {person.first_name} añadida.")
        except sqlite3.Error as e:
            #print(f"Error al añadir la persona: {e}")
            pass

    def get_all(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM persons")
            return cursor.fetchall()
        except sqlite3.Error as e:
            # print(f"Error al obtener todas las personas: {e}")
            return []
