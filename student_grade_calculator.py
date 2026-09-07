def calculate_grade(mark):
    if mark >= 80:
        return "A+"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "A-"
    elif mark >= 50:
        return "B"
    elif mark >= 40:
        return "C"
    elif mark >= 33:
        return "D"
    else:
        return "F"


print("Student Grade Calculator")

name = input("Enter student name: ")
mark = float(input("Enter mark (0-100): "))

if 0 <= mark <= 100:
    grade = calculate_grade(mark)
    print(f"\nStudent: {name}")
    print(f"Mark: {mark:g}")
    print(f"Grade: {grade}")
else:
    print("Invalid mark. Please enter a value between 0 and 100.")
