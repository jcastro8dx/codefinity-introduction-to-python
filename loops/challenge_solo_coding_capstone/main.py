# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
keys = list(inventory)
for index in range(len(inventory)):
    current_stock = inventory[keys[index]][0]
    discounted_price = inventory[keys[index]][2]
    regular_price = inventory[keys[index]][1]
    if current_stock < 30:
        print(f"Item {keys[index]} need restocking.")
    elif current_stock > 100:
        print(f"Item {keys[index]} should be sold at the discounted price of {discounted_price}.")
    else:
        print(f"Item {keys[index]} should be sold at the regular price of {regular_price}.")