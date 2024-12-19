# app/repositories/person/sqlite_player_repository.py
import sqlite3
from app.repositories.player.iplayer_repository import IPlayerRepository

class SQLitePlayerRepository(IPlayerRepository):
    _instance = None

    def __new__(cls, db_path):
        if cls._instance is None:
            cls._instance = super(SQLitePlayerRepository, cls).__new__(cls)
            cls._instance._initialize(db_path)
        return cls._instance

    def _initialize(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY,
                        father INTEGER,
                        mother INTEGER
                    )
                ''')
            # print("Tabla 'players' creada o existente.")
        except sqlite3.Error as e:
            # print(f"Error al crear la tabla: {e}")
            pass

    def add(self, player):
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO players (id, father, mother)
                    VALUES (?, ?, ?)
                ''', (player.id, player.father, player.mother))
        except sqlite3.Error as e:
            # print(f"Error al añadir el jugador: {e}")
            pass

    def get_all(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM players")
            return cursor.fetchall()
        except sqlite3.Error as e:
            # print(f"Error al obtener todos los jugadores: {e}")
            return []
        
    def get_player_by_id(self, player_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT p.id, p.first_name, p.middle_name, p.last_name, p.second_last_name, p.sex, p.age, p.location, p.plausible_death,
                       pl.father, pl.mother
                FROM persons p
                JOIN players pl ON p.id = pl.id
                WHERE pl.id = ?
            ''', (player_id,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                # Get player statitics
                cursor = self.conn.cursor()
                cursor.execute('''
                SELECT * from statistics WHERE person_id = ?
                ''', (player_id,))
                _data_statistics = cursor.fetchone()
                _statistics = {}

                if _data_statistics:
                    _statistics = {
                        "time": _data_statistics[1],
                        "energy": _data_statistics[2],
                        "hunger": _data_statistics[3],
                        "intelligence": _data_statistics[4],
                        "strength": _data_statistics[5],
                        "mental_health": _data_statistics[6],
                        "physical_health": _data_statistics[7],
                        "social_skills": _data_statistics[8],
                        "job_performance": _data_statistics[9]
                    }
                cursor.close()

                return {
                    "id": result[0],
                    "first_name": result[1],
                    "middle_name": result[2],
                    "last_name": result[3],
                    "second_last_name": result[4],
                    "sex": result[5],
                    "age": result[6],
                    "location": result[7],
                    "plausible_death": result[8],
                    "father": result[9],
                    "mother": result[10],
                    "statistics": _statistics
                }
            else:
                return None
        except sqlite3.Error as e:
            return None
        

    def update_player_statistics(self, player):
        try:
            cursor = self.conn.cursor()
            sql = '''
            UPDATE statistics
            SET 
                time = ?,
                energy = ?,
                hunger = ?,
                intelligence = ?,
                strength = ?,
                mental_health = ?,
                physical_health = ?,
                social_skills = ?,
                job_performance = ?
            WHERE person_id = ?
            '''
            values = (
                player.statistics.time,
                player.statistics.energy,
                player.statistics.hunger,
                player.statistics.intelligence,
                player.statistics.strength,
                player.statistics.mental_health,
                player.statistics.physical_health,
                player.statistics.social_skills,
                player.statistics.job_performance,
                player.id
            )
            cursor.execute(sql, values)
            self.conn.commit()
            # print("Estadísticas del jugador actualizadas exitosamente.")
        except sqlite3.Error as e:
            # print(f"Error al actualizar las estadísticas del jugador: {e}")
            pass
