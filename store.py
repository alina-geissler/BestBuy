import products


class Store:
    def __init__(self, products_list):
        if not isinstance(products_list, list):
            raise TypeError("Products has to be a list!")
        for product in products_list:
            if not isinstance(product, products.Product):
                raise TypeError("All products have to be Product objects!")
        self.products = products_list

    def add_product(self, product):
        if not isinstance(product, products.Product):
            raise TypeError("Product has to be a Product object!")
        self.products.append(product)

    def remove_product(self, product):
        if not isinstance(product, products.Product):
            raise TypeError("Product has to be a Product object!")
        self.products.remove(product)

    def get_total_quantity(self):
        quantity = 0
        for product in self.products:
            quantity += product.quantity
        return quantity

    def get_all_products(self):
        return [product for product in self.products if product.active]

    def order(self, shopping_list):
        if not isinstance(shopping_list, list):
            raise TypeError("shopping_list has to be a list!")
        for item in shopping_list:
            if not isinstance(item, tuple):
                raise TypeError("Each item has to be a tuple!")
            if len(item) != 2:
                raise ValueError("Each tuple has to contain exactly 2 values!")
            product, quantity = item
            if not isinstance(product, products.Product):
                raise TypeError("First value in each tuple has to be a Product object!")
            if not isinstance(quantity, int):
                raise TypeError("Second value in each tuple has to be an integer!")
            if quantity <= 0:
                raise ValueError("Quantity has to be a positive integer!")
            if quantity > product.quantity:
                raise ValueError("Quantity larger than what exists!")

        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
