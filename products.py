class Product:
    def __new__(cls, name, price, quantity):
        if not name.replace(" ", ""):
            raise ValueError("Product name can't be empty")
        int(price)
        if price < 0:
            raise ValueError("Price has to be a positive number")
        int(quantity)
        if quantity < 0:
            raise ValueError("Quantity has to be a positive number")
        return super().__new__(cls)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        if quantity > 0:
            self.active = True
        else:
            self.active = False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        try:
            int(quantity)
        except ValueError as e:
            print("Error while making order!", e)
            return None
        try:
            products_left_after_buy = self.quantity - int(quantity)
            if products_left_after_buy < 0:
                raise ValueError("Quantity larger than what exists")
        except ValueError as e:
            print("Error while making order!", e)
            return None
        self.set_quantity(self.quantity - int(quantity))
        return self.price * int(quantity)
