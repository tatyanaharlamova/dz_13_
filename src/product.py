class Product:
    name: str
    description: str
    price: float
    quantity: int

    product_list = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, new_product_data):
        new_product = cls(**new_product_data)
        if cls.product_list:
            for item in cls.product_list:
                if item.name == new_product.name:
                    item.quantity += new_product.quantity
                    if item.price >= new_product.price:
                        continue
                    item.price = new_product.price
                else:
                    cls.product_list.append(new_product)
                    return new_product
        else:
            cls.product_list.append(new_product)
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

