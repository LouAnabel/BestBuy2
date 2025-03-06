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

    def order(self, shopping_list):

        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"Product {product.name} not available!")
                continue

            product.quantity -= quantity
            total_price += float(product.price * quantity)
            print(f"{quantity} * {product.name} for {product.price}€")

        print(f"_____________________________________"
                  f"\nTotal price: {total_price} €")


