import sys
from inventory import Inventory
from receipt import Receipt

# Initialize inventory and receipt objects
inventory = Inventory()
receipt = Receipt()

def manage_inventory():
    """Allow the user to manage inventory."""
    while True:
        print("\n--- Managing Inventory ---")
        serial_number = input("Enter serial number for new item (or type 'exit' to go back to dashboard): ")
        if serial_number.lower() == 'exit':
            break
        
        name = input("Enter the name of the item: ")
        price = float(input("Enter the price of the item: "))
        
        # Add the item to the inventory
        inventory.add_item(serial_number, name, price)
        print(f"Item '{name}' with serial number {serial_number} added to inventory.")
        
        # Ask if user is done adding items
        done = input("Are you done adding items? (yes to finish, or press any key to continue adding): ")
        if done.lower() == 'yes':
            break

def perform_billing():
    """Allow the user to perform billing and create a receipt."""
    while True:
        if len(inventory.queue) == 0:
            print("\nError: Inventory is empty! The supermarket is out of stock.")
            break
        
        print("\n--- Billing ---")
        serial_number = input("Enter the serial number of the item (or type 'exit' to finish billing): ")
        if serial_number.lower() == 'exit':
            break
        
        # Search and remove the item from inventory
        item = inventory.remove_item(serial_number)
        if item:
            receipt.add_item(item["name"], item["price"])
            print(f"Item '{item['name']}' added to receipt with price {item['price']}.")
        else:
            print(f"Error: Item with serial number {serial_number} not found in inventory.")
            continue

        # Ask if user wants to continue or finish billing
        done = input("Are you done with the billing? (yes to finish, or press any key to continue): ")
        if done.lower() == 'yes':
            break

    # Calculate and display the total cost if billing is finished
    if receipt.size > 0:
        print("\n--- Receipt Summary ---")
        receipt.display_receipt()

def dashboard():
    """Display the main dashboard for the user."""
    while True:
        print("\n--- Supermarket Dashboard ---")
        choice = input("Enter '1' to manage inventory, '2' to perform billing, or 'exit' to quit: ")
        
        if choice == '1':
            manage_inventory()
        elif choice == '2':
            perform_billing()
        elif choice.lower() == 'exit':
            print("Exiting the supermarket system.")
            sys.exit(0)
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    dashboard()
