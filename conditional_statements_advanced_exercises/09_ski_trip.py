days = int(input())
type_of_room = input()  # room for one person, apartment or president apartment
grade = input()  # positive or negative

nights = days - 1
cost_per_day = 0
discount = 0

if type_of_room == "room for one person":
    cost_per_day = 18.00
    if days < 10:
        discount = 0
    elif days <= 15:
        discount = 0
    else:
        discount = 0
elif type_of_room == "apartment":
    cost_per_day = 25.00
    if days < 10:
        discount = 0.30
    elif days <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif type_of_room == "president apartment":
    cost_per_day = 35.00
    if days < 10:
        discount = 0.10
    elif days <= 15:
        discount = 0.15
    else:
        discount = 0.20
total_cost = nights * cost_per_day * (1 - discount)

if grade == "positive":
    total_cost *= 1.25
elif grade == "negative":
    total_cost *= 0.90
print(f"{total_cost :.2f}")
