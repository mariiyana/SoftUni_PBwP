actor_name = input()
academy_points = float(input())
number_of_jury = int(input())

total_points = academy_points

for actor in range(number_of_jury):
    name_of_jury = input()
    jury_points = float(input())
    total_jury_points = len(name_of_jury) * jury_points / 2
    total_points += total_jury_points

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points :.1f} more!")
