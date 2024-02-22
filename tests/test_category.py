from src.category import Category
from src.product import Product

p1 = Product("Джинсы", "Джинсы классические", 2000, 7)
p2 = Product("Рубашка", "Рубашка хлопковая", 1000, 5)
c1 = Category("Одежда", "Повседневная одежда", [p1, p2])


def test_init():
    assert c1.name == "Одежда"
    assert c1.description == "Повседневная одежда"
    assert c1.count_of_products == 4


p3 = Product("Брелок", "Брелок металлический", 200, 3)
p4 = Product("Кулон", "Кулон - сердце", 500, 5)
c2 = Category("Аксессуары", "Аксессуары и украшения", [p3, p4])


def test_number_of_categories():
    assert Category.number_of_categories == 2

