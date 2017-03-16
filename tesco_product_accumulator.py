from tesco_scraper import get_all_products_from
from product import Product

def save_to_db_products_from(department_link):
    print "Crawling through ", department_link," ."
    product_list = get_all_products_from(department_link)
    for product in product_list:
        product.save()
    print "Saved to database."
    return


def download_all():
    department_links = [
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/warzywa-owoce/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/nabial-i-jaja/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/mieso-ryby-garmaz/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/mrozonki/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/art.-spozywcze/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/napoje/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/chemia/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/kosmetyki/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/dla-dzieci/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/dla-zwierzat/all',
        'https://ezakupy.tesco.pl/groceries/pl-PL/shop/art.-przemyslowe/all'
    ]
    for link in department_links:
        save_to_db_products_from(link)
    return

