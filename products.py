class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise Exception("Product name cannot be empty!")
        if price < 0:
            raise Exception("Price cannot not be negative!")
        if quantity < 0:
            raise Exception("Quantity cannot be negative!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return int(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity to buy must be at least 1!")
        if quantity > self.quantity:
            raise Exception("Not enough items in stock!")
        if not self.active:
            raise Exception("None of this product available!")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


