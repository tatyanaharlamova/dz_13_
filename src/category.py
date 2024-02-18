class Category:
    name: str
    description: str
    products: list
    number_of_categories = 0
    count_of_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.count_of_products = self.count_of_products + len(self.__products)

        Category.number_of_categories += 1

    def add_product(self, product):
        self.__products.append(product)
        self.count_of_products += 1

    @property
    def product(self):
        prod_list = []
        for product in self.__products:
            prod_list.append(f"{product.name}, цена {product.price} руб. Отстаток: {product.quantity} шт.")
        return prod_list

