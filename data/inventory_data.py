#Filtro---Tipo de Dado---Reverse-----------
from pages.inventory_page import InventoryPage


inventory_filter_tests = [
    ("az", lambda page: page.get_product_names(), False),
    ("za", lambda page: page.get_product_names(), True),
    ("lohi", lambda page: [float(price.replace("$","")) for price in page.get_products_price()], False),
    ("hilo", lambda page: [float(price.replace("$","")) for price in page.get_products_price()], True),
]