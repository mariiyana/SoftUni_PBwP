budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

price_of_video_cards = video_cards * 250
price_of_processors = processors * (price_of_video_cards * 0.35)
price_of_ram_memory = ram_memory * (price_of_video_cards * 0.10)

sum_of_all = price_of_video_cards + price_of_processors + price_of_ram_memory

if video_cards > processors:
    sum_of_all = sum_of_all * 0.85

money_left = abs(sum_of_all - budget)
if budget >= sum_of_all:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")
