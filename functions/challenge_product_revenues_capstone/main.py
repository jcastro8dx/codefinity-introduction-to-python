# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold



def calculate_revenue(prices, quantities_sold):
    revenue = []
    for index in range(len(products)):
        dummy = prices[index]*quantities_sold[index]
        revenue[index].append(dummy)
    return revenue

def formatted_output(revenues):
    sort(revenue_per_product)
    for index in range(len(revenue_per_product)):
        print(f"{revenue_per_product[0]} has total revenue of ${revenue_per_product[1]}")
    

revenue = calculate_revenue(prices_quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)




    
# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")