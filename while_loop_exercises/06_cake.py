width = int(input())
length = int(input())

is_cake_over = False
total_pieces = width * length
command = input()

while command != "STOP":
    current_pieces = int(command)
    total_pieces -= current_pieces
    if total_pieces < 0:
        is_cake_over = True
        break
    command = input()
if is_cake_over:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")
