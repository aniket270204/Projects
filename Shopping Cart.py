class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    # Add item to cart
    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))
        print(f"Added {quantity} x {item.name} to cart.")

    # Remove item from cart
    def remove_item(self, item_name):
        for i, (item, quantity) in enumerate(self.items):
            if item.name == item_name:
                self.items.pop(i)
                print(f"Removed {item_name} from cart.")
                return
        print(f"{item_name} not found in cart.")

    # Show items in cart
    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nShopping Cart:")
            for item, quantity in self.items:
                print(f"- {item.name} (₹{item.price}) x {quantity}")

    # Calculate total bill
    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items)
        return total


# Example Usage
# Create items
laptop = Item("Laptop", 60000)
mouse = Item("Mouse", 500)
keyboard = Item("Keyboard", 1500)

# Create shopping cart
cart = ShoppingCart()

# Add items
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(keyboard, 1)

# Show cart
cart.show_cart()

# Remove item
cart.remove_item("Mouse")

# Show cart again
cart.show_cart()

# Calculate total
print("\nTotal Bill: ₹", cart.calculate_total())
