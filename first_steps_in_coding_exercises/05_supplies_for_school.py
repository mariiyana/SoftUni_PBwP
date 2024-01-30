one_package_of_pens = 5.80
one_package_of_markers = 7.20
board_cleaner_per_liter = 1.20

number_packet_of_pens = int(input())
number_packet_of_markers = int(input())
liters_of_board_cleaner = int(input())
discount_percentages = int(input())

one_package_of_pens = number_packet_of_pens * 5.80
one_package_of_markers = number_packet_of_markers * 7.20
board_cleaner_per_liter = liters_of_board_cleaner * 1.20

price_for_all_materials = one_package_of_pens + one_package_of_markers + board_cleaner_per_liter
price_with_discount = price_for_all_materials - (price_for_all_materials * 0.10)
print(price_with_discount)
