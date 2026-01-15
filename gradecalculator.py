from utils import calculate_average, assign_letter_grade, validate_grade, find_class_extremes

students = {}

print("Grade Calculator")
print("Enter student names (blank to stop)")


while True:
    name = input("Student name: ").strip()
    if name == "":
        break

    grades = []

    for i in range(3):
        while True:
            try:
                score = input(f"Enter grade {i+1}: ")
                grades.append(validate_grade(score))
                break
            except:
                print("Invalid input. Enter a number between 0 and 100.")

    students[name] = grades

print("\nName            Average  Letter Grade")
print("------------------------------------")

for name in students:
    avg = calculate_average(students[name])
    letter = assign_letter_grade(avg)
    print(f"{name:<15} {avg:>7.2f}   {letter}")

high, high_avg, low, low_avg = find_class_extremes(students)

print(f"\nHighest average: {high} ({high_avg:.2f})")
print(f"Lowest average: {low} ({low_avg:.2f})")
