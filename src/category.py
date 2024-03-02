from src.product import Product, Smartphone, LawnGrass, MixinRepr
from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """
    Абстрактный класс для Категории и Заказа
    """
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass


class Category(MixinRepr, BaseCategory):
    """
    Класс категорий товаров
    """
    name: str
    description: str
    products: list
    number_of_categories = 0
    count_of_products = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Конструктор для категории
        """
        self.name = name
        self.description = description
        self.__products = products
        super().__init__()
        Category.count_of_products += len(self.__products)

        Category.number_of_categories += 1

    def __str__(self) -> str:
        """
        Метод, определяющий строковое представление экземпляра класса
        """
        return f"{self.name}, количество продуктов: {len(self)}"

    def __len__(self) -> int:
        """
        Метод для подсчета количества продуктов данной категории на складе
        """
        res = 0
        for product in self.__products:
            res += len(product)
        return res

    def add_product(self, product) -> None:
        """
        Метод для добавления нового продукта в категорию
        """
        if isinstance(product, Product):
            self.__products.append(product)
            self.count_of_products += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

    @property
    def product(self) -> list:
        """
        Метод возвращающий список продуктов в формате: Продукт, цена -- руб. Остаток: -- шт.
        """
        prod_list = []
        for product in self.__products:
            prod_list.append(f"{product.name}, цена {product.price} руб. Отстаток: {product.quantity} шт.")
        return prod_list


class Order(BaseCategory, MixinRepr):
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'{self.product}, цена {self.price} руб., {self.quantity} шт.'

    def __len__(self):
        return self.quantity


class ProductIterator:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current_value = - 1
        return self

    def __next__(self):
        if self.current_value + 1 < len(self.category.product):
            self.current_value += 1
            return self.category.product[self.current_value]
        else:
            raise StopIteration


# p_1 = Product("Джинсы", "Джинсы классические", 2000, 7, "синий")
# p_2 = Product("Рубашка", "Рубашка хлопковая", 1000, 2, "белый")
# c_1 = Category("Одежда", "Повседневная одежда", [p_1, p_2])


# it = ProductIterator(c1)
# print(list(it))
