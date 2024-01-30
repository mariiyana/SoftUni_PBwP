hour_of_exam = int(input())
min_of_exam = int(input())
arrival_hour = int(input())
min_of_arrival = int(input())

time_of_exam_in_min = hour_of_exam * 60 + min_of_exam
time_of_arrival_in_min = arrival_hour * 60 + min_of_arrival

diff = time_of_arrival_in_min - time_of_exam_in_min
if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hh = diff // 60
        mm = diff % 60
        print(f"{hh}:{mm :02d} hours after the start")
elif diff >= -30:
    print("On time")
    if not diff == 0:
        print(f"{abs(diff)} minutes before the start")
else:
    print("Early")
    if diff > -60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hh = abs(diff) // 60
        mm = abs(diff) % 60
        print(f"{hh}:{mm :02d} hours before the start")
