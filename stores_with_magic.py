from products import Product

class Store:
    def __init__(self, products=None):
        self.products = products or []

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def __contains__(self, item):
        """Check if a product exists in the store using 'in' operator."""
        if isinstance(item, Product):
            return item in self.products
        elif isinstance(item, str):
            # Also allow checking by product name
            return any(p.name == item for p in self.products)
        return False

    def __add__(self, other):
        """Combine two stores using '+' operator."""
        if isinstance(other, Store):
            new_store = Store()
            # Add products from both stores
            for product in self.products:
                new_store.add_product(product)
            for product in other.products:
                new_store.add_product(product)
            return new_store
        return NotImplemented