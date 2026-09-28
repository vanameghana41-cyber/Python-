def build_profile(**details):
    print("\n--- Profile Card ---")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

build_profile(name="Saimeghana", age=20, city="Razam", hobby="Coding")
build_profile(name="Ravi", branch="ECE", year=2)
'''Name: Saimeghana
Age: 20
City: Razam
Hobby: Coding

--- Profile Card ---
Name: Ravi
Branch: ECE
Year: 2'''
