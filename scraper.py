import urllib
from bs4 import BeautifulSoup

class Product:
    def __init__(self, name, promo, price, price_per_kg, link):
        self.name = name
        self.promo = promo
        self.unit_price = price
        self.price_per_kg = price_per_kg
        self.link = link

def get_soup_from(link):
    page = urllib.urlopen(link).read()
    return BeautifulSoup(page, 'html.parser')

def get_name_from(product_soup):
    return product_soup.find(name="a", attrs={"class": "product-tile--title product-tile--browsable"}).string

def get_link_from(product_soup):
    return product_soup.find(name="a", attrs={"class": "product-tile--title product-tile--browsable"})['href']

def get_promo_from(product_soup):
    promo_text = ""
    promo_soup = product_soup.find(name = "li", attrs= {"class" : "product-promotion"})
    if not promo_soup is None:
        promo_text = promo_soup.find(name = "span", attrs= {"class" : "offer-text"}).string
        # TODO
    return promo_text

def scrap_products_from(link):
    result_products = []
    soup = get_soup_from(link)
    products_soup = soup.find_all(name = "li", attrs= {"class" : "product-list--list-item"})
    for product_soup in products_soup:
        name = get_name_from(product_soup)
        link = get_link_from(product_soup)
        promo = get_promo_from(product_soup)

        result_products.append(Product(name, promo, 0, 0, link))
    return result_products

products = scrap_products_from('https://ezakupy.tesco.pl/groceries/pl-PL/shop/warzywa-owoce/all')

print products
