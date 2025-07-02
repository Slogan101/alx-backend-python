import csv
import uuid
import mysql.connector
from mysql.connector import errorcode


HOST = 'localhost'
USER = 'root'
PASSWORD = 'Papertrail1.'
DATABASE = 'ALX_prodev'

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        )
        print("Connected to MySQL server.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
        print(f"Database `{DATABASE}` is ready.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    cursor.close()


def connect_to_prodev():
    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        print(f"Connected to `{DATABASE}` database.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3,0) NOT NULL,
                INDEX(user_id)
            )
        """)
        print("Table `user_data` is ready.")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    for row in data:
        user_id = str(uuid.uuid4())
        name, email, age = row['name'], row['email'], row['age']
        try:
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                SELECT * FROM (SELECT %s, %s, %s, %s) AS tmp
                WHERE NOT EXISTS (
                    SELECT 1 FROM user_data WHERE email = %s
                ) LIMIT 1
            """, (user_id, name, email, age, email))
        except mysql.connector.Error as err:
            print(f"Insert error: {err}")
    connection.commit()
    print("Data inserted successfully.")
    cursor.close()

def load_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        create_database(conn)
        conn.close()

    db_conn = connect_to_prodev()
    if db_conn:
        create_table(db_conn)
        user_data = load_csv("user_data.csv")
        insert_data(db_conn, user_data)
        db_conn.close()
