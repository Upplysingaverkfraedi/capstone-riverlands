import psycopg2

from config import DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT, DB_USER

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS lengd_keppna (
                "competitionYear" INTEGER PRIMARY KEY,
                show INTERVAL NOT NULL,
                songs INTERVAL NOT NULL,
                entertainment INTERVAL NOT NULL,
                voting INTERVAL NOT NULL,
                "firstSong" INTERVAL NOT NULL,
                "lastSong" INTERVAL NOT NULL,
                "firstVote" INTERVAL NOT NULL,
                "lastVote" INTERVAL NOT NULL,
                FOREIGN KEY ("competitionYear") REFERENCES keppnir(year)
            )"""
INSERT_DATA = """INSERT INTO lengd_keppna (
    "competitionYear", 
    show, 
    songs, 
    entertainment, 
    voting, 
    "firstSong", 
    "lastSong", 
    "firstVote", 
    "lastVote"
) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT ("competitionYear") DO NOTHING"""

class LengdKeppnaData():
    def __init__(self):
        self.db_params = {
            "dbname": DB_NAME,
            "user": DB_USER,
            "password": DB_PASSWORD,
            "host": DB_HOST,
            "port": DB_PORT
        }
        self.create_table()

    def get_connection(self):
        return psycopg2.connect(**self.db_params)

    def insert_data(self, lengd_keppna_list):
        connection = self.get_connection()
        cursor = connection.cursor()

        try:
            for keppnir in lengd_keppna_list:
                cursor.execute(INSERT_DATA, (
                    keppnir.get_year(),
                    keppnir.get_show(),
                    keppnir.get_songs(),
                    keppnir.get_entertainment(),
                    keppnir.get_voting(),
                    keppnir.get_first_song(),
                    keppnir.get_last_song(),
                    keppnir.get_first_vote(),
                    keppnir.get_last_vote()
                ))
            connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def create_table(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(CREATE_TABLE)
            connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
