from src.category import Category
from src.product import Product, Smartphone, LawnGrass
import pytest


@pytest.fixture()
def category_clothes():
    Category.count_of_products = 0
    Category.number_of_categories = 0
    p_1 = Product("Джинсы", "Джинсы классические", 2000, 7, "синий")
    p_2 = Product("Рубашка", "Рубашка хлопковая", 1000, 2, "белый")
    return Category("Одежда", "Повседневная одежда", [p_1, p_2])


@pytest.fixture()
def new_product():
    p_5 = Product("Платье", "Платье летнее", 2000, 3, "белый")
    return p_5


@pytest.fixture()
def two_categories():
    Category.count_of_products = 0
    Category.number_of_categories = 0
    p_1 = Product("Джинсы", "Джинсы классические", 2000, 7, "синий")
    p_2 = Product("Рубашка", "Рубашка хлопковая", 1000, 5, "белый")
    Category("Одежда", "Повседневная одежда", [p_1, p_2])
    p_3 = Product("Брелок", "Брелок металлический", 200, 3, "металлик")
    p_4 = Product("Кулон", "Кулон - сердце", 500, 5, "золотой")
    return Category("Аксессуары", "Аксессуары и украшения", [p_3, p_4])


def test_init(category_clothes):
    """
    Тест создания категории
    """
    assert category_clothes.name == "Одежда"
    assert category_clothes.description == "Повседневная одежда"
    assert category_clothes.count_of_products == 2
    assert Category.number_of_categories == 1


def test_number_of_categories(two_categories):
    """
    Тест на подсчет количества категорий
    """
    assert Category.number_of_categories == 2


def test_add_product(category_clothes, new_product):
    """
    Тест на добавление продукта в категорию
    """
    category_clothes.add_product(new_product)
    assert category_clothes.count_of_products == 3
    with pytest.raises(TypeError):
        category_clothes.add_product("Рубашка")


def test__len__(category_clothes):
    """
    Тест измереня длины экземпляра класса Category
    """
    assert len(category_clothes) == 9


def test_getter_product(category_clothes):
    """
    Тест геттера списка товаров
    """
    assert category_clothes.product == ['Джинсы, цена 2000 руб. Отстаток: 7 шт.', 'Рубашка, цена 1000 руб. Отстаток: 2 шт.']


def test__str__(category_clothes):
    """
    Тест строкового представления экземплярв класса
    """
    assert str(category_clothes) == 'Одежда, количество продуктов: 9'


