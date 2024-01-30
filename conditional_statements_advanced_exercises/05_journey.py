budget = float(input())
season = input()

destination = ""
percent_budget = 0
rest_place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        rest_place = "Camp"
        percent_budget = budget * 0.30
    elif season == "winter":
        rest_place = "Hotel"
        percent_budget = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        rest_place = "Camp"
        percent_budget = budget * 0.40
    elif season == "winter":
        rest_place = "Hotel"
        percent_budget = budget * 0.80
else:
    destination = "Europe"
    if season == "summer" or season == "winter":
        rest_place = "Hotel"
        percent_budget = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{rest_place} - {percent_budget:.2f}")
