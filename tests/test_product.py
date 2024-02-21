from src.product import Product
import pytest


@pytest.fixture()
def product_jeans():
    return Product("Джинсы", "Джинсы классические", 2000, 7)


def test_product_init(product_jeans):
    assert product_jeans.name == "Джинсы"
    assert product_jeans.description == "Джинсы классические"
    assert product_jeans.price == 2000
    assert product_jeans.quantity == 7


def test_product_add():
    p3 = Product("Брелок", "Брелок металлический", 200, 3)
    p4 = Product("Кулон", "Кулон - сердце", 500, 5)
    assert p3 + p4 == 3100


