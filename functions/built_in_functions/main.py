# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

keys = list(products)
for index in range(len(products)):
    product_name = keys[index]
    product_values = products[keys[index]]
    price_float = float(product_values[0])
    quantity_sold_int = int(product_values[1])
    total_sales = price_float*quantity_sold_int
    total_sales_list = total_sales_list.append(total_sales)
    
    print(f"Total sales for {products[keys[index]]}: ${total_sales}")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")