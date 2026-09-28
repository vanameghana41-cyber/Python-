grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks_list = [35, 67, 89, 23, 40, 55]
for m in marks_list:
    print(f"Marks: {m}, Result: {grade(m)}")
'''Marks: 35, Result: Fail
Marks: 67, Result: Pass
Marks: 89, Result: Pass
Marks: 23, Result: Fail
Marks: 40, Result: Pass
Marks: 55, Result: Pass'''
