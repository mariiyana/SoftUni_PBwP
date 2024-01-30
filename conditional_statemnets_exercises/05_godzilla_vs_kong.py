film_budget = float(input())
number_of_extras = int(input())
price_extra_outfit = float(input())

sum_of_decor = film_budget * 0.1
sum_of_outfits = number_of_extras * price_extra_outfit

if number_of_extras > 150:
    sum_of_outfits = sum_of_outfits * 0.90

total_sum = sum_of_decor + sum_of_outfits
money_left = abs(film_budget - total_sum)

if film_budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")
