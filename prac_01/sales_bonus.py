"""

CP1404/CP5632 - Practical
Sales Bonus

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_THRESHOLD = 1000
BONUS_MULTIPLIER_LOW = 0.1
BONUS_MULTIPLIER_HIGH = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        commission = sales * BONUS_MULTIPLIER_LOW
    else:
        commission = sales * BONUS_MULTIPLIER_HIGH
    print(f"Yous sales commissions for ${sales:.2f} is ${commission:.2f}")
    sales = float(input("Enter sales: $"))
