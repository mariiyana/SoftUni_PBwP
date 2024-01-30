unsatisfied_grades = int(input())

problems_count = 0
unsatisfied_grade_count = 0
grade = 0
last_problem = ""

command = input()
while command != "Enough":
    problem_name = command
    problem_grade = int(input())

    last_problem = problem_name
    grade += problem_grade
    problems_count += 1

    if problem_grade <= 4:
        unsatisfied_grade_count += 1
        if unsatisfied_grade_count >= unsatisfied_grades:
            break
    command = input()

if command == "Enough":
    average_score = grade / problems_count
    print(f"Average score: {average_score :.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {unsatisfied_grade_count} poor grades.")
