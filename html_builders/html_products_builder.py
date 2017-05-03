from __future__ import unicode_literals
from product.product_service import get_latest_products_with_promo_sorted

header = """
<html>
<head>
  <title>Best promo on e-zakupy Tesco</title>
  <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
Author: M.Kuzmik<br>
"""

table_header = """
<table class="table" border="1" style="border-collapse:collapse">
<tr>
<th>Produkt</th>
<th>Promocja</th>
<th>Cena w zl</th>
<th>Cena za kg/litr</th>
<th>Link</th>
<th>Data</th>
</tr>
"""

footer = """
</table>
</body>
</html>
"""

def products_to_html():
    result = ""
    for product in get_latest_products_with_promo_sorted():
        result += "<tr>"
        result += "<td>" + product.name + "</td>"
        result += "<td>" + str(product.promo).encode("utf-8").decode("utf-8")  + "%" + "</td>"
        result += "<td>" + str(product.unit_price).encode("utf-8").decode("utf-8")  + "</td>"
        result += "<td>" + str(product.price_per_kg).encode("utf-8").decode("utf-8")  + "</td>"
        result += "<td>" + product.link + "</td>"
        result += "<td>" + product.get_date_in_string() + "</td>"
        result += "</tr>\n"
    return result


def get_current_html():
    table_content = products_to_html()
    return header + table_header + table_content + footer

