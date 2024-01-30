hours = int(input())
day_of_week = input()

if day_of_week == "Sunday" or not 10 <= hours <= 18:
    print("closed")
else:
    print("open")
