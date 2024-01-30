month = input()
number_of_stays = int(input())

discount_studio = 0
studio_cost = 0
discount_apartment = 0
apartment_cost = 0


if month == "May" or month == "October":
    studio_cost = 50
    if number_of_stays > 14:
        discount_studio = 0.30
    elif number_of_stays > 7:
        discount_studio = 0.05
    apartment_cost = 65

elif month == "June" or month == "September":
    studio_cost = 75.20
    if number_of_stays > 14:
        discount_studio = 0.20
    apartment_cost = 68.70

elif month == "July" or month == "August":
    studio_cost = 76
    apartment_cost = 77

if number_of_stays > 14:
    discount_apartment = 0.10

studio_cost = studio_cost * (1 - discount_studio)
apartment_cost = apartment_cost * (1 - discount_apartment)

total_studio_cost = studio_cost * number_of_stays
total_apartment_cost = apartment_cost * number_of_stays

print(f"Apartment: {total_apartment_cost :.2f} lv.")
print(f"Studio: {total_studio_cost :.2f} lv.")
