import psycopg2
from datetime import datetime

from models import Keppnir
from config import DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT, DB_USER

# Constants
CREATE_TABLE = """CREATE TABLE IF NOT EXISTS keppnir (
            year INTEGER PRIMARY KEY,
            country VARCHAR NOT NULL,
            city VARCHAR NOT NULL,
            location VARCHAR NOT NULL,
            broadcaster VARCHAR NOT NULL,
            date DATE NOT NULL
            )"""
INSERT_DATA = """INSERT INTO keppnir (year, country, city, location, broadcaster, date)
                 VALUES (%s, %s, %s, %s, %s, %s)
                 ON CONFLICT ("year") DO NOTHING"""

class KeppnirData:
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

    def create_table(self):
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(CREATE_TABLE)
                    connection.commit()
                except Exception as e:
                    print(f"An error occurred while creating the table: {e}")
                    connection.rollback()

    def insert_data(self, keppnir_list):
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                try:
                    for keppnir in keppnir_list:
                        date = datetime.strptime(keppnir.get_date(), '%d.%m.%Y').strftime('%Y-%m-%d')
                        cursor.execute(INSERT_DATA, (
                            keppnir.get_year(),
                            keppnir.get_country(),
                            keppnir.get_city(),
                            keppnir.get_location(),
                            keppnir.get_broadcaster(),
                            date
                        ))
                    connection.commit()
                except Exception as e:
                    print(f"An error occurred while inserting data: {e}")
                    connection.rollback()
