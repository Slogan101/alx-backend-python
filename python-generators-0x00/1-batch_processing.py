import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Papertrail1.'
DATABASE = 'ALX_prodev'

def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows from user_data table in batches.
    Yields a list of user dicts of size batch_size (or smaller if last batch).
    """
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    
    batch = []
    for row in cursor:  # loop 1: iterate all rows
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
    
    cursor.close()
    conn.close()

def batch_processing(batch_size):
    """
    Processes each batch from stream_users_in_batches to filter users over age 25.
    Yields each filtered user one by one.
    """
    for batch in stream_users_in_batches(batch_size):  # loop 2: iterate batches
        for user in batch:  # loop 3: iterate users in batch
            if user['age'] > 25:
                yield user

# Example usage:
if __name__ == "__main__":
    for user in batch_processing(3):
        print(user)
