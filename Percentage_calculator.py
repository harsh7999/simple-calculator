def calculate_percentage(marks, total_marks):
    percentage = (marks / total_marks) * 100
    return percentage

marks = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))

result = calculate_percentage(marks, total_marks)
print("Percentage:", result)


