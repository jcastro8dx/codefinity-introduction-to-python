# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# the zip function creates a list of tuples
combined_list = zip(products, prices, quantities_sold)
# sorted() sorts by product name in ascending order
sorted_products = sorted(combined_list)

for index in range(len(sorted_products)):
    print(f"Product: {sorted_products[index][0]}")
    print(f"Price: {sorted_products[index][1]}")
    print(f"Quantity Sold: {sorted_products[index][2]}")