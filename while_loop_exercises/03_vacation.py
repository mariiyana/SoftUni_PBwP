money_needed = float(input())
current_money = float(input())

days_count = 0
spend_days = 0

while current_money < money_needed and spend_days < 5:
    action = input()
    action_money = float(input())

    if action == "spend":
        current_money -= action_money
        spend_days += 1
        if current_money < 0:
            current_money = 0
    elif action == "save":
        current_money += action_money
        spend_days = 0

    days_count += 1

if spend_days == 5:
    print("You can't save the money.")
    print(days_count)
elif current_money >= money_needed:
    print(f"You saved the money for {days_count} days.")
