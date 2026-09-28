def calculate_price(price, tax_rate=18, discount=0):
    taxed_price = price + (price * tax_rate / 100)
    final_price = taxed_price - discount
    return final_price
print("Final Price (only price):", calculate_price(1000))
print("Final Price (custom tax):", calculate_price(1000, tax_rate=10))
print("Final Price (all overridden):", calculate_price(1000, tax_rate=12, discount=200))
'''Final Price (only price): 1180.0
Final Price (custom tax): 1100.0
Final Price (all overridden): 920.0'''
