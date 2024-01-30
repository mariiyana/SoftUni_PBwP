type_projection = input()
rows = int(input())
columns = int(input())
price = 0

capacity = rows * columns

if type_projection == "Premiere":
    price = capacity * 12.00
elif type_projection == "Normal":
    price = capacity * 7.50
elif type_projection == "Discount":
    price = capacity * 5.00
print(f"{price:.2f} leva")
