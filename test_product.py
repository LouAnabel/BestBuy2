import pytest
from products import Product  # Assuming the Product class is in a file named product.py

class TestProduct:

    def test_init_valid_parameters(self):
        # Test initialization with valid parameters
        product = Product("Test Product", 10.0, 5)
        assert product.name == "Test Product"
        assert product.price == 10.0
        assert product.quantity == 5
        assert product.active is True

    def test_init_empty_name(self):
        # Test initialization with empty name
        with pytest.raises(Exception) as e:
            Product("", 1450, 100)
        assert str(e.value) == "Product name cannot be empty!"

    def test_init_negative_price(self):
        # Test initialization with negative price
        with pytest.raises(Exception) as e:
            Product("MacBook Air M2", -10, 100)
        assert str(e.value) == "Price cannot not be negative!"

    def test_init_negative_quantity(self):
        # Test initialization with negative quantity
        with pytest.raises(Exception) as e:
            Product("Test Product", 10.0, -5)
        assert str(e.value) == "Quantity cannot be negative!"

    def test_zero_quantity_becomes_inactive(self):
        """Test that when a product reaches 0 quantity, it becomes inactive."""
        # Initialize a product with a positive quantity
        product = Product("Test Product", 15.99, 5)
        assert product.is_active() is True

        # Set quantity to zero
        product.set_quantity(0)

        # Verify product became inactive
        assert product.quantity == 0
        assert product.is_active() is False

    def test_purchase_modifies_quantity_and_returns_correct_price(self):
        """Test that product purchase modifies the quantity and returns the right output."""
        # Initialize a product
        product = Product("Test Product", 20.50, 10)
        initial_quantity = product.quantity

        # Purchase 3 items
        quantity_to_buy = 3
        expected_price = quantity_to_buy * product.price
        actual_price = product.buy(quantity_to_buy)

        # Verify correct price was returned
        assert actual_price == expected_price

        # Verify quantity was reduced correctly
        assert product.quantity == initial_quantity - quantity_to_buy

    def test_buying_larger_quantity_than_exists_raises_exception(self):
        """Test that buying a larger quantity than exists invokes exception."""
        # Initialize a product with 5 items
        product = Product("Test Product", 10.0, 5)

        # Try to buy 6 items (more than exist)
        with pytest.raises(Exception) as e:
            product.buy(6)

        # Verify correct exception message
        assert str(e.value) == "Not enough items in stock!"

        # Verify quantity remained unchanged
        assert product.quantity == 5
        assert product.is_active() is True

