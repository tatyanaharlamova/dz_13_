import pytest
from src.category import Category
from src.product import Product


@pytest.fixture()
def category_clothes():
    p1 = Product("Джинсы", "Джинсы классические", 2000, 7)
    p2 = Product("Рубашка", "Рубашка хлопковая", 1000, 5)
    return Category("Одежда", "Повседневная одежда", [p1, p2])


def test_init(category_clothes):
    assert category_clothes.name == "Одежда"
    assert category_clothes.description == "Повседневная одежда"
    assert category_clothes.count_of_products == 12


@pytest.fixture()
def category_accessorise():
    p3 = Product("Брелок", "Брелок металлический", 200, 3)
    p4 = Product("Кулон", "Кулон - сердце", 500, 5)
    return Category("Аксессуары", "Аксессуары и украшения", [p3, p4])


def test_number_of_categories(category_accessorise):
    assert Category.number_of_categories == 2

