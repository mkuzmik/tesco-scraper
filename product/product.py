import peewee
import time
import datetime
from peewee import *

sql_database = SqliteDatabase('my_app.db')

class Product(peewee.Model):
    name = peewee.TextField()
    promo = peewee.IntegerField()
    unit_price = peewee.FloatField()
    price_per_kg = peewee.FloatField()
    link = peewee.TextField()
    timestamp = peewee.IntegerField()

    # def __init__(self, name, promo, price, price_per_kg, link, timestamp=time.time()):
    #     super(Product, self).__init__()
    #     self.name = name
    #     self.promo = promo
    #     self.unit_price = price
    #     self.price_per_kg = price_per_kg
    #     self.link = link
    #     self.timestamp = timestamp

    def get_date_in_string(self):
        return datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y/%m/%d')

    def __unicode__(self):
        return self.name + "  " + str(self.unit_price) + "zl   -" + str(self.promo) + "%   " + str(self.price_per_kg)\
               + "zl/unit   " + self.link + "    " + self.get_date_in_string()

    class Meta:
        database = sql_database
