from src.product import Product, Smartphone, LawnGrass, MixinRepr
from abc import ABC, abstractmethod


class NoneProductsException(Exception):
    """
    Класс исключения для продуктов с нулевым количеством
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Ошибка: добавление объекта с нулевым количеством'

    def __str__(self):
        return self.message


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
            try:
                if product.quantity == 0:
                    raise NoneProductsException
            except NoneProductsException as e:
                print(e)
            else:
                self.__products.append(product)
                self.count_of_products += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

    def avg_price(self):
        """
        Метод расчета средней стоимости товаров
        """
        summ = 0
        for product in self.__products:
            summ += product.price
        try:
            avg = summ / len(self.__products)
            return avg
        except ZeroDivisionError:
            return 0

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
    """
    Класс заказа
    """

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'{self.product}, цена {self.price} руб., {self.quantity} шт.'

    def __len__(self):
        return self.quantity

    def add_product(self, product) -> None:
        """
        Метод для добавления нового продукта в заказ
        """
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise NoneProductsException
            except NoneProductsException as e:
                print(e)
            else:
                self.product.append(product)
            finally:
                print("Обработка завершена")
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")


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



