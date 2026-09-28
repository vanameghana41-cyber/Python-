def build_profile(**details):
    print("\n--- Profile Card ---")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")
    print("--------------------")
build_profile(name="Alice", age=20, city="Hyderabad", hobby="Reading")
build_profile(name="Bob", profession="Engineer", country="India")
build_profile(name="Charlie", age=25, hobby="Gaming", city="Delhi", skill="Python")
'''Name: Alice
Age: 20
City: Hyderabad
Hobby: Reading
--------------------

--- Profile Card ---
Name: Bob
Profession: Engineer
Country: India
--------------------

--- Profile Card ---
Name: Charlie
Age: 25
Hobby: Gaming
City: Delhi
Skill: Python
--------------------'''
