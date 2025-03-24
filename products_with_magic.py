from abc import ABC, abstractmethod


# Promotions Module
class Promotion(ABC):
    """Abstract base class for product promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    """Every second item is half price."""

    def apply_promotion(self, product, quantity):
        # Calculate how many items get the full price and how many get half price
        full_price_count = (quantity + 1) // 2  # Round up for odd quantities
        half_price_count = quantity // 2  # Integer division for even count

        total = (full_price_count * product.price) + (half_price_count * product.price * 0.5)
        return total


class ThirdOneFree(Promotion):
    """Buy 2 items, get 1 free."""

    def apply_promotion(self, product, quantity):
        # Calculate how many free items
        free_items = quantity // 3
        # Calculate how many items to pay for
        paid_items = quantity - free_items

        return product.price * paid_items


class PercentDiscount(Promotion):
    """Applies a percentage discount to a product."""

    def __init__(self, name, percent):
        super().__init__(name)
        if not 0 < percent < 100:
            raise Exception("Percentage discount must be between 0 and 100!")
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount_factor = (100 - self.percent) / 100
        return product.price * quantity * discount_factor


# Products Module
class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise Exception("Product name cannot be empty!")
        if price < 0:
            raise Exception("Price cannot be negative!")
        if quantity < 0:
            raise Exception("Quantity cannot be negative!")

        self.name = name
        self.price = price
        self._quantity = quantity
        self._active = True
        self._promotion = None  # Default: no promotion

    @property
    def quantity(self):
        return int(self._quantity)

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
        if self._quantity <= 0:
            self.deactivate()

    @property
    def active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    @property
    def promotion(self):
        """Get the current promotion."""
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """Set a promotion for this product."""
        self._promotion = promotion

    def remove_promotion(self):
        """Remove the current promotion from this product."""
        self._promotion = None

    def __str__(self):
        if self._promotion:
            return f"{self.name}, Price: {self.price}, Quantity: {self._quantity}, Promotion: {self._promotion.name}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self._quantity}"

    def __gt__(self, other):
        """Greater than comparison based on price."""
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

    def __eq__(self, other):
        """Equality comparison based on name."""
        if isinstance(other, Product):
            return self.name == other.name
        return NotImplemented

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity to buy must be at least 1!")
        if quantity > self._quantity:
            raise Exception(f"Not enough {self.name} in stock!")
        if not self._active:
            raise Exception(f"Product {self.name} is not active!")

        # Calculate price with promotion if applicable
        if self._promotion:
            total_price = self._promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.quantity = self._quantity - quantity
        return total_price


class NonStockedProduct(Product):
    """A product that doesn't have physical stock (e.g., digital licenses).
    Quantity is always zero, but the product remains active."""

    def __init__(self, name, price):
        # Initialize with zero quantity:
        super().__init__(name, price, 0)
        # Ensure it's active despite zero quantity:
        self.activate()

    @property
    def quantity(self):
        return 0

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = 0
        self.activate()

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity to buy must be at least 1!")
        if not self._active:
            raise Exception(f"Product {self.name} is not active!")

        # Calculate price with promotion if applicable
        if self._promotion:
            total_price = self._promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        # Don't call set_quantity here as it would reset to 0 anyway
        # Instead, explicitly ensure the product stays active
        self.activate()

        return total_price

    def __str__(self):
        if self._promotion:
            return f"{self.name}, Price: {self.price}, Quantity: Unlimited, Promotion: {self._promotion.name}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: Unlimited"


class LimitedProduct(Product):
    """A product with a maximum purchase quantity per order (e.g., shipping fee)."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)

        if maximum <= 0:
            raise Exception("Maximum purchase quantity must be positive!")

        self.maximum = maximum

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity to buy must be at least 1!")

        # Check maximum first to provide a clearer error message
        if quantity > self.maximum:
            raise Exception(f"Error: Cannot purchase more than {self.maximum} of {self.name} per order!")

        if quantity > self._quantity:
            raise Exception(f"Not enough {self.name} in stock!")
        if not self._active:
            raise Exception(f"Product {self.name} is not active!")

        # Calculate price with promotion if applicable
        if self._promotion:
            total_price = self._promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.quantity = self._quantity - quantity
        return total_price

    def __str__(self):
        promotion_text = f", Promotion: {self._promotion.name}" if self._promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self._quantity}, Limited to {self.maximum} per order{promotion_text}"
