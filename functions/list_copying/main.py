# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    prices_copy = prices.copy()
    for index in range(len(prices_copy)):
        if prices_copy > 2 :
            prices_copy = prices_copy - prices_copy*0,10

    return prices_copy


# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: ${updated_prices}")