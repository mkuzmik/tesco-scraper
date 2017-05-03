from html_builders.html_products_builder import get_current_html

f = open("index.html", "w")

f.write(get_current_html().encode('utf8'))
