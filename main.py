from inventory.operations import enqueue, dequeue
from inventory.reporting import generate_pdf
from utils.fetch_data import fetch_inventory

# Example Usage
enqueue("12345", "Milk", 50, 10)
dequeue("12345")

# Generate a report
data = fetch_inventory()
generate_pdf(data)
