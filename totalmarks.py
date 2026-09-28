def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average
print("3 Marks:", total_marks(80, 90, 85))
print("5 Marks:", total_marks(70, 75, 80, 85, 90))
print("1 Mark:", total_marks(95))
'''3 Marks: (255, 85.0)
5 Marks: (400, 80.0)
1 Mark: (95, 95.0)'''
