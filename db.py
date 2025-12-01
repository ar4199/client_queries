import pymysql

# Connect to MySQL server (no DB selected)
def server_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='Arahim4199'
    )

# Connect to the main DB
def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='Arahim4199',
        database='client_queries'
    )

# Create DB + tables (run once)
def initialize_database():
    # Create database
    conn = server_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS client_queries")
    conn.commit()
    conn.close()

    # Create tables
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            USER_NAME VARCHAR(100) PRIMARY KEY,
            HASHED_PASSWORD VARCHAR(255),
            ROLE VARCHAR(20)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS QUERIES (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            EMAIL VARCHAR(255),
            MOBILE VARCHAR(20),
            HEADING TEXT,
            DESCRIPTION TEXT,
            STATUS VARCHAR(20),
            CREATED_TIME DATETIME,
            CLOSED_TIME DATETIME
        )
    """)

    conn.commit()
    conn.close()

