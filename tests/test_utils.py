import pytest
from src.ulils import Category, Product


@pytest.fixture()
def category_clothes():
    return Category("Одежда", "Повседневная одежда", ["Джинсы", "Толстовка", "Футболка"])


def test_init(category_clothes):
    assert category_clothes.name == "Одежда"
    assert category_clothes.description == "Повседневная одежда"
    assert category_clothes.products == ["Джинсы", "Толстовка", "Футболка"]
    assert category_clothes.count_of_products == 3


@pytest.fixture()
def category_accessorise():
    return Category("Аксессуары", "Аксессуары и украшения", ["Брелок", "Кулон"])


def test_number_of_categories(category_accessorise):
    assert Category.number_of_categories == 2


@pytest.fixture()
def product_jeans():
    return Product("Джинсы", "Джинсы классические", 2000, 7)


def test_product_init(product_jeans):
    assert product_jeans.name == "Джинсы"
    assert product_jeans.description == "Джинсы классические"
    assert product_jeans.price == 2000
    assert product_jeans.quantity == 7


