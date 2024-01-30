pages_current_book = int(input())
pages_read = int(input())
number_of_days = int(input())
number_of_hours = pages_current_book // pages_read
needed_hours = number_of_hours / number_of_days
print(needed_hours)
