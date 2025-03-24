import products
from products import NonStockedProduct, LimitedProduct
from stores import Store
from colorama import Fore, Style


def initialize_products():
    """Initialize and return the list of products"""
    return [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]


def initialize_promotions():
    """Initialize and return the promotions dictionary"""
    return {
        0: products.SecondHalfPrice("Second Half price!"),
        1: products.ThirdOneFree("Third One Free!"),
        3: products.PercentDiscount("30% off!", percent=30)
    }


def apply_promotions(product_list, promotions):
    """Apply promotions to products"""
    for product_index, promotion in promotions.items():
        product_list[product_index].set_promotion(promotion)


def initialize_store():
    """Initialize the store with products and promotions"""
    # Get products and promotions
    product_list = initialize_products()
    promotions = initialize_promotions()

    # Apply promotions to products
    apply_promotions(product_list, promotions)

    # Create and return store instance
    return Store(product_list)


def display_menu():
    """Display the store menu and get user choice"""
    print("\n-----------------")
    print("Store Menu")
    print("-----------------")
    print("")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

    return input("\nPlease enter your choice by number (1-4): ")


def print_error(message):
    """Print an error message in red"""
    print(Fore.RED + message + Style.RESET_ALL)


def get_product_number(products_list):
    """Get a valid product number from user input"""
    product_input = input("\nEnter the number for the product (or press Enter to finish): ")

    # Check if user wants to finish
    if product_input.strip() == "":
        print("Order complete!")
        print("\n-----------")
        return None, True  # Return None and a flag indicating completion

    try:
        product_choice = int(product_input)

        # Check if the number is in the valid range
        if not (1 <= product_choice <= len(products_list)):
            print_error(f"Error: Number must be between 1 and {len(products_list)}")
            return None, False  # Return None and a flag indicating to continue

        return product_choice - 1, False  # Return product index and a flag indicating to continue

    except ValueError:
        print_error("Error: Please enter a valid product number")
        return None, False  # Return None and a flag indicating to continue


def validate_product_availability(product):
    """Validate if a product is available for purchase"""
    # Check if product is active
    if not product.is_active():
        print_error(f"Error: {product.name} is not available")
        return False

    # Check if product is in stock
    if not isinstance(product, NonStockedProduct) and product.get_quantity() <= 0:
        print_error(f"Error: {product.name} is out of stock")
        return False

    return True


def get_valid_quantity(product, is_limited=False, maximum=0):
    """Get a valid quantity from user input"""
    while True:
        try:
            quantity = int(input(f"What amount of {product.name} do you want? "))

            if quantity <= 0:
                print_error("Error: Quantity must be at least 1")
                continue

            # Check maximum limit for LimitedProduct
            if is_limited and quantity > maximum:
                print_error(f"Error: Cannot purchase more than {maximum} of {product.name} per order!")
                continue

            # For regular products, check if enough quantity is available
            if not isinstance(product, NonStockedProduct):
                available = product.get_quantity()
                if quantity > available:
                    print_error(f"Error: Not enough stock. Only {available} available")
                    continue

            return quantity

        except ValueError:
            print_error("No valid number entered! Enter only integers.")


def build_shopping_list(products_list):
    """Build a shopping list from user input"""
    shopping_list = []

    while True:
        # Get product choice from user
        product_index, is_done = get_product_number(products_list)

        # If user is done or there was an error, continue to next iteration
        if is_done:
            break
        if product_index is None:
            continue

        # Get the selected product
        selected_product = products_list[product_index]

        # Validate product availability
        if not validate_product_availability(selected_product):
            continue

        # Get quantity for the selected product
        is_limited = isinstance(selected_product, LimitedProduct)
        maximum = selected_product.maximum if is_limited else 0
        quantity = get_valid_quantity(selected_product, is_limited, maximum)

        # Add to shopping list
        shopping_list.append((product_index, quantity))
        print(f"Added {quantity} x {selected_product.name} to your cart")

    return shopping_list


def process_order(products_list, shopping_list):
    """Process an order and display the summary"""
    if not shopping_list:
        print_error("No items in cart.")
        return 0

    total_price = 0
    print("\nOrder Summary:")

    for product_index, quantity in shopping_list:
        product = products_list[product_index]
        try:
            item_price = product.buy(quantity)
            total_price += item_price
            print(f"- {quantity} x {product.name}: ${item_price:.2f}")
        except Exception as e:
            print_error(f"Could not process {product.name}: {str(e)}")

    print(f"\nTotal Order Price: ${total_price:.2f}")
    return total_price


def list_available_products(products_list):
    """List all available products with their index"""
    print("\nAvailable Products:")
    for i, product in enumerate(products_list, 1):
        if product.is_active():
            print(f"{i}. {product.show()}")


def handle_list_products(products_list):
    """Handle the list products menu option"""
    print(" ")
    for product in products_list:
        print(product.show())


def handle_show_total(store):
    """Handle the show total quantity menu option"""
    print(" ")
    print(store.get_total_quantity())


def handle_make_order(products_list):
    """Handle the make order menu option"""
    list_available_products(products_list)

    # Build the shopping list
    shopping_list = build_shopping_list(products_list)

    # Process the order
    if shopping_list:
        process_order(products_list, shopping_list)


def main():
    # Initialize the store once outside the loop
    best_buy = initialize_store()

    while True:
        user_choice = display_menu()
        products_list = best_buy.get_all_products()

        if user_choice == "1":
            handle_list_products(products_list)

        elif user_choice == "2":
            handle_show_total(best_buy)

        elif user_choice == "3":
            handle_make_order(products_list)

        elif user_choice == "4":
            print("Goodbye")
            break

        else:
            print_error("\nChoice not available! Type number for available commands!")


if __name__ == "__main__":
    main()