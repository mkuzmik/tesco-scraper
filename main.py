from tesco_product_accumulator import download_all
from product import Product

def reset_table():
    Product.drop_table()
    Product.create_table()

def findAll():
    return Product.select()


