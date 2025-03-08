import products
from products import NonStockedProduct, LimitedProduct
from stores import Store
from colorama import Fore, Style

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = products.SecondHalfPrice("Second Half price!")
third_one_free = products.ThirdOneFree("Third One Free!")
thirty_percent = products.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

def start():
    print("\n-----------------")
    print("Store Menu")
    print( "-----------------")
    print("")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

    users_choice = input("\nPlease enter your choice by number (1-4): ")
    return users_choice


def build_shopping_list(products):
    shopping_list = []

    while True:
        product_input = input("\nEnter the number for the product (or press Enter to finish): ")
        # Check if user wants to finish
        if product_input.strip() == "":
            print("Order quit!")
            print("\n-----------")
            break

        try:
            product_choice = int(product_input)
            # Check if the number is in the valid range
            if not (1 <= product_choice <= len(products)):
                print(Fore.RED + f"Error: Number must be between 1 and {len(products)}" + Style.RESET_ALL)
                continue

            product_index = product_choice - 1
            selected_product = products[product_index]

            # Check if product is active
            if not selected_product.is_active():
                print(Fore.RED + f"Error: {selected_product.name} is not available" + Style.RESET_ALL)
                continue

            # Check if product is in stock
            if not isinstance(selected_product, NonStockedProduct) and selected_product.get_quantity() <= 0:
                print(Fore.RED + f"Error: {selected_product.name} is out of stock" + Style.RESET_ALL)
                continue

            # Get quantity for the selected product
            quantity_valid = False
            while not quantity_valid:
                try:
                    quantity = int(input(f"What amount of {selected_product.name} do you want? "))
                    if quantity <= 0:
                        print(Fore.RED + "Error: Quantity must be at least 1" + Style.RESET_ALL)
                        continue

                    # Check maximum limit for LimitedProduct
                    if isinstance(selected_product, LimitedProduct) and quantity > selected_product.maximum:
                        print(Fore.RED + f"Error: Cannot purchase more than {selected_product.maximum} of {selected_product.name} per order!" + Style.RESET_ALL)
                        continue

                    # For regular products, check if enough quantity is available
                    if not isinstance(selected_product, NonStockedProduct):
                        if quantity > selected_product.get_quantity():
                            print(
                                Fore.RED + f"Error: Not enough stock. Only {selected_product.get_quantity()} available" + Style.RESET_ALL)
                            continue

                    quantity_valid = True

                except ValueError:
                    print(Fore.RED + "No valid number entered! Enter only integers." + Style.RESET_ALL)
                    continue

            shopping_list.append((product_index, quantity))
            print(f"Added {quantity} x {selected_product.name} to your cart")

        except ValueError:
            print(Fore.RED + "Error: Please enter a valid product number" + Style.RESET_ALL)
            continue

    return shopping_list

def process_order(products, shopping_list):
    if not shopping_list:
        print(Fore.RED + "No items in cart." + Style.RESET_ALL)
        return 0

    total_price = 0
    print("\nOrder Summary:")

    for product_index, quantity in shopping_list:
        product = products[product_index]
        try:
            item_price = product.buy(quantity)
            total_price += item_price
            print(f"- {quantity} x {product.name}: ${item_price:.2f}")
        except Exception as e:
            print(Fore.RED + f"Could not process {product.name}: {str(e)}" + Style.RESET_ALL)

    print(f"\nTotal Order Price: ${total_price:.2f}")
    return total_price

def main():

    while True:
        user_choice = start()
        best_buy = Store(product_list)
        products = best_buy.get_all_products()

        if user_choice not in ["1", "2", "3", "4"]:
            print(Fore.RED + "\nChoice not available! Type number for available commands!" + Style.RESET_ALL)
            continue

        if user_choice == "1":
            print(" ")
            for product in products:
                print(product.show())

        if user_choice == "2":
            print(" ")
            print(best_buy.get_total_quantity())

        if user_choice == "3":
            print("\nAvailable Products:")
            for i, product in enumerate(products, 1):
                if product.is_active():
                    print(f"{i}. {product.show()}")

            # First build the shopping list (multiple items)
            shopping_list = build_shopping_list(products)

            # Then process the order once when complete
            if shopping_list:
                new_shopping_list = []
                for product_nr, amount in shopping_list:
                    new_shopping_list.append((products[product_nr], amount))

                process_order(products, shopping_list)
            continue

        if user_choice == "4":
            print("Goodbye")
            break

if __name__ == "__main__":
    main()

