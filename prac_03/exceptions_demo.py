"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("denominator cannot be 0!")
        else:
            fraction = numerator / denominator
            print(fraction)
            is_valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")

# Question 1. When the input is not a int (e.g. float or str)
# Question 2. When the denominator is 0
# Question 3. Yes
