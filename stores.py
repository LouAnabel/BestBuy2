from colorama import Fore, Style
from products import Product, NonStockedProduct

class Store:
    """Manages a collection of products in a store."""

    def __init__(self, products):
        """Initialize store with optional product list."""
        self.products = products if products is not None else []


    def add_product(self, product):
        """Add a single product to the store."""
        self.products.append(product)


    def remove_product(self, product):
        """Remove specified product if it exists in the store."""
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self):
        """Calculate and return formatted total of all product quantities."""
        total_sum = sum(product.quantity for product in self.products)
        return f"Total items of {total_sum} in store"


    def get_all_products(self):
        """Return a list of all active products."""
        return [product for product in self.products if product.active]

    def order(self, shopping_list):
        """Process an order based on a shopping list and return the total price."""
        total_price = 0
        order_details = []
        products_to_deactivate = []

        # First check all products are available and quantities are sufficient
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(Fore.RED + f"Product {product.name} is not available!" + Style.RESET_ALL)
            if product.quantity < quantity and not isinstance(product, NonStockedProduct):
                raise Exception(Fore.RED + f"Not enough {product.name} in stock!" + Style.RESET_ALL)

        # Process all products without deactivating any during the process
        for product, quantity in shopping_list:
            # Save original quantity for later
            original_quantity = product.quantity

            # Calculate price but don't deactivate the product yet
            if product.promotion:
                item_price = product.promotion.apply_promotion(product, quantity)
            else:
                item_price = quantity * product.price

            # Update quantity without deactivating
            product.quantity -= quantity

            # If this purchase would zero out the product, mark it for deactivation later
            if product.quantity <= 0 and not isinstance(product, NonStockedProduct):
                products_to_deactivate.append(product)

            total_price += item_price
            order_details.append(Fore.BLUE + f"{quantity} * {product.name} for {product.price}€")

        # Print order summary
        for detail in order_details:
            print(detail)

        print(f"_____________________________________")
        print(f"Total price: {total_price:.2f} €" + Style.RESET_ALL)

        # Now deactivate products that should be deactivated
        for product in products_to_deactivate:
            product.deactivate()

        return total_price