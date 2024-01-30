number_of_climbers_group = int(input())

total_climbers = 0

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for group in range(number_of_climbers_group):
    number_of_climbers = int(input())
    total_climbers += number_of_climbers

    if number_of_climbers <= 5:
        musala += number_of_climbers
    elif number_of_climbers <= 12:
        mont_blanc += number_of_climbers
    elif number_of_climbers <= 25:
        kilimanjaro += number_of_climbers
    elif number_of_climbers <= 40:
        k2 += number_of_climbers
    else:
        everest += number_of_climbers

musala_percent = musala / total_climbers * 100
mont_blanc_percent = mont_blanc / total_climbers * 100
kilimanjaro_percent = kilimanjaro / total_climbers * 100
k2_percent = k2 / total_climbers * 100
everest_percent = everest / total_climbers * 100

print(f"{musala_percent :.2f}%")
print(f"{mont_blanc_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")
