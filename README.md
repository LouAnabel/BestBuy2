# *Best Buy*

This Python application simulates a store inventory management system. 
It allows users to view available products, check total stock, and make orders from a product list. The code includes simple input validation and an interactive menu that guides the user through available actions.

### Features
**List all products:** 
Display a list of products available in the store with their price and quantity.
Show total stock: Calculate and display the total quantity of all products in the store.
Make an order: Users can select products, specify the quantity they want, and place an order.
Exit the program: Quit the program and end the session.
Requirements
This application requires the following Python libraries:

**colorama:** 
Used to enhance terminal output with colored text.

To install the necessary dependencies, run the following command:

bash, 
Kopieren, 
pip install colorama, 

**How to Use**
Start the program: 
When executed, the program presents a menu with the following options:

*1: List all products in store*: 
Displays the available products, each with its price and stock quantity.

*2: Show total stock in store*:
Displays the sum of quantities across all products.

*3: Make an order*:
Allows the user to select products and specify quantities for purchase. 
Once the order is placed, the system processes it and updates the stock.

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

Please enter your choice by number (1-4): 1
After choosing option 1, the program will display all the products:

yaml
Kopieren
MacBook Air M2 - Price: $1450 - Stock: 100
Bose QuietComfort Earbuds - Price: $250 - Stock: 500
Google Pixel 7 - Price: $500 - Stock: 250
The user can then choose to make an order by selecting products and quantities.

Contributing
Feel free to fork this project, make improvements, and submit pull requests. All contributions are welcome.
