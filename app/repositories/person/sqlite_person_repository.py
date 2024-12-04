# app/repositories/person/sqlite_person_repository.py
import sqlite3
from app.repositories.person.iperson_repository import IPersonRepository

class SQLitePersonRepository(IPersonRepository):
    _instance = None

    def __new__(cls, db_path):
        if cls._instance is None:
            cls._instance = super(SQLitePersonRepository, cls).__new__(cls)
            cls._instance._initialize(db_path)
        return cls._instance

    def _initialize(self, db_path):
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
                        location TEXT,
                        plausible_death TEXT
                    )
                ''')
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS statistics (
                        person_id INTEGER PRIMARY KEY,
                        energy INTEGER,
                        hunger INTEGER,
                        intelligence INTEGER,
                        strength INTEGER,
                        mental_health INTEGER,
                        physical_health INTEGER,
                        social_skills INTEGER,
                        job_performance INTEGER,
                        FOREIGN KEY(person_id) REFERENCES persons(id)
                    )
                ''')
            # print("Tabla 'persons' creada o existente.")
        except sqlite3.Error as e:
            # print(f"Error al crear la tabla: {e}")
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
                    INSERT INTO persons (id, first_name, middle_name, last_name, second_last_name, sex, age, location, plausible_death)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (person.id, person.first_name, person.middle_name, person.last_name, person.second_last_name, person.sex, person.age, person.location, person.plausible_death))
                self.conn.execute('''
                    INSERT INTO statistics (person_id, energy, hunger, intelligence, strength, mental_health, physical_health, social_skills, job_performance)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    person.id,
                    person.statistics.energy,
                    person.statistics.hunger,
                    person.statistics.intelligence,
                    person.statistics.strength,
                    person.statistics.mental_health,
                    person.statistics.physical_health,
                    person.statistics.social_skills,
                    person.statistics.job_performance
                ))
        except sqlite3.Error as e:
            # print(f"Error al añadir la persona: {e}")
            pass


    def get_all(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM persons")
            return cursor.fetchall()
        except sqlite3.Error as e:
            # print(f"Error al obtener todas las personas: {e}")
            return []
