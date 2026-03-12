import products


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        quantity = 0
        for product in self.products:
            quantity += product.quantity
        return quantity

    def get_all_products(self):
        return [product for product in self.products if product.active]

    def order(self, shopping_list):
        total = 0.0
        for product, quantity in shopping_list:
            subtotal = product.buy(quantity)
            if subtotal is None:
                return None
            total += subtotal
        return total
