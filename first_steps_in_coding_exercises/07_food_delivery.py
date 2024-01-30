chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery_fee = 2.50

number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegetarian_menu = int(input())

total_order = (number_of_chicken_menu * chicken_menu) + (number_of_fish_menu * fish_menu) + \
              (number_of_vegetarian_menu * vegetarian_menu)

dessert_price = total_order * 0.20
total_order_price = total_order + dessert_price + delivery_fee
print(total_order_price)
