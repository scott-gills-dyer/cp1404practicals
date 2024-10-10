"""

CP1404/CP5632 - Practical
Shop Calculator


 DISCOUNT_THRESHOLD = 100
 DISCOUNT = 0.1

total_price = 0
get number_of_items
while number_of_items is less than 0
    print invalid message
    get number_of_items
repeat number_of_items times
    get item_price
    total_price += item_price
if total_price > DISCOUNT_THRESHOLD
    total_price = total_price - (DISCOUNT * total_price)
print number_of_items, total_price
"""

DISCOUNT_THRESHOLD = 100
DISCOUNT_PERCENTAGE = 0.9

total_price = 0
number_of_items = int(input("How many items are you buying: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("How many items are you buying: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT_PERCENTAGE

print(f"Total price for {number_of_items} items is {total_price:.2f}")
