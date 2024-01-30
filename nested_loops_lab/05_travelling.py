destination = input()

while destination != "End":
    current_budget = float(input())
    current_money = 0
    while current_money < current_budget:
        saved_money = float(input())
        current_money += saved_money
    print(f"Going to {destination}!")
    destination = input()
