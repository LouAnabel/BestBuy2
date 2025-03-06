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

class NonStockedProduct(Product):
    """A product that doesn't have physical stock (e.g., digital licenses).
    Quantity is always zero, but the product remains active."""

    def __init__(self, name, price):
        # Initialize with zero quantity:
        super().__init__(name, price, 0)
        # Ensure it's active despite zero quantity:
        self.activate()

    def set_quantity_to_zero(self, quantity):
        # Override to prevent quantity changes
        self.quantity = 0
        # Always keep active
        self.activate()

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity to buy must be at least 1!")
        if not self.active:
            raise Exception("None of this product available!")

        # Calculate price without modifying quantity
        total_price = quantity * self.price
        return total_price

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited, Promotion: 30% off"

class LimitedProduct(Product):
    """A product with a maximum purchase quantity per order (e.g., shipping fee)."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)

        if 0 > maximum > 1:
            raise Exception("purchase quantity must be positive and max 1 per order!")

        self.maximum = maximum

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity to buy must be at least 1!")
        if quantity > self.maximum:
            raise Exception(f"Cannot purchase more than {self.maximum} of this product per order!")
        if quantity > self.quantity:
            raise Exception("Not enough items in stock!")
        if not self.active:
            raise Exception("None of this product available!")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price

    def show(self):
        return f"{self.name}, Price: {self.price}, Limited to {self.maximum} per order!, Promotion: None)"




