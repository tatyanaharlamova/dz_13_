import json
from category import Category
from product import Product


def create_instance(file_name):
    """
    Читает файл json и cоздает список экземпляров класса Category,
    добавляет экземпляры классв в класс Product
    """
    with open(file_name) as file:
        full_data = json.load(file)
        category_list = []
        for category_data in full_data:
            products_data = category_data['products']
            for product_data in products_data:
                Product.create_product(product_data)
            category = Category(category_data["name"], category_data["description"], Product.product_list)
            category_list.append(category)
        return category_list


print(create_instance("products.json"))
print(Product.product_list)