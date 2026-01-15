def calculate_average(grades):
    return sum(grades) / len(grades)


def assign_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def validate_grade(score):
    score = float(score)
    if 0 <= score <= 100:
        return score
    else:
        raise ValueError


def find_class_extremes(students):
    averages = {}

    for name in students:
        averages[name] = calculate_average(students[name])

    highest = max(averages, key=averages.get)
    lowest = min(averages, key=averages.get)

    return highest, averages[highest], lowest, averages[lowest]
