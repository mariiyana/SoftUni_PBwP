group_budget = int(input())
season = input()
number_of_fishermen = int(input())

price_boat = 0
group_discount = 0
extra_discount = 0

if season == "Spring":
    price_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if number_of_fishermen <= 6:
    group_discount = 0.10
elif number_of_fishermen <= 11:
    group_discount = 0.15
else:
    group_discount = 0.25

if season != "Autumn" and number_of_fishermen % 2 == 0:
    extra_discount = 0.05

total_cost = price_boat * (1 - group_discount) * (1 - extra_discount)
money_left = group_budget - total_cost

if money_left >= 0:
    print(f"Yes! You have {abs(money_left) :.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left) :.2f} leva.")
