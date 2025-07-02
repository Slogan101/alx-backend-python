import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Papertrail1.'
DATABASE = 'ALX_prodev'

def paginate_users(page_size, offset):
    """
    Fetches a single page of users from the database.
    Returns a list of user dicts of length up to page_size.
    """
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def lazy_paginate(page_size):
    """
    Generator that lazily fetches users page by page.
    Yields one user dict at a time.
    """
    offset = 0
    while True:  # one loop total
        page = paginate_users(page_size, offset)
        if not page:
            break
        for user in page:
            yield user
        offset += page_size

# Example usage:
if __name__ == "__main__":
    for user in lazy_paginate(3):
        print(user)
