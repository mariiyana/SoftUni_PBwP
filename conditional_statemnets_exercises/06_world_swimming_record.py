import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

time = distance_in_meters * time_in_seconds
added_time = math.floor(distance_in_meters / 15) * 12.5
total_time = time + added_time

if record_in_seconds <= total_time:
    diff = total_time - record_in_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

