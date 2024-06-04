import random
from faker import Faker # py -m pip install faker

# We use faker to create big amounts of first and last names for our database
fake = Faker()
name_list = []
surname_list = []

while len(name_list) < 75:
    name_list.append(fake.first_name())

while len(surname_list) < 75:
    surname_list.append(fake.last_name())

product_data = [('Product 1',50), ('Product 2',120), ('Product 3',75), ('Product 4',80), ('Product 5',95), ('Product 6',180), ('Product 7',200), ('Product 8',64),
                ('Product 9',121), ('Product 10',142), ('Product 11',66), ('Product 12',98), ('Product 13',111), ('Product 14',98), ('Product 15',165), ('Product 16',191),
                ('Product 17',102), ('Product 18',123), ('Product 19',66), ('Product 20',51), ('Product 21',171), ('Product 22',148)]

def customer_insert():
     customer_first_name = random.choice(name_list)
     customer_last_name = random.choice(surname_list)
     customer_phone = random.randrange(5501111, 5599999)
     return customer_first_name, customer_last_name, \
        f"{customer_first_name}{customer_last_name}{random.randint(1,154)}@gmail.com", customer_phone

            
def sale_insert():
    day = random.randint(1,28)
    month = random.randint(1,12)
    year = random.randint(2021, 2023)
    sale_date = f'{month}-{day}-{year}'
    sale_customer_id = random.randint(1,2531)
    sale_product_id = random.randint(0,21)
    sale_quantity = random.randint(1,20)
    selected_product = product_data[sale_product_id]
    sale_unit_price = selected_product[1]
    sale_total_price = sale_quantity * sale_unit_price
    return sale_date, sale_customer_id, sale_product_id, sale_quantity, sale_unit_price, sale_total_price