import math

series_name = input()
duration_of_episode = int(input())
duration_of_break = int(input())

time_for_lunch = duration_of_break / 8
time_to_rest = duration_of_break / 4

time_left = duration_of_break - time_for_lunch - time_to_rest

time_left_1 = abs(time_left - duration_of_episode)
time_left_2 = math.ceil(time_left_1)
if time_left >= duration_of_episode:
    print(f"You have enough time to watch {series_name} and left with {time_left_2} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {time_left_2} more minutes.")







