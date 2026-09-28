from functools import reduce

employees = [
    {"name": "Alice", "department": "IT", "salary": 50000},
    {"name": "Bob", "department": "HR", "salary": 40000},
    {"name": "Charlie", "department": "IT", "salary": 60000},
    {"name": "Diana", "department": "Finance", "salary": 55000}
]
it_employees = list(filter(lambda e: e["department"] == "IT", employees))
hiked = list(map(lambda e: {"name": e["name"], 
                            "department": e["department"], 
                            "salary": int(e["salary"] * 1.1)}, it_employees))
total_salary = reduce(lambda a, b: a + b["salary"], hiked, 0)

print("IT Employees after hike:", hiked)
print("Total IT salary expenditure:", total_salary)
'''IT Employees after hike: [{'name': 'Alice', 'department': 'IT', 'salary': 55000}, {'name': 'Charlie', 'department': 'IT', 'salary': 66000}]
Total IT salary expenditure: 121000'''
