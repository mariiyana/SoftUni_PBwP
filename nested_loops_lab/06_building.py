number_of_floors = int(input())
number_of_rooms = int(input())

for floor in range(number_of_floors, 0, -1):
    if floor == number_of_floors:
        room_type = "L"
    elif floor % 2 == 0:
        room_type = "O"
    else:
        room_type = "A"

    for room in range(number_of_rooms):
        print(f"{room_type}{floor}{room}", end=" ")
    print()

