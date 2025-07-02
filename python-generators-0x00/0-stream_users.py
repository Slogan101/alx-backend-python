import mysql.connector

# MySQL connection parameters
HOST = 'localhost'
USER = 'root'
PASSWORD = 'Papertrail1.'
DATABASE = 'ALX_prodev'

def stream_users():
    """
    Generator function that fetches rows one by one from the user_data table.
    Yields:
        dict: A row from the user_data table.
    """
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data")
    
    for row in cursor:
        yield row  # Yield one row at a time
    
    cursor.close()
    conn.close()

# Optional test block
if __name__ == "__main__":
    for user in stream_users():
        print(user)
