from inventory.operations import enqueue, dequeue
from inventory.reporting import generate_pdf
from utils.fetch_data import fetch_inventory

# Example Usage
enqueue("12345", "Milk", 50, 10)
enqueue("233423", "Egg", 70, 10)
enqueue("564563", "Cake", 80, 10)
enqueue("2342", "Sugar", 90, 10)
dequeue("12345")

# Generate a report
data = fetch_inventory()
generate_pdf(data)
