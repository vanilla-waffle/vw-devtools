import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")

def connect():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def insert(file_path, table_name):
    conn = connect()
    with open(file_path, "r") as f:
        print(f"Started insert operation into {table_name}")
        sql = f.read()
        with conn.cursor() as cur:
            try:
                cur.execute(sql)
                conn.commit()
            except psycopg2.Error as e:
                print(f'Warning: {e}')
                pass
        print(f"Done")

insert("data/vw_driver_licenses.sql", "vw_driver_licenses")
insert("data/vw_users.sql", "vw_users")
insert("data/vw_locations.sql", "vw_locations")
insert("data/vw_vehicle_passport.sql", "vw_vehicle_passport")                                                       
insert("data/vw_vehicles.sql", "vw_vehicles")
