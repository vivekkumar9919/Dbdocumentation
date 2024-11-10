import psycopg2
from psycopg2 import sql

# Database connection parameters
DATABASE = {
    'dbname': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the PostgreSQL database
def create_connection():
    try:
        conn = psycopg2.connect(**DATABASE)
        print("Connected to the database!")
        return conn
    except Exception as e:
        print("Failed to connect to the database.")
        print(e)
        return None

# Create a sample schema and table
def create_schema_and_table(conn):
    try:
        with conn.cursor() as cur:
            # Create a schema
            cur.execute("CREATE SCHEMA IF NOT EXISTS myschema;")
            print("Schema 'myschema' created.")

            # Create a table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS myschema.users (
                user_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cur.execute(create_table_query)
            conn.commit()
            print("Table 'users' created.")
    except Exception as e:
        print("Failed to create schema or table.")
        print(e)
        conn.rollback()

# Insert a record
def insert_user(conn, name, email):
    try:
        with conn.cursor() as cur:
            insert_query = """
            INSERT INTO myschema.users (name, email) VALUES (%s, %s) RETURNING user_id;
            """
            cur.execute(insert_query, (name, email))
            user_id = cur.fetchone()[0]
            conn.commit()
            print(f"User {name} added with user_id: {user_id}")
    except Exception as e:
        print("Failed to insert user.")
        print(e)
        conn.rollback()

# Query users
def query_users(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM myschema.users;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Failed to query users.")
        print(e)

# Main function to execute operations
if __name__ == "__main__":
    connection = create_connection()
    if connection:
        create_schema_and_table(connection)
        insert_user(connection, 'Alice', 'alice@example.com')
        insert_user(connection, 'Bob', 'bob@example.com')
        print("Querying users:")
        query_users(connection)
        connection.close()
