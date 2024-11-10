# setup_tables.py

import psycopg2
from db_connection import create_connection

def create_tables():
    conn = create_connection()
    if conn is None:
        print("Connection to database failed.")
        return

    try:
        with conn.cursor() as cursor:
            # Ensure schema 'myschema' exists
            cursor.execute("CREATE SCHEMA IF NOT EXISTS myschema")

            # Set the search path to use myschema by default
            cursor.execute("SET search_path TO myschema")

            # Create tables in myschema
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255)
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                price DECIMAL(10, 2)
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id SERIAL PRIMARY KEY,
                customer_id INTEGER REFERENCES customers(customer_id),
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                order_item_id SERIAL PRIMARY KEY,
                order_id INTEGER REFERENCES orders(order_id),
                product_id INTEGER REFERENCES products(product_id),
                quantity INTEGER
            )
            """)

            conn.commit()
            print("Tables created successfully.")
    except Exception as e:
        print("Failed to create tables:", e)
        conn.rollback()
    finally:
        conn.close()
