def order_summary(customer, *items, discount=0, **extra):
    print("\n--- Order Summary ---")
    print("Customer:", customer)
    print("Items Ordered:", ", ".join(items))
    print("Discount Applied:", discount)
    for key, value in extra.items():
        print(f"{key.replace('_',' ').capitalize()}: {value}")
    print("---------------------")
order_summary(
    "Saimeghana", 
    "Laptop", "Mouse", "Keyboard", 
    discount=500, 
    delivery_address="Razam, AP", 
    gift_wrap="Yes"
)
'''--- Order Summary ---
Customer: Saimeghana
Items Ordered: Laptop, Mouse, Keyboard
Discount Applied: 500
Delivery address: Razam, AP
Gift wrap: Yes
---------------------'''
