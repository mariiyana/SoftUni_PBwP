amount_deposited = float(input())
monthly_deposit = float(input())
annual_interest_rate = float(input()) / 100
final_amount = amount_deposited + monthly_deposit * ((amount_deposited * annual_interest_rate) / 12)
print(final_amount)
