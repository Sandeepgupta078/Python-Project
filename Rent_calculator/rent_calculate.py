rent = int(input("Enter the hsotel/flat rent amount: "))
no_of_people = int(input("Enter the number of people living in flat/hostel : "))
food = int(input("Enter the food expense: "))
electricity = int(input("Enter the electricity expense: "))
charge_per_unit = int(input("Enter the charge per unit: "))
internet = int(input("Enter the internet expense: "))

total_electricity_bill = electricity * charge_per_unit

output = (rent + food + total_electricity_bill + internet) / no_of_people

print(f"Each person has to pay: {output}")
