import json


class Category:
    name: str
    description: str
    products: list
    number_of_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.count_of_products = len(self.products)

        Category.number_of_categories += 1


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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








