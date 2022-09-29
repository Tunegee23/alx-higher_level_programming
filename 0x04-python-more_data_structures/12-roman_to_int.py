#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Returns the roman value of a character
    None if its not a Roman Character
    """
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'VI': 6, 'I': 1}
    for roman in reversed(roman_string):
        arabic = digits[roman]
        total += arabic if total < arabic * 5 else -arabic
    return total
