# *Best Buy*

This Python application simulates a store inventory management system. 
It allows users to view available products, check total stock, and make orders from a product list. The code includes simple input validation and an interactive menu that guides the user through available actions.

### Features
**List all products:** 
+ Display a list of products available in the store with their price and quantity.
+ Show total stock: Calculate and display the total quantity of all products in the store.
+ Make an order with a **Flexible Promotion System:**

*Percentage discounts*
+ "Buy 2, Get 1 Free" promotions
+ "Second item half price" deals
+ Easily extendable for custom promotion types: Users can select products, specify the quantity they want, and place an order.

Exit the program: Quit the program and end the session.
Requirements
This application requires the following Python libraries:


**How to Use**
Start the program: 
When executed, the program presents a menu with the following options:

*1: List all products in store*: 
Displays the available products, each with its price and stock quantity.

*2: Show total stock in store*:
Displays the sum of quantities across all products.

*3: Make an order*:
Allows the user to select products and specify quantities for purchase. 
Once the order is placed, the system processes it, displays the **total price** with all the discount and updates the stock.

*4: Quit the program*
Quit the program.


## Code Overview
*start() Function*
The start() function presents the user with a menu and prompts them to choose an option. It returns the user's choice for further processing.

*build_shopping_list() Function*
This function allows the user to create a shopping list by selecting products and entering the desired quantity. Input validation is performed to ensure only valid product numbers and quantities are accepted.

*main() Function*
The main() function continuously runs the application until the user chooses to quit. It handles user input and coordinates the workflow, including displaying the product list, processing orders, and displaying total stock.

*Store and Product Classes*
The application uses a Store class to manage the inventory and handle orders. Products are represented by instances of the Product class, which stores the product's name, price, and quantity.

*Example*
Upon running the program, a user might see the following menu:

-----------------
Store Menu
-----------------

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit

Please enter your choice by number (1-4): 3

Available Products:
1. MacBook Air M2, Price: 1450, Quantity: 100, Promotion: Second Half price!
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500, Promotion: Third One Free!
3. Google Pixel 7, Price: 500, Quantity: 250
4. Windows License, Price: 125, Quantity: Unlimited, Promotion: 30% off!
5. Shipping, Price: 10, Quantity: 250, Limited to 1 per order


Enter the number for the product (or press Enter to finish): 1
What amount of MacBook Air M2 do you want? 20
Added 20 x MacBook Air M2 to your cart

Enter the number for the product (or press Enter to finish): 5
What amount of Shipping do you want? 1
Added 1 x Shipping to your cart

Enter the number for the product (or press Enter to finish): 
Order quit!

-----------

Order Summary:
- 20 x MacBook Air M2: $21750.00
- 1 x Shipping: $10.00

Total Order Price: $21760.00
 

**Contributing**
Feel free to fork this project, make improvements, and submit pull requests. All contributions are welcome.
