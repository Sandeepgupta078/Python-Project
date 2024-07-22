from prettytable import PrettyTable

# Create a PrettyTable object
menu_table = PrettyTable()

# Add the columns
menu_table.field_names = ["Item", "Price"]

# Menu of the restaurant - item and price
menu = {
    "idly": 20,
    "dosa": 30,
    "vada": 20,
    "pongal": 40,
    "chapathi": 30,
    "poori": 40,
    "biryani": 100,
    "fried rice": 60,
    "noodles": 50,
    "pizza": 200,
    "burger": 50,
    "sandwich": 80,
    "pasta": 80,
    "salad": 50,
    "juice": 40,
    "milk shake": 50,
    "ice cream": 20,
    "cake": 50,
    "coffee": 30,
    "tea": 15,
    "soup": 30,
    "paneer chilli": 80,
    "gobi manchurian": 70,
    "paneer masala": 80,
    "manchurian": 70,
}

# Add menu items to the PrettyTable
for item, price in menu.items():
    menu_table.add_row([item, price])

# Greet
print("Welcome to our restaurant!")
print("Here is the menu:")
print(menu_table)

# Order
order = []
while True:
    item = input("Enter the item you want to order: ")
    if item.lower() in menu:
        order.append(item.lower())
    else:
        print("Sorry, we don't have that item.")
    more = input("Do you want to order more items? (y/n): ")
    if more.lower() != "y":
        break

# Bill
total = 0
bill_table = PrettyTable()
bill_table.field_names = ["Item", "Price"]
print("Your order is:")
for item in order:
    price = menu[item]
    bill_table.add_row([item, price])
    total += price

print(bill_table)
print(f"Total: {total}")
print("Thank you for visiting our restaurant!")
