kind_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

discount = 0
flower_price = 0

if kind_of_flowers == "Roses":
    flower_price = 5
    if number_of_flowers > 80:
        discount = 0.10
elif kind_of_flowers == "Dahlias":
    flower_price = 3.80
    if number_of_flowers > 90:
        discount = 0.15
elif kind_of_flowers == "Tulips":
    flower_price = 2.80
    if number_of_flowers > 80:
        discount = 0.15
elif kind_of_flowers == "Narcissus":
    flower_price = 3
    if number_of_flowers < 120:
        discount = -0.15
elif kind_of_flowers == "Gladiolus":
    flower_price = 2.50
    if number_of_flowers < 80:
        discount = -0.20

total_cost = number_of_flowers * flower_price * (1 - discount)

if budget >= total_cost:
    extra_money = budget - total_cost
    print(f"Hey, you have a great garden with {number_of_flowers} {kind_of_flowers} and {extra_money :.2f} leva left.")

else:
    not_enough_money = total_cost - budget
    print(f"Not enough money, you need {not_enough_money :.2f} leva more.")
