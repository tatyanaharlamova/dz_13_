from src.product import Product, Smartphone, LawnGrass


class Category:
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
        if isinstance(product, (Product, Smartphone, LawnGrass)):
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


# p1 = Product("Джинсы", "Джинсы классические", 2000, 7)
# p2 = Product("Рубашка", "Рубашка хлопковая", 1000, 5)
# c1 = Category("Одежда", "Повседневная одежда", [p1, p2])
# print(c1.count_of_products)
# p5 = Product("Платье", "Платье летнее", 2000, 1)
# c1.add_product(p5)
# print(c1.count_of_products)
# it = ProductIterator(c1)
# print(list(it))
