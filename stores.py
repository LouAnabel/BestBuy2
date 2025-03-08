class Store:

    def __init__(self, products):
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
       total_sum = sum(product.quantity for product in self.products)
       return f"Total items of {total_sum} in store"

    def get_all_products(self):
        return [product for product in self.products if product.active ]



