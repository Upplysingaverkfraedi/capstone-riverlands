import sqlite3

from models import Keppnir

# Constants
CREATE_TABLE = """CREATE TABLE IF NOT EXISTS keppnir (
            id INTEGER PRIMARY KEY, 
            year INTEGER NOT NULL,
            country STRING NOT NULL,
            city STRING NOT NULL,
            location STRING NOT NULL,
            broadcaster STRING NOT NULL,
            date DATE NOT NULL
            )"""
INSERT_DATA = """INSERT INTO keppnir (year, country, city, location, broadcaster, date)
                 VALUES (?, ?, ?, ?, ?, ?)"""


class KeppnirData():
    def __init__(self):
        pass

    def insert_data(self, keppnir_list):
        with sqlite3.connect('mydb.db') as conn:
            cursor = conn.cursor()
            
            for keppnir in keppnir_list:
                cursor.execute(INSERT_DATA, (
                    keppnir.get_year(),
                    keppnir.get_country(),
                    keppnir.get_city(),
                    keppnir.get_location(),
                    keppnir.get_broadcaster(),
                    keppnir.get_date()
                ))

            conn.commit()

    def create_table():
        with sqlite3.connect('mydb.db') as conn:
            cursor = conn.cursor()
            cursor.execute(CREATE_TABLE)
            conn.commit()
