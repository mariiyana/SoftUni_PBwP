import sys

number = int(input())

max_sum = -sys.maxsize
sum_of_numbers = 0

for numbers in range(number):
    current_number = int(input())
    if current_number > max_sum:
        max_sum = current_number

    sum_of_numbers += current_number

if max_sum == sum_of_numbers - max_sum:
    print("Yes")
    print(f"Sum = {max_sum}")
else:
    sum_of_numbers = sum_of_numbers - max_sum
    print("No")
    print(f"Diff = {abs(max_sum - sum_of_numbers)}")
