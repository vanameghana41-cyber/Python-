def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    print("\nTemperature Converter Menu")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c} °C = {celsius_to_fahrenheit(c):.2f} °F")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f} °F = {fahrenheit_to_celsius(f):.2f} °C")
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
