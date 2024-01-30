number = int(input())
percent_1 = 0
percent_2 = 0
percent_3 = 0
percent_4 = 0
percent_5 = 0

for numbers in range(number):
    current_number = int(input())
    if current_number < 200:
        percent_1 += 1
    elif current_number < 400:
        percent_2 += 1
    elif current_number < 600:
        percent_3 += 1
    elif current_number < 800:
        percent_4 += 1
    else:
        percent_5 += 1

print(f"{percent_1 / number :.2%}")
print(f"{percent_2 / number :.2%}")
print(f"{percent_3 / number :.2%}")
print(f"{percent_4 / number :.2%}")
print(f"{percent_5 / number :.2%}")
