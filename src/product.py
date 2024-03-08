from abc import ABC, abstractmethod


class BaseProduct(ABC):

    """
    Абстрактый класс продукта, предписывающий наследникам реализовывать методы str, len, add
    """
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def price(self):
        pass


class MixinRepr:
    """
    Миксин для вывода информации о том, что был создан продукт
    """

    def __init__(self):
        print(self.__repr__())

    def __repr__(self):
        return f'{self.__class__.__name__}, {self.__dict__}'


class Product(MixinRepr, BaseProduct):
    """
    Класс продуктов
    """
    name: str
    description: str
    price: float
    quantity: int

    product_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        """
        Конструктор для создания экземпляра класса
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    def __str__(self) -> str:
        """
        Метод для строкового представления экземпляра класса
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __len__(self) -> int:
        """
        Метод для определения длины экземпляра класса (количества товаров)
        """
        return self.quantity

    def __add__(self, other) -> float:
        """
        Метод для сложения экземпляров класса сложением сумм, умноженных на количество на складе
        """
        if type(self) is type(other):
            result = self.__price * self.quantity + other.__price * other.quantity
            return result
        else:
            raise TypeError("Нельзя складывать продукты разных классов")

    @classmethod
    def create_product(cls, new_product_data: dict):
        """
        Метод для создания экземпляра класса и добавления его в список продуктов
        """
        new_product = cls(**new_product_data)
        if not cls.product_list:
            cls.product_list.append(new_product)
            return new_product
        else:
            for item in cls.product_list:
                if item.name == new_product.name:
                    item.quantity += new_product.quantity
                    if new_product.price >= item.price:
                        item.price = new_product.price
                    else:
                        pass
                else:
                    cls.product_list.append(new_product)
                    return new_product

    @property
    def price(self):
        """
        Геттер для цены продукта
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Метод для установления цены продукта
        """
        if value < self.price:
            confirmation = input("Вы хотите снизить цену?\nЕсли да, нажмите Y, отменить действие - нажмите N: ")
            if confirmation.upper() == "Y":
                self.__price = value
            elif confirmation.upper() == "N":
                print('Операция отменена')
            else:
                print("Некорректный вввод")
        else:
            self.__price = value


class Smartphone(Product):
    """
    Подкласс Смартфон класса Продукт
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str, performance: float,
                 model: str, memory: int):
        self.performance = performance
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)


class LawnGrass(Product):
    """
    Подкласс Трава газонная класса Продукт
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str, country: str,
                 period_of_grown: int):
        self.country = country
        self.period_of_grown = period_of_grown
        super().__init__(name, description, price, quantity, color)
