import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Papertrail1.'
DATABASE = 'ALX_prodev'

def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    
    for row in cursor:
        yield row['age']
    
    cursor.close()
    conn.close()

def calculate_average_age():
    """
    Calculate the average age by consuming stream_user_ages() without loading all data.
    Prints the average age.
    """
    total_age = 0
    count = 0
    
    for age in stream_user_ages():  # Loop 1
        total_age += float(age)
        count += 1
    
    average = total_age / count if count > 0 else 0
    print(f"Average age of users: {average:.2f}")

if __name__ == "__main__":
    calculate_average_age()
