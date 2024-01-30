starting_number = int(input())
bonus = 0

if starting_number <= 100:
    bonus = 5
elif 1000 >= starting_number > 100:
    bonus = 0.20 * starting_number
else:
    bonus = 0.10 * starting_number

if starting_number % 2 == 0:
    bonus = bonus + 1

if starting_number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(starting_number + bonus)

