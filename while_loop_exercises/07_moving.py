width = int(input())
length = int(input())
height = int(input())

free_space = True
total_volume = width * length * height
command = input()

while command != "Done":
    box_count = int(command)
    total_volume -= box_count
    if total_volume < 0:
        free_space = False
        break
    command = input()
if free_space:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
