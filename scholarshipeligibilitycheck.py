percentage = float(input("Enter student's percentage: "))
family_income = int(input("Enter student's family income: "))
if percentage > 85 or (percentage > 75 and family_income < 200000):
    print("Student is eligible for merit scholarship")
else:
    print("Student is NOT eligible for merit scholarship")
    #output
    #Enter student's percentage: 98
#Enter student's family income: 80000
#Student is eligible for merit scholarship
