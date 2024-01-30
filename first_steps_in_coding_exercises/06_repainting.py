nylon_per_square_meter = 1.50
paint_per_liter = 14.50
paint_thinner_per_liter = 5.00
bag_price = 0.40

needed_amount_nylon = int(input())
needed_amount_paint = int(input())
amount_paint_thinner = int(input())
hours = int(input())

extra_nylon = 2
extra_paint = 0.10 * needed_amount_paint

total_material_price = (needed_amount_nylon + extra_nylon) * nylon_per_square_meter \
                       + (needed_amount_paint + extra_paint) * paint_per_liter \
                       + amount_paint_thinner * paint_thinner_per_liter + bag_price

work_hours = total_material_price * 0.30
total_price = total_material_price + hours * work_hours
print(total_price)
