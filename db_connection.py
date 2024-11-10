import psycopg2
from config import DATABASE

def create_connection():
    try:
        connection= psycopg2.connect(**DATABASE)
        print("Connected to the database!")
        return connection
    except Exception as e:
        print("Failed to connect!")
        print(e)
        return None