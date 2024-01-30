hour_in = int(input())
minutes_in = int(input())

total_time_minutes = (hour_in * 60) + minutes_in + 15

hour = total_time_minutes // 60
minutes = total_time_minutes % 60

if hour > 23:
    hour = 0

print(f"{hour}:{minutes:02}")
