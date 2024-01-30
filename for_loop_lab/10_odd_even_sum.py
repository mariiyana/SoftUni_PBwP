number = int(input())

even_position = 0
odd_position = 0

for numbers in range(number):
    current_number = int(input())
    if numbers % 2 == 0:
        even_position += current_number
    else:
        odd_position += current_number
if odd_position == even_position:
    print("Yes")
    print(f"Sum = {odd_position}")
else:
    diff = abs(even_position - odd_position)
    print("No")
    print(f"Diff = {diff}")
