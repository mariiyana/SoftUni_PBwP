book = input()

command = input()
books_count = 0
while command != "No More Books":
    current_book = command
    if current_book == book:
        break
    books_count += 1
    command = input()
if command == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
else:
    print(f"You checked {books_count} books and found it.")
