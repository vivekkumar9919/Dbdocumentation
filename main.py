# main.py

from setup_tables import create_tables
from insert_data import insert_sample_data

if __name__ == "__main__":
    # Create tables
    create_tables()

    # Define sample data
    customers = []
    # customers = [
    #     ("Alice", "alice@example.com"),
    #     ("Bob", "bob@example.com")
    # ]
    products = []
    # products = [
    #     ("Laptop", 1500.00),
    #     ("Smartphone", 700.00)
    # ]

    orders = []
    # orders = [
    #     (1,),  # Assuming customer_id 1 for the first order
    # ]
    order_items = []
    # order_items = [
    #     (1, 1, 1),  # Order 1, Product 1, Quantity 1
    #     (1, 2, 2)   # Order 1, Product 2, Quantity 2
    # ]

    payments = [
        (1, 1500.00, "Completed"),
        (2, 700.00, "Pending")      
    ]
    
    # Insert sample data
    insert_sample_data(customers, products, orders, order_items, payments)
