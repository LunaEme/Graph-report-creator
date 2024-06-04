import sqlite3
import random
import datetime
from data_creation import customer_insert, product_data, sale_insert


# Table creation

create_sales_table = '''CREATE TABLE sales (
                        sale_id INTEGER PRIMARY KEY,
                        sale_date DATE,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        unit_price DECIMAL(10, 2),
                        total_price DECIMAL(10, 2),
                        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                        FOREIGN KEY (product_id) REFERENCES products(product_id)
                     )'''

create_products_table = '''CREATE TABLE products (
                            product_id INTEGER PRIMARY KEY,
                            product_name TEXT,
                            unit_cost  DECIMAL(10, 2)
                         )'''

create_customers_table = '''CREATE TABLE customers (
                            customer_id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            phone INTEGER
                         )'''


# Base insert queries

insert_products_data = '''INSERT INTO products (product_name, unit_cost) VALUES (?, ?)'''

insert_sales_data = '''INSERT INTO sales (sale_date, customer_id, product_id, quantity, unit_price, total_price) VALUES (?, ?, ?, ?, ?, ?)'''

insert_customers_data = '''INSERT INTO customers (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)'''


# Executing create and inserts

conn = sqlite3.connect("sales_dept.db")
conn.execute(create_customers_table)
conn.execute(create_products_table)
conn.execute(create_sales_table)


for customer in range(2531):  # amount of total customers
   conn.execute(insert_customers_data, customer_insert())

for product in product_data:
   conn.execute(insert_products_data, product)

for sale in range(48181):   # amount of total sales
   conn.execute(insert_sales_data, sale_insert())
   

conn.commit()