name_of_student = input()
annual_grade = 0
current_class = 1
bad_attempts = 0

is_excluded = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_attempts += 1
        if bad_attempts > 1:
            is_excluded = True
            break
        continue
    current_class += 1
    annual_grade += current_grade
if is_excluded:

    print(f"{name_of_student} has been excluded at {current_class} grade")
else:
    average_grade = annual_grade / 12
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
