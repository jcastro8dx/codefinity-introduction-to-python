def apply_discount(price, discount=0.05):
    price = price*(1-discount)
    return price

def apply_tax(price, tax=0.07):
    price = price + price*tax
    return price

def calculate_total(price, discount=0.05, tax=0.07):
    price = apply_discount(price, discount)
    price = apply_tax(price, tax)
    return price

total_price_default = calculate_total(price = 120)
total_price_custom = calculate_total(price = 100, discount=0.10, tax=0.08)
print(f"Total cost with default discount and tax: ${total_price_default}")
print(f"Total cost with custom discount and tax: ${total_price_custom}")