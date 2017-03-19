from product import Product
import re

def reset_table():
    Product.drop_table()
    Product.create_table()

def find_all():
    return Product.select()

def find_by_name(name):
    products = []
    for prod in find_all():
        if re.match('(?i)' + name, prod.name):
            products.append(prod)
    return products

def print_result(result):
    for prod in result:
        print prod