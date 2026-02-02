grocery_inventory = {"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99,15), "Apples": ("Produce",1.50,50)}
eggs_price_tupple = grocery_inventory.get("Eggs")
eggs_price = eggs_price_tupple[1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": ("Dairy", eggs_price-1, 30)})
else:
    print("The price of Eggs is reasonable.")
#
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")
#
milk_stock_tupple = grocery_inventory.get("Milk")
milk_stock = milk_stock_tupple[2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": ("Dairy", 3.50, milk_stock + 20)})
else: print("Milk has sufficient stock.")
#
apples_price_tupple = grocery_inventory.get("Apples")
aplles_price = apples_price_tupple[1]
if aplles_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
#
print(f"Updated inventory: {grocery_inventory}")