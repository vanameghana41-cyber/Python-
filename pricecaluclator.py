def calculate_price(price, tax_rate=18, discount=0):
    final_price = price + (price * tax_rate / 100) - discount
    return final_price
print("Final Price:", calculate_price(1000))
print("Final Price:", calculate_price(1000, tax_rate=10))
print("Final Price:", calculate_price(1000, tax_rate=12, discount=200))
'''Final Price: 1180.0
Final Price: 1100.0
Final Price: 920.0'''
