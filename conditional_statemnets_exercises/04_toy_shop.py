price_vacation = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
discount = 0

total_toys = puzzles + talking_dolls + teddy_bears + minions + trucks
total_sum_toys = puzzles * 2.60 + talking_dolls * 3 + teddy_bears * 4.10 \
                 + minions * 8.20 + trucks * 2
if total_toys >= 50:
    discount = total_sum_toys * 0.25

final_price = total_sum_toys - discount
rent = final_price * 0.10
profit = final_price - rent
money_left = profit - price_vacation
money_not_enough = price_vacation - profit

if profit > price_vacation:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_not_enough:.2f} lv needed.")
