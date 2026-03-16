import pytest
from data.products_data import BACKPACK
from data.inventory_data import inventory_filter_tests

#Teste de Carrinho----------------------------------------------------
produto = BACKPACK

def test_add_to_cart(inventory_page):
    inventory_page.add_product(produto)
    inventory_page.expect_add(produto)
    inventory_page.expect_cart("1")

def test_remove_to_cart(inventory_page):
    inventory_page.add_product(produto)
    inventory_page.remove_product(produto)
    inventory_page.expect_remove(produto)

#Teste de Filtros----------------------------------------------------
@pytest.mark.parametrize("filter_type, get_items, reverse", inventory_filter_tests)
def test_inventory_filters(inventory_page, filter_type, get_items, reverse):
    inventory_page.selected_filter(filter_type)
    
    items = get_items(inventory_page)
    assert items == sorted(items, reverse=reverse)

