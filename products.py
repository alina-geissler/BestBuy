class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("Product name has to be a string!")
        if not name.strip():
            raise ValueError("Product name can't be empty!")
        if not isinstance(price, (int, float)):
            raise TypeError("Price has to be a number!")
        if price < 0:
            raise ValueError("Price can't be negative!")
        if not isinstance(quantity, int):
            raise TypeError("Quantity has to be an integer!")
        if quantity < 0:
            raise ValueError("Quantity can't be negative!")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        if quantity > 0:
            self.active = True
        else:
            self.active = False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity has to be an integer!")
        if quantity < 0:
            raise ValueError("Quantity can't be negative!")
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
        if not self.active:
            raise ValueError("Product is not available (not active)!")
        if not isinstance(quantity, int):
            raise TypeError("Quantity has to be an integer!")
        if quantity <= 0:
            raise ValueError("Quantity has to be positive!")
        if quantity > self.quantity:
            raise ValueError("Quantity larger than what exists!")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity
