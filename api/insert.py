import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")

def insert_data(file_path, table_name):
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()
    with open(file_path, "r") as f:
        next(f)  # skip header row
        cur.copy_from(f, table_name, sep=",")
        conn.commit()
        cur.close()
        conn.close()
        print(f"Inserted data from {file_path} into {table_name} table")

insert_data("data/users.csv", "users")
insert_data("data/post.csv", "post")                                                               
