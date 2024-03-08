from src.product import Product, Smartphone, LawnGrass
import pytest


@pytest.fixture()
def product_jeans():
    return Product("Джинсы", "Джинсы классические", 2000, 7, "синий")


@pytest.fixture()
def product_dress():
    return Product("Платье", "Платье летнее", 2000, 3, "белый")


def test__str__(product_jeans):
    """
    Тест строкового представления экземпляра класса
    """
    assert str(product_jeans) == 'Джинсы, 2000 руб. Остаток: 7 шт.'


def test_product_init(product_jeans):
    """
    Тест инициализации экземпляра класса Product
    """
    assert product_jeans.name == "Джинсы"
    assert product_jeans.description == "Джинсы классические"
    assert product_jeans.price == 2000
    assert product_jeans.quantity == 7


def test__add__(product_jeans, product_dress):
    """
    Тест на сложение экземпляров класса
    """
    Product.product_list = []
    assert product_jeans + product_dress == 20000


@pytest.fixture
def product_data():
    data = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "color": "серый"
      }
    return data


@pytest.fixture
def new_price_data():
    data = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 280000.0,
        "quantity": 3,
        "color": "серый"
      }
    return data


@pytest.fixture
def low_price_data():
    data = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 80000.0,
        "quantity": 3,
        "color": "серый"
      }
    return data


@pytest.fixture
def new_name_data():
    data = {
        "name": "Iphone15",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 280000.0,
        "quantity": 3,
        "color": "серый"
      }
    return data


def test_create_product(product_data):
    """
    Тест на создание нового экземпляра класса с использованием классового метода.
    """
    Product.product_list = []
    assert Product.create_product(product_data).name == "Samsung Galaxy C23 Ultra"


def test_new_price_product(new_price_data, low_price_data):
    """
    Тест на добавление такого же продукта с новой ценой
    """
    Product.create_product(new_price_data)
    assert Product.product_list[0].quantity == 8
    assert Product.product_list[0].price == 280000.0
    Product.create_product(low_price_data)
    assert Product.product_list[0].quantity == 11
    assert Product.product_list[0].price == 280000.0


def test_new_name_product(new_name_data):
    """
    Тест на добавление нового экземпляра класса с использованием классового метода.
    """
    assert Product.create_product(new_name_data).name == "Iphone15"


def test_set_prise(product_jeans):
    """
    Тест дя установки цены
    """
    product_jeans.price = 3000
    assert product_jeans.price == 3000


@pytest.fixture()
def create_smartphone():
    return Smartphone("Iphone15", "Iphone15", 100000, 3, "белый", 60,
                      "Pro", 256)


def test_init_smartphone(create_smartphone):
    assert create_smartphone.price == 100000
    assert create_smartphone.color == "белый"
    assert create_smartphone.memory == 256


@pytest.fixture()
def create_grass():
    return LawnGrass("Лилипут", "спортивный газон", 1000, 2, "зеленый",
                     "Россия", 12)


def test_init_lawn_grass(create_grass):
    assert create_grass.price == 1000
    assert create_grass.color == "зеленый"
    assert create_grass.period_of_grown == 12


def test__add__different_classes(create_smartphone, create_grass, product_dress):
    with pytest.raises(TypeError):
        create_grass + create_smartphone
        create_smartphone + product_dress
