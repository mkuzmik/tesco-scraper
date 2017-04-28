import re

from product import Product
from peewee import *
import datetime
import time


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


def find_promo_grower_than(percent):
    return Product.select().where(Product.promo > percent)


def get_today_products():
    now = datetime.datetime.now()
    timestamp = datetime.datetime(now.year, now.month, now.day, 0, 0)
    return Product.select().where(Product.timestamp > time.mktime(timestamp.timetuple()))


def get_last_timestamp():
    return Product.select(fn.Max(Product.timestamp)).scalar()


def transfer_to_full_day_timestamp(timestamp):
    dateobj = datetime.datetime.fromtimestamp(timestamp)
    return int(time.mktime(datetime.datetime(dateobj.year, dateobj.month, dateobj.day, 0, 0).timetuple()))


def get_latest_products():
    timestamp = transfer_to_full_day_timestamp(get_last_timestamp())
    return Product.select().where(Product.timestamp > timestamp)


def get_latest_products_with_promo_sorted():
    timestamp = transfer_to_full_day_timestamp(get_last_timestamp())
    return Product.select().where((Product.timestamp > timestamp)).where(Product.promo > 0)\
        .order_by(Product.promo.desc())


def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d')

