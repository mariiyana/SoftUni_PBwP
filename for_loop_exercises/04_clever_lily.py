age = int(input())
price_for_wm = float(input())
price_per_toy = int(input())

total_money = 0
total_toys = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        current_money = birthday * 5
        total_money += current_money
        total_money -= 1
    else:
        total_toys += 1

money_toys = total_toys * price_per_toy
total_money += money_toys

if total_money >= price_for_wm:
    money_left = total_money - price_for_wm
    print(f"Yes! {money_left:.2f}")
else:
    needed_money = price_for_wm - total_money
    print(f"No! {needed_money:.2f}")
