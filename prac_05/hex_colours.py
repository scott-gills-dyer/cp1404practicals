"""
CP1404 Practical
Hexadecimal colour
"""

COLOUR_TO_HEX = {"absolutezero": "#0048ba", "bitterlemon": "#cae00d", "blue2": "#0000ee", "brown3": "#cd3333",
                 "coffee": "#6f4e37", "daffodil": "#ffff31", "firebrick2": "#ee2c2c", "fuzzywuzzy": "#87421f",
                 "ghostwhite": "	#f8f8ff", "glossygrape": "#ab92b3"}

colour = input("Please choose a colour: ").lower()
while colour != "":
    print(f"{colour} is {COLOUR_TO_HEX.get(colour)}")
    colour = input("Please choose a colour: ").lower()
