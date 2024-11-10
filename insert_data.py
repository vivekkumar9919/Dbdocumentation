# insert_data.py

import psycopg2
from db_connection import create_connection

def insert_sample_data(customers, products, orders, order_items, payments):
    """
    Inserts sample data into the customers, products, orders, and order_items tables.
    :param customers: List of tuples for each customer (name, email)
    :param products: List of tuples for each product (name, price)
    :param orders: List of tuples for each order (customer_id)
    :param order_items: List of tuples for each order item (order_id, product_id, quantity)
    :param payments: List of tuples for each payment (customer_id, amount, status)
    """
    conn = create_connection()
    if conn is None:
        print("Connection to database failed.")
        return

    try:
        with conn.cursor() as cursor:
            # Insert customers
            customer_ids = []
            for customer in customers:
                cursor.execute(
                    "INSERT INTO myschema.customers (name, email) VALUES (%s, %s) RETURNING customer_id",
                    customer
                )
                customer_ids.append(cursor.fetchone()[0])  # Collect inserted customer IDs
            
            # Insert products
            product_ids = []
            for product in products:
                cursor.execute(
                    "INSERT INTO myschema.products (name, price) VALUES (%s, %s) RETURNING product_id",
                    product
                )
                product_ids.append(cursor.fetchone()[0])  # Collect inserted product IDs
            
            # Insert orders
            order_ids = []
            for order in orders:
                cursor.execute(
                    "INSERT INTO myschema.orders (customer_id) VALUES (%s) RETURNING order_id",
                    (order[0],)
                )
                order_ids.append(cursor.fetchone()[0])  # Collect inserted order IDs
            
            # Insert order items
            for item in order_items:
                cursor.execute(
                    "INSERT INTO myschema.order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                    item
                )
            # Insert payments
            payment_ids = []
            for payment in payments:
                cursor.execute(
                    "INSERT INTO myschema.payments (customer_id, amount, status) VALUES (%s, %s, %s) RETURNING payment_id",
                    payment
                )
                payment_ids.append(cursor.fetchone()[0])  

            conn.commit()
            print("Sample data inserted successfully!")
            print("Customer IDs:", customer_ids)
            print("Product IDs:", product_ids)
            print("Order IDs:", order_ids)
            print("Payment IDs:", payment_ids)
    except Exception as e:
        print("Failed to insert sample data:", e)
        conn.rollback()
    finally:
        conn.close()
