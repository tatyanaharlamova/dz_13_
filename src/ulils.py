import json


class Category:
    name: str
    description: str
    products: list
    number_of_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.count_of_products = len(self.__products)

        Category.number_of_categories += 1

    def add_product(self, product):
        self.__products.append(product)

    @property
    def product(self):
        prod_list = []
        for product in self.__products:
            prod_list.append(f"{product.name}, цена {product.price} руб. Отстаток: {product.quantity} шт.")
        return prod_list


class Product:
    name: str
    description: str
    price: float
    quantity: int
    prod_list = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity, product_list):
        new_product = cls(name, description, price, quantity)
        for item in product_list:
            if item.name == new_product.name:
                item.quantity += new_product.quantity
                if item.price < new_product.price:
                    item.price = new_product.price
        else:
            return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Некорректная цена.")
        else:
            if value < self.price:
                confirmation = input("Вы хотите снизить цену?\nЕсли да, нажмите Y, отменить действие - нажмите N: ")
                if confirmation.upper() == "Y":
                    self.__price = value
                elif confirmation.upper() == "N":
                    print('Операция отменена')
                else:
                    print("Некорректный вввод")


def create_instance(file_name):
    '''
    Читает файл json и cоздает списки экземпляров классов
    '''
    with open(file_name) as file:
        list_ = json.load(file)
        category_list = []
        products_list = []
        for item in list_:
            category = Category(item["name"], item["description"], item["products"])
            category_list.append(category)
            for prod in item["products"]:
                product = Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
                products_list.append(product)
        return category_list, products_list
