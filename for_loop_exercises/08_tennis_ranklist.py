import math

number_of_tournaments = int(input())
number_of_points = int(input())

W = 2000  # win
F = 1200  # finalist
SF = 720  # semifinal

total_points = 0
points = 0
wins = 0

for tournament in range(number_of_tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        points += 2000
        wins += 1
    elif tournament_stage == "F":
        points += 1200
    elif tournament_stage == "SF":
        points += 720

total_points = points + number_of_points
print(f"Final points: {total_points}")

average_points = points / number_of_tournaments
print(f"Average points: {math.floor(average_points)}")

win_percent = wins / number_of_tournaments * 100
print(f"{win_percent :.2f}%")
