from product.product_service import *

def show(products, max = 20):
    for prod in products:
        print prod
        max -= 1
        if max == 0:
            break
    return

print len(get_latest_products_with_promo_sorted())
show(get_latest_products_with_promo_sorted())


