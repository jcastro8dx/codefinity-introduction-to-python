# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

keys = list(inventory)

print("Processing started")
for index in range(len(inventory)):
    # gets the stock quantity which is the first element of each value list
    key = keys[index]
    print(f"Processing {key}" )
    current_stock = inventory[key][0]
    minimum_stock = inventory[key][1]
    restock_quantity = inventory[key][2]
    # restocking
    while current_stock < minimum_stock:
        current_stock += restock_quantity
    # updates value in dictionary   
    inventory[key][0] = current_stock
    if inventory[key][0] > discount_threshold and inventory[key][3] == False:
        inventory[key][3] = True

print("Processing completed")
    