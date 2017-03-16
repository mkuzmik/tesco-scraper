import urllib
from bs4 import BeautifulSoup
from product import Product

def get_soup_from(link):
    page = urllib.urlopen(link).read()
    return BeautifulSoup(page, 'html.parser')

def get_name_from(product_soup):
    return product_soup.find(name="a", attrs={"class": "product-tile--title product-tile--browsable"}).string

def get_link_from(product_soup):
    return product_soup.find(name="a", attrs={"class": "product-tile--title product-tile--browsable"})['href']

def get_price_per_kg_from(product_soup):
    price_soup = product_soup.find(attrs={"class": "price-per-quantity-weight"})
    price_str = price_soup.find(attrs={"class" : "value"}).string
    price = float(price_str.replace(",","."))
    return price

def get_unit_price_from(product_soup):
    price_soup = product_soup.find(attrs={"class": "price-control-wrapper clearfix"})
    price_str = price_soup.find(attrs={"class" : "value"}).string
    price = float(price_str.replace(",", "."))
    return price

def get_promo_from(product_soup):
    promo_text = ""
    promo = 0
    promo_soup = product_soup.find(name = "li", attrs= {"class" : "product-promotion"})
    if not promo_soup is None:
        promo_text = promo_soup.find(name = "span", attrs= {"class" : "offer-text"}).string
        promo_text = promo_text[9:11]
        if promo_text[1] == '%':
            promo_text = promo_text[0]
        promo = int(promo_text)
    return promo

def scrap_products_from(link):
    result_products = []
    soup = get_soup_from(link)
    products_soup = soup.find_all(name = "li", attrs= {"class" : "product-list--list-item"})

    for product_soup in products_soup:

        name = get_name_from(product_soup)
        link = get_link_from(product_soup)
        promo = get_promo_from(product_soup)
        price_per_kg = get_price_per_kg_from(product_soup)
        unit_price = get_unit_price_from(product_soup)

        result_products.append(Product(name, promo, unit_price, price_per_kg, link))
    return result_products

# test

products = scrap_products_from('https://ezakupy.tesco.pl/groceries/pl-PL/shop/warzywa-owoce/all')

print products
